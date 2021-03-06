import time
from neopixel import *
import threading
import random
from record import record
from bpm import detect_bpm

# LED strip configuration:
LED_COUNT = 266  # Number of LED pixels.
LED_PIN = 12  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB


def getRandomColor(exceptCol=Color(0, 0, 0)):
    color = Color(255,255,255)
    while True:
        i = random.randint(0, 11)
        if (i == 0):
            color = Color(255, 0, 0)
        elif (i == 1):
            color = Color(255, 150, 0)
        elif (i == 2):
            color = Color(255, 255, 0)
        elif (i == 3):
            color = Color(150, 255, 0)
        elif (i == 4):
            color = Color(0, 255, 0)
        elif (i == 5):
            color = Color(0, 255, 150)
        elif (i == 6):
            color = Color(0, 255, 255)
        elif (i == 7):
            color = Color(0, 150, 255)
        elif (i == 8):
            color = Color(55, 0, 255)
        elif (i == 9):
            color = Color(150, 0, 255)
        elif (i == 10):
            color = Color(255, 0, 255)
        elif (i == 11):
            color = Color(255, 0, 150)
        if (color != exceptCol): break
    return color


def lightBox(strip, color, number):
    if (number == 18):
        for i in range(0, 4):
            strip.setPixelColor(i, color)
        for i in range(81, 87):
            strip.setPixelColor(i, color)
    elif (number == 17):
        for i in range(4, 11):
            strip.setPixelColor(i, color)
        for i in range(73, 80):
            strip.setPixelColor(i, color)
    elif (number == 16):
        for i in range(11, 18):
            strip.setPixelColor(i, color)
        for i in range(67, 73):
            strip.setPixelColor(i, color)
    elif (number == 15):
        for i in range(18, 25):
            strip.setPixelColor(i, color)
        for i in range(59, 66):
            strip.setPixelColor(i, color)
    elif (number == 14):
        for i in range(25, 32):
            strip.setPixelColor(i, color)
        for i in range(53, 59):
            strip.setPixelColor(i, color)
    elif (number == 13):
        for i in range(32, 52):
            strip.setPixelColor(i, color)
    elif (number == 12):
        for i in range(87, 93):
            strip.setPixelColor(i, color)
        for i in range(170, 176):
            strip.setPixelColor(i, color)
    elif (number == 11):
        for i in range(94, 100):
            strip.setPixelColor(i, color)
        for i in range(163, 170):
            strip.setPixelColor(i, color)
    elif (number == 10):
        for i in range(101, 107):
            strip.setPixelColor(i, color)
        for i in range(156, 163):
            strip.setPixelColor(i, color)
    elif (number == 9):
        for i in range(108, 114):
            strip.setPixelColor(i, color)
        for i in range(149, 156):
            strip.setPixelColor(i, color)
    elif (number == 8):
        for i in range(115, 121):
            strip.setPixelColor(i, color)
        for i in range(142, 149):
            strip.setPixelColor(i, color)
    elif (number == 7):
        for i in range(121, 142):
            strip.setPixelColor(i, color)
    elif (number == 6):
        for i in range(177, 183):
            strip.setPixelColor(i, color)
        for i in range(259, 266):
            strip.setPixelColor(i, color)
    elif (number == 5):
        for i in range(183, 190):
            strip.setPixelColor(i, color)
        for i in range(252, 259):
            strip.setPixelColor(i, color)
    elif (number == 4):
        for i in range(190, 197):
            strip.setPixelColor(i, color)
        for i in range(245, 252):
            strip.setPixelColor(i, color)
    elif (number == 3):
        for i in range(197, 204):
            strip.setPixelColor(i, color)
        for i in range(238, 245):
            strip.setPixelColor(i, color)
    elif (number == 2):
        for i in range(204, 211):
            strip.setPixelColor(i, color)
        for i in range(232, 238):
            strip.setPixelColor(i, color)
    elif (number == 1):
        for i in range(212, 231):
            strip.setPixelColor(i, color)
    strip.show()


def clearBox(strip, number):
    lightBox(strip, Color(0, 0, 0), number)


def colorWipe(strip, color, wait_ms=400):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / (1000.0 * strip.numPixels()))


def flashWhite(strip, wait_ms=400):
    for i in range(0, 2):
        if (i == 0):
            color = Color(0, 0, 0)
        elif (i == 1):
            color = Color(255, 255, 255)

        for k in range(strip.numPixels()):
            strip.setPixelColor(k, color)
        strip.show()
        time.sleep(wait_ms / 1000)

def countdown(strip, wait_ms=1000):
    t = threading.current_thread()
    color = Color(255,255,255)
    for j in range(0, 10):
        if j == 9:
            lightBox(strip, color,  13)
            lightBox(strip, color,  14)
            lightBox(strip, color,  15)
            lightBox(strip, color,  9)
            lightBox(strip, color,  3)
            lightBox(strip, color,  2)
            lightBox(strip, color,  1)
            lightBox(strip, color,  7)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  12)
            lightBox(strip, color,  18)

        if j == 8:
            lightBox(strip, color,  13)
            lightBox(strip, color,  14)
            lightBox(strip, color,  15)
            lightBox(strip, color,  9)
            lightBox(strip, color,  3)
            lightBox(strip, color,  2)
            lightBox(strip, color,  1)
            lightBox(strip, color,  7)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  12)
            lightBox(strip, color,  18)
            lightBox(strip, color,  17)
            lightBox(strip, color,  16)

        if j == 7:
            lightBox(strip, color,  13)
            lightBox(strip, color,  3)
            lightBox(strip, color,  2)
            lightBox(strip, color,  1)
            lightBox(strip, color,  7)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)

        if j == 6:
            lightBox(strip, color, 1)
            lightBox(strip, color, 7)
            lightBox(strip, color, 13)
            lightBox(strip, color, 14)
            lightBox(strip, color, 15)
            lightBox(strip, color, 16)
            lightBox(strip, color, 17)
            lightBox(strip, color, 18)
            lightBox(strip, color, 12)
            lightBox(strip, color, 6)
            lightBox(strip, color, 5)
            lightBox(strip, color, 4)
            lightBox(strip, color, 10)

        if j == 5:
            lightBox(strip, color,  1)
            lightBox(strip, color,  7)
            lightBox(strip, color,  13)
            lightBox(strip, color,  14)
            lightBox(strip, color,  15)
            lightBox(strip, color,  9)
            lightBox(strip, color,  3)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  12)
            lightBox(strip, color,  18)
        if j == 4:
            lightBox(strip, color,  1)
            lightBox(strip, color,  2)
            lightBox(strip, color,  3)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  9)
            lightBox(strip, color,  13)
            lightBox(strip, color,  14)
            lightBox(strip, color,  15)

        if j == 3:
            lightBox(strip, color,  1)
            lightBox(strip, color,  2)
            lightBox(strip, color,  3)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  7)
            lightBox(strip, color,  9)
            lightBox(strip, color,  12)
            lightBox(strip, color,  13)
            lightBox(strip, color,  15)
            lightBox(strip, color,  18)


        if j == 2:
            lightBox(strip, color,  13)
            lightBox(strip, color,  7)
            lightBox(strip, color,  1)
            lightBox(strip, color,  2)
            lightBox(strip, color,  3)
            lightBox(strip, color,  9)
            lightBox(strip, color,  15)
            lightBox(strip, color,  16)
            lightBox(strip, color,  17)
            lightBox(strip, color,  18)
            lightBox(strip, color,  12)
            lightBox(strip, color,  6)

        if j == 1:
            lightBox(strip, color,  7)
            lightBox(strip, color,  8)
            lightBox(strip, color,  9)
            lightBox(strip, color,  10)
            lightBox(strip, color,  11)
            lightBox(strip, color,  12)

        if j == 0:
            lightBox(strip, color,  1)
            lightBox(strip, color,  2)
            lightBox(strip, color,  3)
            lightBox(strip, color,  4)
            lightBox(strip, color,  5)
            lightBox(strip, color,  6)
            lightBox(strip, color,  7)
            lightBox(strip, color,  12)
            lightBox(strip, color,  13)
            lightBox(strip, color,  14)
            lightBox(strip, color,  15)
            lightBox(strip, color,  16)
            lightBox(strip, color,  17)
            lightBox(strip, color,  18)
        time.sleep(wait_ms/1000)
        for k in range(strip.numPixels()):
            strip.setPixelColor(k, Color(0,0,0))
        if t.task is not "Countdown":
            break

def rainbowStep(strip, wait_ms=400):
    t = threading.current_thread()
    color = Color(0, 0, 0)
    lastcolor = color
    for i in range(0, 11):
        while color == lastcolor:
            color = getRandomColor(color)
        for k in range(0, strip.numPixels()):
            strip.setPixelColor(k, color)
        strip.show()
        lastcolor = color
        time.sleep(wait_ms / 1000.0)
        if t.task is not "Rainbow_Step":
            break

def stepBoxes(strip, wait_ms=400):
    t = threading.current_thread()
    for j in range(0, 11):
        a = random.randint(1, 19)
        b = random.randint(1, 19)
        c = random.randint(1, 19)
        lightBox(strip, Color(255,255,255), a)
        lightBox(strip, Color(255,255,255), b)
        lightBox(strip, Color(255,255,255), c)
        time.sleep(wait_ms / 1000.0)
        clearBox(strip, a)
        clearBox(strip, b)
        clearBox(strip, c)
        if t.task is not "Rainbow_Step_Boxes":
            break

def rainbowStepBoxes(strip, wait_ms=400):
    t = threading.current_thread()
    for j in range(0, 11):
        a = random.randint(1, 19)
        b = random.randint(1, 19)
        c = random.randint(1, 19)
        lightBox(strip, getRandomColor(), a)
        lightBox(strip, getRandomColor(), b)
        lightBox(strip, getRandomColor(), c)
        time.sleep(wait_ms / 1000.0)
        clearBox(strip, a)
        clearBox(strip, b)
        clearBox(strip, c)
        if t.task is not "Rainbow_Step_Boxes":
            break


def rainbowStepAllBoxes(strip, wait_ms=400):
    t = threading.current_thread()
    for j in range(0, 11):
        a = random.randint(1, 19)
        b = random.randint(1, 19)
        c = random.randint(1, 19)
        lightBox(strip, getRandomColor(), a)
        lightBox(strip, getRandomColor(), b)
        lightBox(strip, getRandomColor(), c)
        time.sleep(wait_ms / 1000.0)
        if t.task is not "Rainbow_Step_All_Boxes":
            break



def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    t = threading.current_thread()
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)
            if t.task is not "Theater_Chase":
                break


def theaterChaseBoxes(strip, color, wait_ms=50, iterations=10):
    t = threading.current_thread()
    for j in range(iterations):
        for q in range(18):
            for i in range(1, 19, 18):
                lightBox(strip, color, i + q)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(1, 19, 18):
                lightBox(strip, 0, i + q)
            if t.task is not "Theater_Chase_Boxes":
                break

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""

    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbowFade(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    t = threading.current_thread()
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)
        if t.task is not "Rainbow_Cycle":
            break


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    t = threading.current_thread()
    for j in range(16):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)
            if t.task is not "Theater_Chase_Rainbow":
                break


def detectBPM():
    t = threading.current_thread()
    while 1:
        wav = record()
        bpm = detect_bpm(wav)
        print("bpm: " + str(bpm))
        t.bpm = int(bpm)
        time.sleep(0.01)

def light():
    t = threading.current_thread()
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    lasttask = "Off"
    t2 = threading.Thread(target=detectBPM, args=())
    t2.daemon = True
    t2.bpm = 120
    t2.start()

    while getattr(t, "do_run", True):
        bpm = t2.bpm
        task = getattr(t, "task")
        sleepTime = 60000.0 / bpm
        if (task == "Rainbow_Fade"):
            rainbowFade(strip, sleepTime / 256)
        if (task == "Off"):
            colorWipe(strip, Color(0, 0, 0))
        if (task == "White"):
            colorWipe(strip, Color(255, 255, 255))
        if (task == "Flash_White"):
            flashWhite(strip, sleepTime)
        if (task == "Rainbow_Cycle"):
            rainbowCycle(strip, sleepTime / 256)
        if (task == "Rainbow_Step"):
            rainbowStep(strip, sleepTime)
        if (task == "Step_Boxes"):
            stepBoxes(strip, sleepTime)
        if (task == "Rainbow_Step_Boxes"):
            rainbowStepBoxes(strip, sleepTime)
        if (task == "Rainbow_Step_All_Boxes"):
            rainbowStepAllBoxes(strip, sleepTime)
        if (task == "Countdown"):
            countdown(strip, sleepTime*2)
        if (task == "Theater_Chase"):
            theaterChase(strip, Color(255, 255, 255), sleepTime / 4, 1)
        if (task == "Theater_Chase_Boxes"):
            theaterChaseBoxes(strip, Color(255, 255, 255), sleepTime / 4, 1)
        if (task == "Theater_Chase_Rainbow"):
            theaterChaseRainbow(strip, sleepTime / 4)
        if "RGB" in task:
            rgb = task.replace("RGB", "").split(",")
            colorWipe(strip, Color(int(rgb[0]), int(rgb[1]), int(rgb[2])))
        if "BOX" in task:
            rgbB = task.replace("BOX", "").split(",")
            lightBox(strip, Color(int(rgbB[0]), int(rgbB[1]), int(rgbB[2])), int(rgbB[3]))

        lasttask = task
        time.sleep(0.01)
    print ("stopped")

