#!/usr/bin/python3
import cv2

cap=cv2.VideoCapture(0)

tp1=cap.read()[1]  #take1
tp2=cap.read()[1]  #take2
tp3=cap.read()[1]  #take3

#converting to gray
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#now creating image differentiater
def img_diff(x,y,z):
    #difference between x,y -- gray1,gray2 --d1
    d1=cv2.absdiff(x,y)
    #difference between y,z -- gray2,gray3 --d2
    d2=cv2.absdiff(y,z)
    #abs diff d1-d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg

#now applying function
while cap.isOpened():
    status,frame=cap.read()   #continue image takercdd
    motionimg=img_diff(gray1,gray2,gray3)
    #replacing image frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #passing live img to gray3
    #cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
        
cv2.destroyAllWindows()
cap.release()
    
