# Dew Detecter version 1.0
# Copyright (C) 2014 Michael Rosenberg
# Developed for the Bilbot Project


from SimpleCV import *
# print SimpleCV.__version__
cam = Camera()
display = Display()
quality = 400.00
minDist = 0.35
minMatch = 0.2
imgloc = Image("mtndewedge.png")

while (display.isNotDone()):
	img = cam.getImage()
	edgy = img.edges(t1=160)	
	keypoints = edgy.findKeypointMatch(imgloc, quality, minDist, minMatch)
	if keypoints:
		for keypoint in keypoints:
			edgy = edgy.applyLayers()
			keypoint.draw(color=Color.BLUE)
	edgy.show()   