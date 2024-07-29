from ultralytics import YOLO
import cv2
import math 


# the default video capture device should be 0,
# OBS Virtual camera should be the last possible, in our case 2.
# adjust accordingly.
camPort = 2

cap = cv2.VideoCapture(camPort)

# YOLOv8 caps the resolution to 640x480, recommended to proportionalize it.
cap.set(3, 640)
cap.set(4, 480)

# this is the car license plate custom model.
# refer to https://github.com/ultralytics/ultralytics for creating more models
model = YOLO("customv1.0.pt")

# this is to limit the detection area according to the y axis.
y_limit = 240


# this will be used as the image name and reference.
idx = 0

while True:
    success, img = cap.read()

    # 👇 YOLOv8 pipeline
    results = model(img, stream=True, verbose=False)

    # visualize the area of limitation 
    start_point = (0,y_limit)
    end_point = (640,y_limit)
    cv2.line(img, start_point,end_point,(255,255,255),2)
    
    for r in results:
        boxes = r.boxes    
        for box in boxes:
            # bounding box data
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            # confidence matric, not used.
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            if confidence >= 0.75:
                # visualize the bounding box area
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                print("box y location",y1)
                if y1 > y_limit:
                    object = img[y1:y2, x1:x2]
                    resPath = f'resultsimg\{idx}.jpg'
                    
                    # saving cropped image according to the bounding box data
                    # creates save this image
                    cv2.imwrite(resPath, object)
                    idx += 1
                    print(idx, resPath)
                
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()