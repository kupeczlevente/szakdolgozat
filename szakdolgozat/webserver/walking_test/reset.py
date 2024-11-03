from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def main():
    for s in range(12):
        kit.servo[s].angle = 90

if __name__ == "__main__":
    main()
