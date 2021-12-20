from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time 
import cv2
import numpy as np
vs = VideoStream(src = 0).start()

firstFrame = None
min_area = 1000
while True:
	frame = vs.read()
	frame = frame
	text = "Unoccupied"

	if frame is None:
		break

	frame = imutils.resize(frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21,21), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]



	thresh = cv2.dilate(thresh, None, iterations=2) 
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	print(cnts)
	for c in cnts:
		if cv2.contourArea(c) < min_area:
			#text = "No Motion Detected"
			continue

		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
		text = "Motion Detected"

	cv2.putText(frame, "Motion status: {}".format(text), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
	#cv2.putText(frame, dateime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
	#	cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255),1)

	cv2.imshow("Video Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame delta", frameDelta)

	key = cv2.waitKey(1) & 0xFF

	if key == ord('q'):
		break


vs.release()
cv2.destroyAllWindows()


