import serial

class bilbot:
	def __init__(self):
		print "You made an object"
		self.ser = serial.Serial(0)
		print "I'm using port "+self.ser.portstr
		self.ser.baudrate = 115200
		
		try:
			self.ser.open()
		except Exception, e:
			print "Serial port broken! " + str(e)
			exit()
			

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
