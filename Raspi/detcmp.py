import cv2
import numpy
#Create object to read images from camera 0
cam = cv2.VideoCapture(0)
mtndew = cv2.imread('mtndew.png')

#Initialize SURF object
surf = cv2.SURF(85)

#Set desired radius for drawing
rad = 1

#Dew to gray dew to find keypoints
graydew = cv2.cvtColor(mtndew, cv2.COLOR_BGR2GRAY)
dewpoints, dewscriptors = surf.detectAndCompute(graydew, None, False)

#Drawing keypoints on the dew picture
for dp in dewpoints:
	dx = int(dp.pt[0])
	dy = int(dp.pt[1])
	cv2.circle(mtndew, (dx, dy), rad, (0, 0, 255))

while True:
	#Get image from webcam and convert to greyscale
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	#Detect keypoints and descriptors in greyscale camera image
	keypoints, descriptors = surf.detectAndCompute(gray, None, False)

	#K NEAREST NUMBERS ARE YUCKY
	rowsize = len(descriptors) / len(keypoints)
	if rowsize > 1:
		rows = numpy.array(descriptors, dtype = numpy.float32).reshape((-1, rowsize))
		drows = numpy.array(dewscriptors, dtype = numpy.float32).reshape((-1, rowsize))
	else:
		rows = numpy.array(descriptors, dtype = numpy.float32)
		drows = numpy.array(dewscriptors, dtype = numpy.float32)
		rowsize = len(rows[0])
	samples = rows
	responses = numpy.arange(len(keypoints), dtype = numpy.float32)
	knn = cv2.KNearest()
	knn.train(samples,responses)
	
	#We're going the Distance...
	for i, descriptor in enumerate(drows):
		descriptor = numpy.array(descriptor, dtype = numpy.float32).reshape((1, rowsize))
		retval, results, neigh_resp, dists = knn.find_nearest(descriptor, 1)
		res, dist =  int(results[0][0]), dists[0][0]

	#If dew found color them dew area
	color = (0, 0, 255)
	for kp in keypoints:
		if dist < 0.27:
			x = int(kp.pt[0])
			y = int(kp.pt[1])
			#color = (0, 0, 255)
			cv2.circle(img, (x, y), rad, color)
			print "Dew Found"
		else:
			print "Dew Not Found"
	
	#Display colour image with detected features
	cv2.imshow("features", img)
	cv2.imshow("dew", mtndew)
	#Exit if user presses <Esc>
	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllWindows()
