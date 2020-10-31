#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import cv2
import os

def adicionar_arma(id):
	cam = cv2.VideoCapture(0)
	cam.set(3, 640) # set video width
	cam.set(4, 480) # set video height

	gun_detector = cv2.CascadeClassifier('haarcascade_gun_default.xml')
	print("\n [INFO] inicializando captura de armas. Mostre-a para a câmera e aguarde ...")
	# Initialize individual sampling face count
	count = 0

	while(count < 30):
		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_detector.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
			count += 1
			print ("New photo taken. Total taken is " + str(count))

			# Save the captured image into the datasets folder
			cv2.imwrite("dataset/User." + str(id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

		cv2.imshow('image', img)

		k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			break

	# Do a bit of cleanup
	cam.release()
	cv2.destroyAllWindows()