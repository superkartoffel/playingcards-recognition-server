Playing card recognition with webrtc, websockets and opencv
==========================================
This is a webrtc, websockets and opencv experiment based on an experiment during a [athega](http://athega.se) hackday.

How does it work?
-------------------
Frames are captured from the web camera via webrtc and sent to the server over websockets. On the server the frames are processed with opencv and a json response is sent back to the client.

Sample json response:

      {
        "cards": {
          0: {
              "color": "hearts"
              "value": "king"
          }
          1: {
              "color": "spades"
              "value": "ace"
          }
        }
      }

Running it
----------
Make sure the dependencies are met.

* [OpenCV](http://opencv.org) with python bindings (I'm using the trunk version)
* [Tornado](http://www.tornadoweb.org)
* [PIL](http://www.pythonware.com/products/pil/)

Run with `python server.py` and browse to http://localhost:8888 

