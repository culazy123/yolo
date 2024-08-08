import cv2
import torch
import numpy as np

# Load mô hình YOLOv5 đã huấn luyện (sử dụng mô hình pre-trained)
model = torch.hub.load('ultralytics/yolov5', 'custom','last.pt')  # Thay 'yolov5s' bằng mô hình khác nếu cần

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    #print(frame)
    #print("--------------------------------------------------------")
    results = model(frame)
    print(frame.shape)
    print(results)
    annotated_frame = results.render()[0]
    cv2.imshow("YOLO", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()