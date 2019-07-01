#!/usr/bin/python3
import cv2

cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
# detecting red colour   
    redimg=cv2.inRange(frame,(0,0,0),(40,40,255))
    cv2.imshow('liveredcoloured',redimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
