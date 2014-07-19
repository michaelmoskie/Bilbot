import serial

class bilbot:
	def __init__(self):
		print "You made an object"
		ser = serial.Serial("/dev/ttyACM0", 115200)
			

	#Functions for sending data

	def sendCommand(self,x):
		self.ser.write(str(x))

	def goForward(self):
		sendCommand("forward *");

	def goBackward(self):
		sendCommand("backward *");

	def turnRight(self):
		sendCommand("right *");

	def turnLeft(self):
		sendCommand("left *");

	def allStop(self):
		sendCommand("allstop *");	

	def digitalWrite(self,pin,state):
		sendCommand("dw"+str(pin)+','+str(state)+" *")

	def analogWrite(self,pin,state):
		sendCommand("aw"+str(pin)+","+str(state)+" *")
	#Functions for getting data
	def analogRead(self,pin):
		sendCommand("aread"+str(pin)+" *")
		return ser.readline()

	def digitalRead(self, pin):
		sendCommand("dread"+str(pin)+" *")
		return ser.readline()
