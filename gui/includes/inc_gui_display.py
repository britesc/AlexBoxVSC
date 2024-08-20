import random
from machine import Pin, SPI, PWM
from time import sleep
from drivers.st7789 import st7789_base, st7789_ext

# LCD Connection to Raspberry Pi Pico W
# LCD   Pico
#________________________________
# VCC = VSYS
# GND = GND
# DIN = GP11
MOSI  = 11
# CLK = GP10
SCK   = 10
# CS  = GP9
CS    = 9
# DC  = GP8
DC    = 8
# RST = GP12
RST   = 12
# BL  = GP13
BL    = 13

HEIGHT = 320
WIDTH  = 240

display = st7789_ext.ST7789(
    SPI(1, baudrate=40000000, phase=0, polarity=1),
        HEIGHT, WIDTH,
        reset=machine.Pin(RST, machine.Pin.OUT),
        dc=machine.Pin(DC, machine.Pin.OUT),
        cs=machine.Pin(CS, machine.Pin.OUT, value=1),
    )

display.init(landscape=True,mirror_y=True ,inversion=True)
backlight = Pin(BL,Pin.OUT)
backlight.off()
    
def ran_rect():    
    # Random rectangles, empty and full.
    color = display.color(0,0,0)
    display.fill(color)
    backlight.on()

    x = 0
    while x < 3:

        full = True
        for i in range(500):
            fill_color = display.color(random.getrandbits(8),
                                       random.getrandbits(8),
                                       random.getrandbits(8))
            display.rect(random.getrandbits(8),
                         random.getrandbits(8),
                         random.getrandbits(6),
                         random.getrandbits(6),
                         fill_color,
                         full)
            full = not full # Switch between full and empty rectangles.
        x += 1
        
    backlight.off()    

def menu_title(title: str):
    color = display.color(0,0,0)
    display.fill(color)
    ears_color = display.color(255,255,0)
    title_color = display.color(255,0,0)
    display.upscaled_text(5,5,'EARS:',ears_color,upscaling=3)
    display.upscaled_text(130,15,title,title_color,upscaling=2)
    backlight.on()

# ran_rect()

#menu_title("Main Menu")