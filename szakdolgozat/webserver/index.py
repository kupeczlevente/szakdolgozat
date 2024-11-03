from flask import Flask, Response, redirect, render_template, flash, request, url_for
from picamera2 import Picamera2
import cv2
import threading
from modules import movement

app = Flask(__name__)

moving_forward = False
moving_backward = False
turning_right = False
turning_left = False

# Felbontások wikipédiáról 16:9-es méretarány
resolutions = {
     "600x400": (600, 400),
     "nHD": (640, 360),
     "FWVGA": (854, 480),
     "qHD": (960, 540),
     "WSVGA": (1024, 576),
     "HD": (1280, 720),
     "FWXGA": (1366, 768),
     "HD+": (1600, 900),
     "FullHD": (1920, 1080)

}

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'RGB888', "size": resolutions["600x400"]}))
camera.start()

def frame_gen():
    while True:
            frame = camera.capture_array()
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def move_robot(direction):
    while direction == "forward" and moving_forward:
        movement.walk_forward()
    movement.reset_servos()

    while direction == "backward" and moving_backward:
        movement.walk_backward()
    movement.reset_servos()

    while direction == "right" and turning_right:
        movement.turn_right()
    movement.reset_servos()

    while direction == "left" and turning_left:
        movement.turn_left()
    movement.reset_servos()
    
    return


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/stream')
def stream():
    return Response(frame_gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    



@app.route('/move_forward', methods=['POST'])
def move_forward():
    global moving_forward
    if not moving_forward:
            moving_forward = True
            threading.Thread(target=move_robot, args=("forward",)).start()
    return Response(status=202)

@app.route('/move_backward', methods=['POST'])
def move_backward():
    global moving_backward
    if not moving_backward:
            moving_backward = True
            threading.Thread(target=move_robot, args=("backward",)).start()
    return Response(status=202)

@app.route('/rotate_right', methods=['POST'])
def rotate_right():
    global turning_right
    if not turning_right:
            turning_right = True
            threading.Thread(target=move_robot, args=("right",)).start()
    return Response(status=202)

@app.route('/rotate_left', methods=['POST'])
def rotate_left():
    global turning_left
    if not turning_left:
            turning_left = True
            threading.Thread(target=move_robot, args=("left",)).start()
    return Response(status=202)

@app.route('/stop', methods=['POST'])
def stop():
    global moving_forward, moving_backward, turning_right, turning_left
    moving_forward = False
    moving_backward = False
    turning_right = False
    turning_left = False
    movement.reset_servos()
    return Response(status=200)





#@app.route('/update')
#def update():
#    direction = request.args.get('direction')
#    should_move = request.args.get('should-move') == "true"
#    print("got: " + direction)
#    print("got: ")
#    return Response(status=200)



             

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
