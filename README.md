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

## Mô hình AI

Dự án sử dụng YOLOv8 của Ultralytics cho bài toán Object Detection.
Mô hình được sử dụng trong ứng dụng là: runs/detect/train2/weights/best.pt
