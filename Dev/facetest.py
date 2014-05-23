from SimpleCV import *
cam = Camera()
display = Display()

while (display.isNotDone()):
	img = cam.getImage()
	faces = img.findHaarFeatures('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
    	if faces:
        	for face in faces:
            		face.draw()
    	img.show()


