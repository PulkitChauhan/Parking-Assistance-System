import cv2
import numpy as np
import os
import pickle
import time
import datetime



def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(circles)<8:
            #print(x,y)
            circles.append(tuple([x, y]))     
            print(circles)
            
           # f = open("file.txt", "w")

           # f.write(circles)
            
     
 
cap = cv2.VideoCapture(0)
 
cv2.namedWindow("Frame1")
cv2.setMouseCallback("Frame1", mouse_drawing)
 
circles = []
#print(circles)
while True:
    _, frame1 = cap.read()
 
    for center_position in circles:
        cv2.circle(frame1, center_position, 5, (0, 0, 255), -1)
    #text="Hey Pulkit!"
    #cv2.putText(frame1,"STATUS:{}".format(text),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    #cv2.circle(frame1,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    #cv2.putText(frame1, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		#(10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 0.5)
 
    cv2.imshow("Frame1", frame1)
    #status="Pulkit"
    #cv2.putText(frame1,"Park{} occupied",cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
 
    key = cv2.waitKey(1)
    #a=np.savetxt("file.txt",np.array(circles),fmt="%s")
    pickle.dump(circles, open('file.txt', 'wb'))
    
    
    if key == 27:
        break
    elif key == ord("d"):
        circles = []

    elif key == ord("q"):
        break
   
cap.release()
cv2.destroyAllWindows()
