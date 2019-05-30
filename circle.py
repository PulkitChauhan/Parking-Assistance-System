import cv2
import numpy as np
from matplotlib import pyplot as plt
import paho.mqtt.client as mqtt , os
import urllib.parse
import time
import pickle
from imutils.video import VideoStream
import datetime

def on_connect(mosq, obj, rc):
   
    print("" )

def on_message(mosq, obj, msg):
    
    print ("")

def on_publish(mosq, obj, mid):
  
    print ("")

def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(  string)

    
client = mqtt.Client()

client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.on_log = on_log

client.username_pw_set("cpfjxexh", "0R1pH_favGt7")

client.connect('m16.cloudmqtt.com',17887, 60)

client.loop_start()

cascade='cars.xml'

#video_src = 'parkinglot_1_480p.mp4'
cap=cv2.VideoCapture(0)
car_cascade=cv2.CascadeClassifier(cascade)

j=0
i=1
rect=["rect1","rect2","rect3","rect4","rect5"]
circles = pickle.load(open('file.txt', 'rb'))


while True:
    _, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    while(i<5 and j<8):
        for k in range(1):     
            text=i
            rect[i]=cv2.rectangle(frame,circles[j],circles[j+1],(255,0,0),2)
            cv2.putText(frame,"STATUS:{}".format(text),circles[j+1],cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        j+=2
        i+=1
    j=0
    i=1
    
    for (a,b,w,h) in cars:
        cv2.rectangle(frame,(a,b),(a+w,b+h),(0,0,255),2)
        #print(a,b,w,h)
        while(i<5 and j<8):    
            for k in range(1):            
                if circles[j+1][k]<a<circles[j][k]:
                    if circles[j][k+1]<b<circles[j+1][k+1]:
                        status=i
                        cv2.putText(frame,"Park{} occupied".format(status),circles[j],cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
                        
                        client.publish  ( "esp/test", i )
                        time.sleep(0)
            j+=2
            i+=1
                        
    cv2.imshow('frame',frame)
    if cv2.waitKey(33) == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
