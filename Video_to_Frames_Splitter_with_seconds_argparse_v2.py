'''import cv2
vidcap = cv2.VideoCapture('C:/Users/soumyama/Desktop/helmet_detection_1.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./imgs/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1'''

import cv2
import argparse

ap= argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Enter Input File Path")
ap.add_argument("-o", "--output", required=True, help="Enetr Output File Path")
args= vars(ap.parse_args())

#vid_cap = cv2.VideoCapture('C:/Users/soumyama/Desktop/helmet_detection_2.avi')
vid_cap= cv2.VideoCapture(args['input'])
count = 0
success = True
fps = int(vid_cap.get(cv2.CAP_PROP_FPS))
seconds= 1
while success:
    success,image = vid_cap.read()
    print('read a new frame:',success)
    if count%(seconds*fps) == 0 :
         cv2.imwrite(str(args['output'])+'frame%d.jpg'%count,image)
         print('successfully written 10th frame')
    count+=1
    




