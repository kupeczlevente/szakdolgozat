from flask import Flask, Response, redirect, render_template, flash, request, url_for
import picamera
import cv2
import io

app = Flask(__name__)

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution(640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n'
            stream.seek(0)
            stream.truncate()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/update')
def update():
    direction = request.args.get('direction')
    print(direction)
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
