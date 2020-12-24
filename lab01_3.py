import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

v=343
TRIG=16
E=18

print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
def measure():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    pulse_start = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start
    d = t*v
    d = d/2
    return d*100

def blink():
    for i in xrange(0,5):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.2)

def light():
    GPIO.output(LED_PIN, GPIO.HIGH)

while(1):
    DIST = measure()
    print DIST
    if DIST > 10 and DIST < 20:
        blink()
    else:
        light()
    time.sleep(1)
GPIO.cleanup()
