import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from gpiozero import LED, Button
from signal import pause

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
        if message == "on_b":
            print "blissful blue"

    def on_close(self):
        print "[WS] Connection was closed."

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler),
        ], **settings)


if __name__ == "__main__":
    try:
        app = make_app()
        app.listen(PORT)
        tornado.ioloop.IOLoop.current().start()

    except:
        print "Exception triggered - Tornado Server stopped."

