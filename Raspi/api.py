import serial

class bilbot:
	def __init__(self):
		print "You made an object"
		self.ser = serial.Serial("/dev/ttyACM0", 115200)
			

	#Functions for sending data
	# 0 = Not Moving, 1 = Move Forward, 2 = Move Left, 3 = Move Right, 4 = Backwards
	def sendCommand(self,x):
		self.ser.write(str(x))

	def goForward(self):
		self.sendCommand("1*");

	def goBackward(self):
		self.sendCommand("4*");

	def turnRight(self):
		self.sendCommand("3*");

	def turnLeft(self):
		self.sendCommand("2*");

	def allStop(self):
		self.sendCommand("0*");	

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
