from SimpleCV import *
from api import *
import cv2
bilb = bilbot()
print "Mountain Dew Detector - ver 0.65"
cam = Camera()
display = Display()
quality = 700.00 #400.00
minDist = 0.35
minDist = 0.35
minMatch = 0.2 #.2
imgloc = Image("mtndew.png")
square = DrawingLayer((imgloc.width, imgloc.height))
box = (150,150)
movement = 0
# 0 = Not Moving, 1 = Move Forward, 2 = Move Left, 3 = Move Right

while (display.isNotDone()):
	img = cam.getImage()
	width = img.width
	divisor = 3
	leftmax = (width/divisor)
	rightmin = width - (width/divisor)	
	keypoints = img.findKeypointMatch(imgloc, quality, minDist, minMatch)
	if keypoints:
		for keypoint in keypoints:
			img = img.applyLayers()
			keypoint.draw(color=Color.BLUE)
			if (keypoint.x > 0 and keypoint.x < leftmax):
				print "Dew is on left"
				movement = 2
				bilb.turnLeft()
			elif (keypoint.x > leftmax and keypoint.x < rightmin):
				print "Dew is in middle"
				movement = 1
				bilb.goForward()
			elif (keypoint.x > rightmin):
				print "Dew is on right"
				movement = 3
				bilb.turnRight()
	else:
		print "No Dew is Present"
		movement = 0
		bilb.turnLeft()
		#BILBOT GOT THE SPINS OH LORDEHHH

	img.show()

del cam	
