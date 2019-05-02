import numpy as np
import cv2 as cv
import glob


vid_lst = glob.glob("vids/Sea_Turtle.mp4")

video = cv.VideoCapture(vid_lst[0])
file_name = vid_lst[0]
out_file_name = file_name[5:-4] + "_out.avi"
mask_file_name = file_name[5:-4] + "_mask.avi"

_, frame = video.read()

w, h,_ = frame.shape

fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
fourcc = cv.VideoWriter_fourcc('M','J','P','G')

mask_video = cv.VideoWriter(mask_file_name, fourcc, 20.0, (int(video.get(3)), int(video.get(4))))
out_video = cv.VideoWriter(out_file_name, fourcc, 20.0, (int(video.get(3)), int(video.get(4))))


while(video.isOpened()):

    ret, frame = video.read()
    
    if ret == False:
        break

    fgmask = fgbg.apply(frame)
    frame = cv.bitwise_and(frame,frame, mask = fgmask)
    frame2 = cv.bitwise_and(frame,frame, mask = 255 - fgmask)
    cv.imshow('frame',frame)

    out_mask = cv.cvtColor(fgmask,cv.COLOR_GRAY2RGB)
    mask_video.write(out_mask)
    out_video.write(frame)
    
    
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break


video.release()
out_video.release()
mask_video.release()
cv.destroyAllWindows()