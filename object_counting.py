from collections import defaultdict
from email.policy import default

import cv2
import imutils
from ultralytics import YOLO
import numpy as np

video_path = "test_videos/baggage_carousel.mp4"
cap = cv2.VideoCapture(video_path)

model_name = "models/yolo11n.pt"
model = YOLO(model_name)

counter = {}
track_history = defaultdict(lambda: [])

suitcase_id = 28
thickness = 2
reference_thickness = 1
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (0, 0, 255)
color_green = (0, 255, 0)
font_scale = 0.5
font = cv2.FONT_HERSHEY_SIMPLEX
width , height = 720,800

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.resize(frame,(width,height))


    text_line = "Reference Line"
    cv2.line(frame,(0,int(height/2)-12),(width,int(height/2)-12),color_red,thickness)
    cv2.rectangle(frame,(10,int(height/2)),(140,int(height/2)+25),color_red,reference_thickness)
    cv2.putText(frame,text_line,(15,int(height/2)+15),font,font_scale,color_red,reference_thickness)

    #object tracking
    results = model.track(frame,persist=True,verbose=False)[0]
    bboxes = np.array(results.boxes.data.tolist(),dtype="int")
    for box in bboxes:
        if len(box) == 7:
            x1,y1,x2,y2,track_id,score,class_id = box
        elif len(box) == 6:
            x1, y1, x2, y2, score, class_id = box
            track_id = -1  # Takip ID'si yoksa -1 olarak ayarla.
        else:
            # Beklenmeyen bir durum, bu kutuyu atla veya hata logla.
            print(f"Uyarı: Beklenmeyen kutu veri uzunluğu: {len(box)}. Kutu atlanıyor.")
            continue

    cv2.imshow("Subway Object Counting",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
