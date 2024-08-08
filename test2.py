import cv2
import torch
import numpy as np


# Load mô hình YOLOv5 đã huấn luyện (sử dụng mô hình pre-trained)
model = torch.hub.load('ultralytics/yolov5', 'custom', '/Users/giapngoclinh/Documents/yolo/Bản sao last.pt')  # Thay 'yolov5s' bằng mô hình khác nếu cần

# Mở camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc khung hình từ camera.")
        break
    
    # Chuyển đổi khung hình từ BGR (OpenCV) sang RGB (mô hình YOLOv5 yêu cầu)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Dự đoán đối tượng trong khung hình
    results = model(frame_rgb)
    
    # Vẽ các kết quả dự đoán lên khung hình
    annotated_frame = results.render()[0]
    
    # Chuyển đổi khung hình từ RGB về BGR để hiển thị bằng OpenCV
    annotated_frame_bgr = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
    
    # Hiển thị khung hình đã đánh dấu
    cv2.imshow("YOLO", annotated_frame_bgr)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng tất cả các cửa sổ OpenCV
cap.release()
cv2.destroyAllWindows()
