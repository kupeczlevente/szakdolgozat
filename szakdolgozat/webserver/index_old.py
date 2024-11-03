from flask import Flask, Response, redirect, render_template, flash, request, url_for
import cv2
import numpy as np

app = Flask(__name__)
camera=cv2.VideoCapture(0)

#if not camera.isOpened():
#    print("Nem sikerült megnyitni a kamerát")
#    exit()

camera.set(cv2.CAP_PROP_EXPOSURE, 40)

def generate_frames():
    while True:
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

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
    app.run(host='0.0.0.0', port=5000)
