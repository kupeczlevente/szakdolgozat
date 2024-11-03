import pygame
import time
from adafruit_servokit import ServoKit

# ServoKit konfiguráció
kit = ServoKit(channels=16)
sleep_time = 0.1

# Pygame és kontroller inicializálása
pygame.init()
pygame.joystick.init()

# Feltételezzük, hogy van egy kontroller csatlakoztatva
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Mozgás funkciók (ahogy a meglévő kódodban is)
def walk_forward():
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

def walk_backward():
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
    reset_servos()

def turn_right():
    kit.servo[9].angle = 180
    kit.servo[7].angle = 180
    kit.servo[11].angle = 180
    time.sleep(sleep_time)

    kit.servo[3].angle = 130
    kit.servo[1].angle = 130
    kit.servo[5].angle = 130
    time.sleep(sleep_time)

    kit.servo[9].angle = 90
    kit.servo[7].angle = 90
    kit.servo[11].angle = 90
    time.sleep(sleep_time)

    kit.servo[8].angle = 180
    kit.servo[6].angle = 180
    kit.servo[10].angle = 180
    time.sleep(sleep_time)

    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
    kit.servo[5].angle = 90
    time.sleep(sleep_time)

    kit.servo[2].angle = 130
    kit.servo[0].angle = 130
    kit.servo[4].angle = 130
    time.sleep(sleep_time)

    kit.servo[8].angle = 90
    kit.servo[6].angle = 90
    kit.servo[10].angle = 90
    time.sleep(sleep_time)

    kit.servo[9].angle = 180
    kit.servo[7].angle = 180
    kit.servo[11].angle = 180
    time.sleep(sleep_time)

    kit.servo[2].angle = 90
    kit.servo[0].angle = 90
    kit.servo[4].angle = 90

def turn_left():
    kit.servo[9].angle = 180
    kit.servo[7].angle = 180
    kit.servo[11].angle = 180
    time.sleep(sleep_time)

    kit.servo[3].angle = 50
    kit.servo[1].angle = 50
    kit.servo[5].angle = 50
    time.sleep(sleep_time)

    kit.servo[9].angle = 90
    kit.servo[7].angle = 90
    kit.servo[11].angle = 90
    time.sleep(sleep_time)

    kit.servo[8].angle = 180
    kit.servo[6].angle = 180
    kit.servo[10].angle = 180
    time.sleep(sleep_time)

    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
    kit.servo[5].angle = 90
    time.sleep(sleep_time)

    kit.servo[2].angle = 50
    kit.servo[0].angle = 50
    kit.servo[4].angle = 50
    time.sleep(sleep_time)

    kit.servo[8].angle = 90
    kit.servo[6].angle = 90
    kit.servo[10].angle = 90
    time.sleep(sleep_time)

    kit.servo[9].angle = 180
    kit.servo[7].angle = 180
    kit.servo[11].angle = 180
    time.sleep(sleep_time)

    kit.servo[2].angle = 90
    kit.servo[0].angle = 90
    kit.servo[4].angle = 90

def reset_servos():
    for s in range(12):
        kit.servo[s].angle = 90
    # Folytatás a meglévő kód alapján

# Egyéb mozgás funkciók, mint walk_backward, turn_right, turn_left

# Fő program, ami figyeli a kontroller gombjait
# Fő program, ami figyeli a kontroller gombjait
def main():
    running = True
    while running:
        pygame.event.pump()  # A pygame események frissítése

        # Ha a gombokat megnyomják, a megfelelő mozgás funkciókat hívjuk meg
        if joystick.get_button(2):  # Háromszög gomb
            walk_forward()
            reset_servos()  # Reset a servóknál
        elif joystick.get_button(0):  # X gomb
            walk_backward()
            reset_servos()  # Reset a servóknál
        elif joystick.get_button(1):  # Négyzet gomb
            turn_right()
            reset_servos()  # Reset a servóknál
        elif joystick.get_button(3):  # Kör gomb
            turn_left()
            reset_servos()  # Reset a servóknál

        # Kilépés a programból, ha a "Start" gombot megnyomják (általában 9-es index a PS kontrollereken)
        if joystick.get_button(9):
            running = False

    pygame.quit()


if __name__ == '__main__':
    main()

