#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import cv2
import numpy as np
#from PIL import Image
import os

def treinar_reconhecimento_armas():
	# Path for gun image database
	path = 'dataset'
    #recognizer = cv2.face.LBPHFaceRecognizer_create() 
	detector = cv2.CascadeClassifier("cascade_armas.xml");

	# function to get the images and label data
	def getImagesAndLabels(path):
		imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
		gunSamples = []
		ids = []
		for imagePath in imagePaths:
			#PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
			#img_numpy = np.array(PIL_img,'uint8')
			id = int(os.path.split(imagePath)[-1].split(".")[1])
			armas = detector.detectMultiScale(img_numpy)
			for (x,y,w,h) in armas:
				gunSamples.append(img_numpy[y:y+h,x:x+w])
				ids.append(id)
		return gunSamples,ids

	armas,ids = getImagesAndLabels(path)
	#recognizer.train(armas, np.array(ids))

	# Save the model into trainer/trainer.yml
	#recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

	# Print the numer of faces trained and end program
	print("\n [INFO] {0} Armas treinadas.".format(len(np.unique(ids))))