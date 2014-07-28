import cv2
import numpy

#Create object to read images from camera 0
cam = cv2.VideoCapture(0)

#Create Mountain Dew Object
mtndew = cv2.imread('mtndew.png')
greydew = cv2.cvtColor(mtndew, cv2.COLOR_BGR2GRAY)

#Initialize SURF object
surf = cv2.SURF(85)

#Set desired radius
rad = 2

#detect points on dew logo
dewpoints, dewscriptors = surf.detectAndCompute(greydew, None, False)

for dp in dewpoints:
        x = int(dp.pt[0])
        y = int(dp.pt[1])
        cv2.circle(mtndew, (x, y), rad, (0, 0, 255))

while True:
    #Get image from webcam and convert to greyscale
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect keypoints and descriptors in greyscale image
	keypoints, descriptors = surf.detectAndCompute(gray, None, False)

    #Draw a small red circle with the desired radius
    #at the (x, y) location for each feature found
#    for kp in keypoints:
 #       x = int(kp.pt[0])
  #      y = int(kp.pt[1])
   #     cv2.circle(img, (x, y), rad, (0, 0, 255))
	rowsize = len(descriptors) / len(keypoints)
	if rowsize > 1:
		hrows = numpy.array(descriptors, dtype = numpy.float32).reshape((-1, rowsize))
		nrows = numpy.array(dewscriptors, dtype = numpy.float32).reshape((-1, rowsize))
		#print hrows.shape, nrows.shape
	else:
		hrows = numpy.array(descriptors, dtype = numpy.float32)
		nrows = numpy.array(dewscriptors, dtype = numpy.float32)
		rowsize = len(hrows[0])

	samples = hrows
	responses = numpy.arange(len(keypoints), dtype = numpy.float32)
	#print len(samples), len(responses)
	knn = cv2.KNearest()
	knn.train(samples,responses)


	for i, descriptor in enumerate(nrows):
    		descriptor = numpy.array(descriptor, dtype = numpy.float32).reshape((1, rowsize))
    		#print i, descriptor.shape, samples[0].shape
    		retval, results, neigh_resp, dists = knn.find_nearest(descriptor, 1)
    		res, dist =  int(results[0][0]), dists[0][0]

	if dist < 0.1:
		color = (0, 0, 255)
        	for xp in dist:
        		x,y = keypoints[res].pt
        		cv2.circle(img, (x, y), rad, (0, 0, 255))
		

    #Display colour image with detected features
	cv2.imshow("DewDetector ocv alpha 3", img)

    #Sleep infinite loop for ~10ms
    #Exit if user presses <Esc>
	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllWindows()
