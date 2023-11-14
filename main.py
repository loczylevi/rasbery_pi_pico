

"""
#blinking tle led wit cycle
from machine import Pin
led = Pin("LED", Pin.OUT)
import time
for szam in range(0,100,1):
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)  # ne felecsd ki ezt a sort te fasz
    
"""

"""

from machine import Pin
led = Pin("LED", Pin.OUT)

led.toggle()   # ki be kacsolja a ledet ha futtatjuk a scriptünket

"""

"""
from machine import Pin, Timer
led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
"""

"""
#blinking tle led wit cycle
from machine import Pin
led = Pin(15, Pin.OUT)
import time
for szam in range(0,100,1):
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)  # ne felecsd ki ezt a sort te fasz
"""
"""
#blinking tle led wit cycle
from machine import Pin

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

import time
while True:
    if button.value():
        led.value(1)
    else:
        led.value(0)
"""


"""
from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15, Pin.OUT))

pwm.freq(1000)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
        
"""

morze = "... --- ..."

from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(15))

buzzer.freq(500)

for elem in morze:
    if elem == ".":
        buzzer.duty_u16(65000)
        sleep(0.1)
        buzzer.duty_u16(0)
        sleep(0.1)
        
    elif elem == "-":
        buzzer.duty_u16(65000)
        sleep(0.3)
        buzzer.duty_u16(0)
        sleep(0.3)
    elif elem == " ":
        sleep(0.2)

