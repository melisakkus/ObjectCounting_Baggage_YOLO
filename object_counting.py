from collections import defaultdict

import cv2
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
width , height = 1000,800
number_of_luggages = 0

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.resize(frame,(width,height))

    #object tracking
    results = model.track(frame,persist=True,verbose=False)[0]
    bboxes = np.array(results.boxes.data.tolist(),dtype="int")

    text_line = "Reference Line"
    cv2.line(frame,(341,407),(631,623),color_red,thickness)
    cv2.rectangle(frame,(370,380),(500,405),color_red,reference_thickness)
    cv2.putText(frame,text_line,(375,395),font,font_scale,color_white,reference_thickness)

    #bagajların ortasına nokta atılacak
    for box in bboxes:
        if len(box) == 7:
            x1,y1,x2,y2,track_id,score,class_id = box
            if class_id == suitcase_id:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                text = "ID:{} LUGGAGE".format(track_id)
                cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                center_coordinates = (cx, cy)

                if cx < 600:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color_white, 2)
                    text = "ID:{} LUGGAGE".format(track_id)
                    cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    counter[track_id] = x1,y1,x2,y2

                number_of_luggages =len(list(counter.keys()))
                info = f"{number_of_luggages} luggages detected"
                cv2.rectangle(frame, (5, 5), (200, 30),color_black,2)
                cv2.putText(frame, info, (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_red, 2)

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
print(f"{number_of_luggages} luggages detected")

