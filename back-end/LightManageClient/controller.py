import RPi.GPIO as GPIO
import time
import distance

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3, GPIO.IN)


class Light:
    def __init__(self, gpio1, gpio2):
        self.gpio1 = gpio1
        self.gpio2 = gpio2
        GPIO.setup(gpio1, GPIO.OUT)
        GPIO.setup(gpio2, GPIO.OUT)

    def open(self):
        GPIO.output(self.gpio1, GPIO.HIGH)
        GPIO.output(self.gpio2, GPIO.LOW)

    def close(self):
        GPIO.output(self.gpio1, GPIO.LOW)
        GPIO.output(self.gpio2, GPIO.LOW)


light1 = Light(32, 37)
light2 = Light(35, 33)
light3 = Light(13, 15)
light4 = Light(18, 16)
light5 = Light(3, 5)


def action(cmd):
    if 0 == cmd:
        light1.close()
        light2.close()
        light3.close()
        light4.close()
        light5.close()
    if 1 == cmd:
        light1.open()
        light2.close()
        light3.close()
        light4.close()
        light5.close()
    if 2 == cmd:
        light1.open()
        light2.open()
        light3.close()
        light4.close()
        light5.close()
    if 3 == cmd:
        light1.open()
        light2.open()
        light3.open()
        light4.close()
        light5.close()
    if 4 == cmd:
        light1.open()
        light2.open()
        light3.open()
        light4.open()
        light5.close()
    if 5 == cmd:
        light1.open()
        light2.open()
        light3.open()
        light4.open()
        light5.open()
