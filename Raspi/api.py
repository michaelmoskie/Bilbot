import serial

class bilbot:
	def __init__(self):
		print "You made an object"
		self.ser = serial.Serial("/dev/ttyACM0", 115200)
			

	#Functions for sending data

	def sendCommand(self,x):
		self.ser.write(str(x))

	def goForward(self):
		self.sendCommand("forward *");

	def goBackward(self):
		self.sendCommand("backward *");

	def turnRight(self):
		self.sendCommand("right *");

	def turnLeft(self):
		self.sendCommand("left *");

	def allStop(self):
		self.sendCommand("allstop *");	

	def digitalWrite(self,pin,state):
		self.sendCommand("dw"+str(pin)+','+str(state)+" *")

	def analogWrite(self,pin,state):
		self.sendCommand("aw"+str(pin)+","+str(state)+" *")
	#Functions for getting data
	def analogRead(self,pin):
		self.sendCommand("aread"+str(pin)+" *")
		return ser.readline()

	def digitalRead(self, pin):
		self.sendCommand("dread"+str(pin)+" *")
		return ser.readline()
