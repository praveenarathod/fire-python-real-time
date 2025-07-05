import cv2
import pyttsx3
import numpy as np
import imutils
import datetime
from matplotlib import pyplot as plt
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
gun_cascade = cv2.CascadeClassifier('cascade.xml')

firstFrame = None
gun_exist = False
from playsound import playsound
cap = cv2.VideoCapture(0)

engine = pyttsx3.init()

# Set the text to be spoken
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = imutils.resize(frame, width=500)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
    if len(gun) > 0:
        gun_exist = True
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    if firstFrame is None:
        firstFrame = gray
        continue
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)
    if gun_exist:
        print("Humans Voilence detected")
        #plt.imshow(frame)
        text_to_speak = "alert Humans Voilence Possible..."

        # Have the engine say the text
        engine.say(text_to_speak)

        # Run the speech synthesis and wait for it to finish
        engine.runAndWait()

        # Optional: Stop the engine after use (though runAndWait() handles most cases)
        engine.stop()

        break

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("Voilence is detected")
        #playsound('C:/Users/hamed/Desktop/2024/loyola/major projects/fire python/audio.mp3')
        #C:\Users\hamed\Desktop\2024\loyola\major projects\fire python
        text_to_speak = "alert violence detected..."

        # Have the engine say the text
        engine.say(text_to_speak)

        # Run the speech synthesis and wait for it to finish
        engine.runAndWait()

        # Optional: Stop the engine after use (though runAndWait() handles most cases)
        engine.stop()


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
