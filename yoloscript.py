from ultralytics import YOLO
import cv2
import math 


# 0 Webcam
# 1 OBS Virtual Cam
cap = cv2.VideoCapture(2)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("customv1.0.pt")

y_limit = 240

idx = 0

while True:
    success, img = cap.read()
    results = model(img, stream=True, verbose=False)


    start_point = (0,y_limit)
    end_point = (640,y_limit)
    
    cv2.line(img, start_point,end_point,(255,255,255),2)
    
    # coordinates
    for r in results:
        boxes = r.boxes
        
        for box in boxes:
            
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # put box in cam
            if confidence >= 0.75:
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

                print("box y location",y1)
                if y1 > y_limit:
                    
                    object = img[y1:y2, x1:x2]
                    resPath = f'resultsimg\{idx}.jpg'
                    
                    cv2.imwrite(resPath, object)
                    idx += 1
                    print(idx, resPath)
                
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()