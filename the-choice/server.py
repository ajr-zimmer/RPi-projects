from gpiozero import LED, Button
from signal import pause

import os.path
import subprocess
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

#Setup Raspberry Pi Components
redLED = LED(22)
blueLED = LED(17)
button = Button(2)

#Methods responding to what the user has chosen in the browser
def reality():
    redLED.on()
    blueLED.off()

def bliss():
    redLED.off()
    blueLED.on()

#Tornado folder paths
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    )

#Tornado server port
PORT = 8888

#Handler to serve up webpage
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print "[HTTP](MainHandler) User Connected."
        self.render("index.html")

#Handler for receiving the status of whether a pill was picked
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "[WS] Connection was opened."

    def on_message(self, message):
        print "[WS] Incoming message:", message
        if message == "on_r":
            print "You've chosen reality, good luck."
            reality()
        if message == "on_b":
            print "You've chosen blissful ignorance, what a shame."
            bliss()

    def on_close(self):
        print "[WS] Connection was closed."

#Create Tornado app
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler),
        ], **settings)

#Launch app
if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(make_app())
        http_server.listen(PORT)
        print "The Matrix has you..."
        print "Follow the white rabbit."
        #Find RPi IP to display address of Tornado app to user
        host_addr = subprocess.check_output("hostname -I", shell=True).strip()
        print "http://%s:8888/" % host_addr
        tornado.ioloop.IOLoop.current().start()

    except:
        print "Exception triggered - Returning to blissful ignorance..."
