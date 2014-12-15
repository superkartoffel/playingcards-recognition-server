onError = (e) -> console.log "Rejected", e

onSuccess = (localMediaStream) ->
  video.src = webkitURL.createObjectURL(localMediaStream)
  setInterval(update, 250) 

update = -> 
  ctx.drawImage(video, 0, 0, 320, 240)
  canvas.toBlob((blob)-> 
                  ws.send(blob)
                ,'image/jpeg')

video = document.querySelector('video')
canvas = document.querySelector('canvas')
ctx = canvas.getContext('2d')
ctx.strokeStyle = '#ff0'
ctx.lineWidth = 2
text = document.querySelector('#text')
ws = new WebSocket("ws://#{location.host}/carddetector")
ws.onopen = ->  console.log "Opened websocket"
ws.onmessage = (e) ->
  cards = JSON.parse(e.data)
  text.innerHTML = cards

navigator.webkitGetUserMedia({'video': true, 'audio': false}, onSuccess, onError) 
