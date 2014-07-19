from SimpleCV import *
from api import *
import cv2
print SimpleCV.__version__
print cv2.__version__
bilb = bilbot()
cam = Camera()
display = Display()
quality = 400.00
minDist = 0.35
minMatch = 0.2
imgloc = Image("mtndew.png")
square = DrawingLayer((imgloc.width, imgloc.height))
box = (150,150)


while (display.isNotDone()):
	img = cam.getImage()
	keypoints = img.findKeypointMatch(imgloc, quality, minDist, minMatch)
	if keypoints:
		for keypoint in keypoints:
			img = img.applyLayers()
			keypoint.draw(color=Color.BLUE)
		#img = img.drawKeypointMatches(imgloc)
	img.show()   
