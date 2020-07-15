import cv2

import numpy as np

cap = cv2.VideoCapture(0)
backFrame = cv2.imread('./BG.jpg')

while cap.isOpened():

    #capturing each frame
    ret, frame = cap.read()

    if ret:

        # converting rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)  #to show with winow name as "hsv"

        red=np.uint8([[[0,0,255]]])   # taking bgr values of red

        hsv_red=cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        #print(hsv_red)    //Can print values and check  [0,255,255] hsv value of red

        #lower: hue-10,100,100   to Higher: hue+10,255,255
        # So our hue value is 0, So our range will be from 0,100,100 to 10,255,255

        l_red=np.array([-10,100,100])
        h_red=np.array([10,255,255])

        mask=cv2.inRange(hsv, l_red, h_red)  # this mask contain all red area
        #cv2.imshow("mask",mask)

        part1 = cv2.bitwise_and(backFrame, backFrame, mask=mask )   # just showing background image at the red area
        #cv2.imshow("part1", part1)

        mask=cv2.bitwise_not(mask)  #leaving red area, now this mask contain every area which is not red

        part2 = cv2.bitwise_and(frame, frame, mask=mask)  #showing current frame image at the  non red area

        cv2.imshow("invisible", part1 + part2)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()