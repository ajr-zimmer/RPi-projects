from gpiozero import LED, Button
from signal import pause

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

#Setup Raspberry Pi Components
redLED = LED(22)
blueLED = LED(17)
button = Button(2)

def reality():
    redLED.on()
    blueLED.off()

def bliss():
    redLED.off()
    blueLED.on()

#Tornado Folder Paths
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    )

#Tornado server port
PORT = 8888

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print "[HTTP](MainHandler) User Connected."
        self.render("index.html")

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "[WS] Connection was opened."

    def on_message(self, message):
        print "[WS] Incoming message:", message
        if message == "on_r":
            print "real red"
            reality()
        if message == "on_b":
            print "blissful blue"
            bliss()

    def on_close(self):
        print "[WS] Connection was closed."

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler),
        ], **settings)


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(make_app())
        http_server.listen(PORT)
        print "Tornado Server started"
        tornado.ioloop.IOLoop.current().start()

    except:
        print "Exception triggered - Tornado Server stopped."
