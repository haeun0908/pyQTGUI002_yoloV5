import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

model = torch.hub.load('ultralytics/yolov5',
                       'custom',
                       path='best.pt',
                       force_reload=True)

model.eval()
cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
    break

  results = model(frame)
  annotated_frame = results.render()[0]

  cv2.imshow('YOLOv5 Custom', annotated_frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()