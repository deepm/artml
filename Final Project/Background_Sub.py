import numpy as np
import cv2 as cv
cap = cv.VideoCapture('fish1.mp4')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG(10)
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    foreground_mask = cv.bitwise_and(frame,frame,mask=255 - fgmask)
    foreground_mask= cv.inpaint(foreground_mask,fgmask,3,cv.INPAINT_TELEA)
    background_mask = cv.bitwise_and(frame,frame,mask=fgmask)
    
    cv.imshow('frame',background_mask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()