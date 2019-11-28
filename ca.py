import cv2
import glob
import os
vc=cv2.VideoCapture("C:/yzn/picture/computer.mp4")
c=1
if vc.isOpened():
  rval,frame=vc.read()
else:
  rval=False
while rval:
  rval,frame=vc.read()
  cv2.imwrite('C:/yzn/picture/computer/'+str(c)+'.jpg',frame)
  c=c+1
  cv2.waitKey(1)
vc.release()
vc=cv2.VideoCapture("C:/yzn/picture/computer1.mp4")
c=1
if vc.isOpened():
  rval,frame=vc.read()
else:
  rval=False
while rval:
  rval,frame=vc.read()
  cv2.imwrite('C:/yzn/picture/computer1/'+str(c)+'.jpg',frame)
  c=c+1
  cv2.waitKey(1)
vc.release()