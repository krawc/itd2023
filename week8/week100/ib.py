import board
import digitalio
import time
import p9813

# Button
sensor1 = digitalio.DigitalInOut(board.D2)
sensor3 = digitalio.DigitalInOut(board.D4)

sensor1.direction = digitalio.Direction.INPUT
sensor3.direction = digitalio.Direction.OUTPUT

shot = False  # set the default value of "shot" to False
experienceStart = True

mode = 'led'

# --- Variables
pin_clk = board.D13
pin_data = board.D10


num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

delta = 5

# --- Functions

# --- Setup
leds.reset()

while True:
    print(sensor1.value)
    time.sleep(0.1)
    #print(sensor2.value)
    if (sensor1.value == True):
        if (mode == 'led'):
                print("Fading in...")
                for intensity in range(0, 255, delta):
                    leds.fill((0, 0, intensity))
                    leds.write()
                    time.sleep(0.05)

                print("Fading out...")
                for intensity in range(255, 0, -delta):
                    leds.fill((0, 0, intensity))
                    leds.write()
                    time.sleep(0.04)
        elif (mode == 'vib'):
            print("Fading in...")
            for intensity in range(0, 255, delta):
                sensor3.value = True
                time.sleep(0.05)
            print("Fading out...")
            for intensity in range(0, 255, delta):
                sensor3.value = False
                time.sleep(0.05)
        elif (mode == 'sound'):
            