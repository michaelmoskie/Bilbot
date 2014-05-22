from SimpleCV import *

cam = Camera()

def halfsies(left,right):
	result = left
	crop = right.crop(right.width/2.0,0,right.width/2.0,right.height)
	result = result.blit(crop,(left.width/2,0))
	return result
	
while True:
	img = cam.getImage()
	output = img.edges(t1=160)	
	result = halfsies(img,output)
	result.show()
