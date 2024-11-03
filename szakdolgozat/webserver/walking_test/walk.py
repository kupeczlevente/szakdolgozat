import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
sleep_time = 0.1 #500 milisec

def main():
    reset_servos(12)
#   time.sleep(3) #3 sec
    
    print("forward")
    walk_forward(3)
    reset_servos(12)

    time.sleep(sleep_time*2)

    print("backward")
    walk_backward(3)
    reset_servos(12)

def walk_forward(number_of_walk_cycles):
    for _ in range(number_of_walk_cycles):
        kit.servo[10].angle = 180
        kit.servo[6].angle = 180
        kit.servo[8].angle = 180
        time.sleep(sleep_time)

        kit.servo[4].angle = 130
        kit.servo[0].angle = 50
        kit.servo[2].angle = 50
        time.sleep(sleep_time)

        kit.servo[10].angle = 90
        kit.servo[6].angle = 90
        kit.servo[8].angle = 90
        time.sleep(sleep_time)

        kit.servo[11].angle = 180
        kit.servo[7].angle = 180
        kit.servo[9].angle = 180
        time.sleep(sleep_time)

        kit.servo[4].angle = 90
        kit.servo[0].angle = 90
        kit.servo[2].angle = 90
        time.sleep(sleep_time)

        #---

        kit.servo[5].angle = 130
        kit.servo[1].angle = 50
        kit.servo[3].angle = 130
        time.sleep(sleep_time)

        kit.servo[11].angle = 90
        kit.servo[7].angle = 90
        kit.servo[9].angle = 90
        time.sleep(sleep_time)

        kit.servo[10].angle = 180
        kit.servo[6].angle = 180
        kit.servo[8].angle = 180
        time.sleep(sleep_time)

        kit.servo[5].angle = 90
        kit.servo[1].angle = 90
        kit.servo[3].angle = 90

def walk_backward(number_of_walk_cycles):
    for _ in range(number_of_walk_cycles):
        kit.servo[11].angle = 180
        kit.servo[7].angle = 180
        kit.servo[9].angle = 180
        time.sleep(sleep_time)

        kit.servo[5].angle = 50
        kit.servo[1].angle = 130
        kit.servo[3].angle = 50
        time.sleep(sleep_time)

        kit.servo[11].angle = 90
        kit.servo[7].angle = 90
        kit.servo[9].angle = 90
        time.sleep(sleep_time)

        kit.servo[10].angle = 180
        kit.servo[6].angle = 180
        kit.servo[8].angle = 180
        time.sleep(sleep_time)

        kit.servo[5].angle = 90
        kit.servo[1].angle = 90
        kit.servo[3].angle = 90
        time.sleep(sleep_time)

        #---

        kit.servo[4].angle = 50
        kit.servo[0].angle = 130
        kit.servo[2].angle = 130
        time.sleep(sleep_time)

        kit.servo[10].angle = 90
        kit.servo[6].angle = 90
        kit.servo[8].angle = 90
        time.sleep(sleep_time)

        kit.servo[11].angle = 180
        kit.servo[7].angle = 180
        kit.servo[9].angle = 180
        time.sleep(sleep_time)

        kit.servo[4].angle = 90
        kit.servo[0].angle = 90
        kit.servo[2].angle = 90

def reset_servos(num_of_servos):
    for s in range(num_of_servos):
        kit.servo[s].angle = 90

if __name__ == "__main__":
    main()
