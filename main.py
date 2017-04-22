from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import RPi.GPIO as GPIO
import json
clients = []

GPIO.setmode(GPIO.BCM)


GPIO.setup([10,9,11,25,8,7],GPIO.OUT)
r1 = GPIO.PWM(10,50)
b1 = GPIO.PWM(9,50)
g1 = GPIO.PWM(11,50)

r2 = GPIO.PWM(7,50)
b2 = GPIO.PWM(8,50)
g2 = GPIO.PWM(25,50)

r1.start(0)
b1.start(0)
g1.start(0)

r2.start(0)
b2.start(0)
g2.start(0)

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        d = self.data
        l = json.loads(d)
        print(int(l[0][0:2],16)/2.55)
        r1.ChangeDutyCycle(int(l[0][0:2],16)/2.55)
        g1.ChangeDutyCycle(int(l[0][2:4],16)/2.55)
        b1.ChangeDutyCycle(int(l[0][4:6],16)/2.55)
        r2.ChangeDutyCycle(int(l[1][0:2],16)/2.55)
        g2.ChangeDutyCycle(int(l[1][2:4],16)/2.55)
        b2.ChangeDutyCycle(int(l[1][4:6],16)/2.55)
        for c in clients:
        	if c != self:
        		c.sendMessage(d)

    def handleConnected(self):
   		clients.append(self)

    def handleClose(self):
    	clients.remove(self)

server = SimpleWebSocketServer('', 4000, SimpleEcho)
server.serveforever()
