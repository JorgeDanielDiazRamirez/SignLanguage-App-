import mediapipe as mp
import cv2
import uuid #unique identifyier
import numpy as np
import os
import time
import tarfile

#Render lankmarks in hand
mp_drawing = mp.solutions.drawing_utils #joint tracking
#Hands model
mp_hands = mp.solutions.hands

#Save output images
IMAGES_PATH = os.path.join('Tensorflow', 'Mediapipe', 'images', 'collectedimages')
mode = 0o666
#mkdir
if not os.path.exists(IMAGES_PATH):
    #Linux
    if os.name == 'posix':
        os.makedirs(IMAGES_PATH, mode, exist_ok=True)
    #Windows
    if os.name == 'nt':
        os.makedirs(IMAGES_PATH, mode)

#Webcam feed
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False  #Flag
        #Detections
        results = hands.process(image)
        image.flags.writeable = True #Flag
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #print(results)
        #Rendering
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=3)
                                        )
        cv2.imwrite(os.path.join(IMAGES_PATH, '{}.jpg'.format(uuid.uuid1())), image)
        time.sleep(2)
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


