import cv2

cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, backFrame = cap.read()

    if ret:
        cv2.imshow("BG",backFrame)

        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("BG.jpg",backFrame)
            break

cap.release()
cv2.destroyAllWindows()

