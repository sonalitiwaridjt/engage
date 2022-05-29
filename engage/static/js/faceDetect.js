const video = document.getElementById('detectVideo')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri(modelSrc),
  faceapi.nets.faceLandmark68Net.loadFromUri(modelSrc),
  faceapi.nets.faceRecognitionNet.loadFromUri(modelSrc),
  faceapi.nets.faceExpressionNet.loadFromUri(modelSrc),
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    (stream) => (video.srcObject = stream),
    (err) => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  video.parentNode.appendChild(canvas)
  const displaySize = {
    width: video.getBoundingClientRect().width,
    height: video.getBoundingClientRect().height,
  }
  console.log(displaySize)
  faceapi.matchDimensions(canvas, displaySize)
  const si = setInterval(async () => {
    const detections = await faceapi
      .detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceExpressions()
    if (detections.length == 0) {
      return
    }
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    // canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    // faceapi.draw.drawDetections(canvas, resizedDetections)
    // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    console.log(detections[0].expressions)
    expressions = detections[0].expressions
    expression = Object.keys(expressions).reduce((a, b) =>
      expressions[a] > expressions[b] ? a : b
    )
    console.log(expression)
    const newUrl = window.location.href + '?mood=' + expression
    console.log(newUrl)
    window.location.href = newUrl
    clearInterval(si)
  }, 100)
})
