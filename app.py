from flask import Flask, request, jsonify, send_file, Response, render_template, redirect, url_for
from ultralytics import YOLO
import cv2
import os
import numpy as np
from collections import Counter

app = Flask(__name__)
model = YOLO("runs/detect/train2/weights/best.pt")

camera_on = False
camera = None
latest_counts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image')
def image_page():
    return render_template('image.html')


@app.route("/camera", methods=["GET", "POST"])
def camera():
    global camera_on
    if request.method == "POST":
        action = request.form.get("action")
        if action == "start":
            camera_on = True
        elif action == "stop":
            camera_on = False
    return render_template("camera.html", camera_on=camera_on)
@app.route("/counts")
def get_counts():
    global latest_counts
    return jsonify(latest_counts)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    os.makedirs("static/uploads", exist_ok=True)
    os.makedirs("static/outputs", exist_ok=True)

    filepath = os.path.join("static/uploads", file.filename)
    file.save(filepath)

    results = model(filepath)
    img = cv2.imread(filepath)

    labels = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = results[0].names[cls]
        labels.append(label)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Đếm số lượng vật nuôi
    counts = Counter(labels)

    output_path = os.path.join("static/outputs", f"result_{file.filename}")
    cv2.imwrite(output_path, img)

    return render_template(
        "result.html",
        original_file=file.filename,
        result_file=f"result_{file.filename}",
        counts=counts
    )

def gen_frames():
    global camera_on, latest_counts
    cap = None

    while True:
        if camera_on:
            if cap is None:
                cap = cv2.VideoCapture(0)

            success, frame = cap.read()
            if not success:
                break

            results = model(frame)
            frame = results[0].plot()

            # Cập nhật latest_counts
            counts = {}
            for box in results[0].boxes:
                cls = int(box.cls[0])
                label = results[0].names[cls]
                counts[label] = counts.get(label, 0) + 1
            latest_counts = counts

        else:
            if cap is not None:
                cap.release()
                cap = None
            frame = cv2.imread("static/camera_off.jpg")
            latest_counts = {}

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    if not os.path.exists("static/camera_off.jpg"):
        off = 255 * np.ones((480, 640, 3), dtype=np.uint8)
        cv2.putText(off, "Camera dang tat", (120, 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imwrite("static/camera_off.jpg", off)
    app.run(debug=True)
