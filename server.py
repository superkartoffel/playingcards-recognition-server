import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from PIL import Image
import time
import StringIO
import uuid
import numpy
import json
from tornado.options import define, options
import opencv

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
        (r"/", MainHandler),
        (r"/carddetector", CardDetectHandler)
        ]

    settings = dict(
        cookie_secret="asdsafl.rleknknfkjqweonrkbknoijsdfckjnk 234jn",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=False,
        autoescape=None,
        debug=True
        )
    tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("facedetect.html")

class SocketHandler(tornado.websocket.WebSocketHandler):

  def open(self):
    logging.info('new connection')

  def on_message(self, message):
    image = Image.open(StringIO.StringIO(message))
    cv_image = numpy.array(image)
    self.process(cv_image)

  def on_close(self):
    logging.info('connection closed')

  def process(self, cv_image):
    pass

class CardDetectHandler(SocketHandler):

  def process(self, cv_image):
    cards = opencv.detect(cv_image)
    if len(cards) > 0:
      result = json.dumps(cards.tolist())
      self.write_message(result)
    else:
      self.write_message(json.dumps("No cards detected."))

def main():
  tornado.options.parse_command_line()
  app = Application()
  app.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
