import mediapipe as mp
import cv2
import uuid #unique identifyier
import numpy as np
import os
import time
import tarfile

#Render lankmarks in hand
mp_drawing = mp.solutions.drawing_utils #joint tracking
mp_drawing_styles = mp.solutions.drawing_styles
#Hands model
mp_hands = mp.solutions.hands
hands_video = mp_hands.Hands(static_image_mode=False,
                    max_num_hands=2,
                    min_detection_confidence=0.7,
                    min_tracking_confidence=0.4)


#Webcam feed, video capture object
cap = cv2.VideoCapture(0)
#cap.set(3,1280) #Resolution
#cap.set(4,960)
# Named window for resizing
cv2.namedWindow('Hands Landmarks Detection', cv2.WINDOW_NORMAL)
#Variable to store the time of the previous frame
time1 = 0


with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read() #Read the frame 
        ### LANDMARKS DETECTION ####       
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Flip on horizontal
        image = cv2.flip(image, 1) #natural selfie view
        image.flags.writeable = False  #Flag
        #Detections
        results = hands.process(image) #landmarks detection after RGB conv
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
        time2 = time.time() #Current time
        if (time2 - time1) > 0:
            # Frames per second
            f_p_s = 1.0 / (time2 - time1)
            # Write the calculated number of framesper second on the frame
            cv2.putText(image, 'FPS: {}'.format(int(f_p_s)),(10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
        #Update frame time
        time1 = time2
        cv2.imshow('Hand Tracking Detection', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


