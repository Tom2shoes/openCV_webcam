import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img_counter = 0

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# 720p
change_res(1280, 720)


while(True):
    ret, frame = cap.read()
    k = cv2.waitKey(20)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame75 = rescale_frame(frame, percent=10)

    cv2.imshow('frame', gray)

    if k & 0xFF == ord('q'):
        # Q to quit
        break

    elif k%256 == 32:
        # SPACE to take picture
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
       
cap.release()
cv2.destroyAllWindows()