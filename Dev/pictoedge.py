# pic 2 edgess
# Mike Rosenberg
# Bilbot Project 2014

from SimpleCV import *

display = Display()
img = Image("imagein.png")

while (display.isNotDone()):
	output = img.edges(t1=160)
	output.show()
	output.save("imageout.png")