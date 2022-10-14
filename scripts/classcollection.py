import cv2
import uuid #unique identifyier
import os
import time
import tarfile

#CLass-Images to Collect
labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5
#Folders
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')
mode = 0o666
#mkdir
if not os.path.exists(IMAGES_PATH):
    #Linux
    if os.name == 'posix':
        os.makedirs(IMAGES_PATH, mode, exist_ok=True)
    #Windows
    if os.name == 'nt':
        os.makedirs(IMAGES_PATH, mode)
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path, mode)

for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

if not os.path.exists(LABELIMG_PATH):
    os.makedirs(LABELIMG_PATH, mode)    
    
