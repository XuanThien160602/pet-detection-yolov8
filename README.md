## YOLOv8 - Nhận diện và quản lý vật nuôi trang trại
Ứng dụng web sử dụng YOLOv8 để nhận diện vật nuôi từ hình ảnh và camera trực tiếp.
Dự án được xây dựng bằng Python, Flask, OpenCV và YOLOv8, cho phép người dùng tải ảnh lên hoặc sử dụng camera để thực hiện nhận diện vật nuôi. Sau khi nhận diện, hệ thống hiển thị bounding box, tên vật nuôi, độ tin cậy và thống kê số lượng từng loại vật nuôi.


##  Giới thiệu

Đề tài xây dựng một hệ thống nhận diện vật nuôi sử dụng mô hình YOLOv8 Object Detection.

Hệ thống có hai chức năng chính:
- Nhận diện vật nuôi thông qua ảnh có sẵn
- Nhận diện vật nuôi trực tiếp qua camera
Kết quả nhận diện được thể hiện trực quan bằng bounding box trên hình ảnh/video và thống kê số lượng vật nuôi được phát hiện.

---

## Chức năng
1. Nhận diện từ hình ảnh
Người dùng có thể:
- Chọn hình ảnh từ máy tính.
- Upload hình ảnh lên hệ thống.
- Mô hình YOLOv8 thực hiện nhận diện.
- Hiển thị bounding box quanh vật nuôi.
- Hiển thị tên vật nuôi.
- Hiển thị confidence score.
- Thống kê số lượng từng loại vật nuôi.

2. Nhận diện qua camera
Người dùng có thể:
- Bật camera trực tiếp từ giao diện web.
- Gửi các frame hình ảnh đến backend.
- YOLOv8 xử lý từng frame.
- Hiển thị kết quả nhận diện trực tiếp.
- Thống kê số lượng vật nuôi đang được phát hiện.
- Tắt camera khi không sử dụng.
---
## Công nghệ sử dụng
| Công nghệ   | Vai trò                        |
| ----------- | ------------------------------ |
| Python      | Ngôn ngữ lập trình chính       |
| Flask       | Xây dựng backend và web server |
| YOLOv8      | Nhận diện vật nuôi             |
| Ultralytics | Thư viện triển khai YOLOv8     |
| OpenCV      | Xử lý hình ảnh và camera       |
| HTML/CSS    | Xây dựng giao diện             |
| NumPy       | Xử lý dữ liệu hình ảnh         |
| Git/GitHub  | Quản lý mã nguồn               |
| Render      | Deploy ứng dụng web            |

## Quy trình nhận diện ảnh
Người dùng chọn ảnh
        ->
Upload ảnh
        ->
Flask nhận file
        ->
YOLOv8 xử lý ảnh
        ->
Phát hiện vật nuôi
        ->
Lấy Label + Bounding Box + Confidence
        ->
Đếm số lượng vật nuôi
        ->
OpenCV vẽ kết quả
        ->
Hiển thị ảnh kết quả

## Quy trình nhận diện camera
Bật camera
    ->
OpenCV lấy frame
    ->
YOLOv8 xử lý frame
    ->
Phát hiện vật nuôi
    ->
Vẽ Bounding Box
    ->
Cập nhật số lượng
    ->
Hiển thị frame lên trình duyệt

Khi người dùng tắt camera, hệ thống giải phóng camera bằng OpenCV và hiển thị trạng thái camera đang tắt.

## Kết quả nhận diện

- Tên vật nuôi
- Bounding Box
- Confidence Score
- Số lượng

## Cài đặt và chạy chương trình
1. Clone project

git clone https://github.com/XuanThien160602/pet-detection-yolov8.git

Di chuyển vào thư mục project: cd pet-detection-yolov8

2. Tạo môi trường ảo

python -m venv venv

3. Kích hoạt môi trường ảo trên Windows

venv\Scripts\Activate.ps1

4. Cài đặt thư viện

pip install -r requirements.txt

5. Chạy ứng dụng

python app.py

Sau đó mở trình duyệt: http://127.0.0.1:5000

## Giao diện ứng dụng

Giao diện chính:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/38cb662c-d2cb-4915-ac88-06e562e8b3b3" />
Chức năng nhận diện ảnh:

<img width="1364" height="713" alt="image" src="https://github.com/user-attachments/assets/9dd7f4eb-d4be-427e-9083-bb53903b4211" />
Kết quả nhận diện:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/993afeec-ef50-4782-94e4-9739e1de9e71" />
Chức năng nhận diện camera:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/6de5e999-91b3-4456-ba4c-3de7479e9e79" />
Kết quả nhận diện camera:

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ffc9d17c-351f-42b9-94ee-5bd01345cd06" />



