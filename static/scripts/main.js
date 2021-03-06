// Generated by CoffeeScript 1.8.0
(function() {
  var canvas, ctx, onError, onSuccess, text, update, video, ws;

  onError = function(e) {
    return console.log("Rejected", e);
  };

  onSuccess = function(localMediaStream) {
    video.src = webkitURL.createObjectURL(localMediaStream);
    return setInterval(update, 250);
  };

  update = function() {
    ctx.drawImage(video, 0, 0, 320, 240);
    return canvas.toBlob(function(blob) {
      return ws.send(blob);
    }, 'image/jpeg');
  };

  video = document.querySelector('video');

  canvas = document.querySelector('canvas');

  ctx = canvas.getContext('2d');

  ctx.strokeStyle = '#ff0';

  ctx.lineWidth = 2;

  text = document.querySelector('#text');

  ws = new WebSocket("ws://" + location.host + "/facedetector");

  ws.onopen = function() {
    return console.log("Opened websocket");
  };

  ws.onmessage = function(e) {
    var cards;
    cards = JSON.parse(e.data);
    return text.innerHTML = cards;
  };

  navigator.webkitGetUserMedia({
    'video': true,
    'audio': false
  }, onSuccess, onError);

}).call(this);
