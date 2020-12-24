import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    print("S")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1.5)

    print("O")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1.5)

    print("S")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1.5)

GPIO.cleanup()
