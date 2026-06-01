from gpiozero import Button, LED
from signal import pause
import os
import threading
import time

POWER_PIN = 3
RESET_PIN = 2
LED_PIN = 14

led = LED(LED_PIN)
power_btn = Button(POWER_PIN, pull_up=True)
reset_btn = Button(RESET_PIN, pull_up=True)

led.on()

def blink_led():
    while True:
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)

def poweroff():
    threading.Thread(target=blink_led, daemon=True).start()
    os.system("sudo shutdown -h now")

def reset():
    os.system("sudo shutdown -r now")

power_btn.when_pressed = poweroff
reset_btn.when_pressed = reset

pause()
