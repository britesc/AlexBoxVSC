import random
import gc
from machine import Pin, SPI, PWM
from time import sleep
from drivers.st7789 import st7789_base, st7789_ext

# LCD Connection to Raspberry Pi Pico W
# Waveshre Pico LCD 2" using ST7789V
# https://www.waveshare.com/wiki/2inch_LCD_Module

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

""" To stop flash of display the Backlight must be turned off before the display is created. """
backlight = Pin(BL,Pin.OUT)
backlight.off()

""" Create the Display. """
display = st7789_ext.ST7789(
    SPI(1, baudrate=40000000, phase=0, polarity=1),
        HEIGHT, WIDTH,
        reset=Pin(RST, Pin.OUT),
        dc=Pin(DC, Pin.OUT),
        cs=Pin(CS, Pin.OUT, value=1),
    )

""" Initialise the Ddisplay. """
display.init(landscape=True,mirror_y=True ,inversion=True)

""" Create and Show the Random Rectangles Display. """    
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

""" Create and Show the Main Menu's Title. """
def menu_title(title: str):
    color = display.color(0,0,0)
    display.fill(color)
    ears_color = display.color(255,255,0)
    title_color = display.color(255,0,0)
    display.upscaled_text(5,5,'EARS:',ears_color,upscaling=3)
    display.upscaled_text(130,15,title,title_color,upscaling=2)
    backlight.on()

""" Create and Show the Main Screen. """
def hero_announce():
    color = display.color(0,0,0)
    display.fill(color)
    display.upscaled_text(85,  25, "Equipment",           display.color(0,255,0),upscaling=2)
    display.upscaled_text(60,  55, "& Ammunition",           display.color(0,255,0),upscaling=2)    
    display.upscaled_text(44, 90, "Reporting System",               display.color(0,255,0),upscaling=2)

    display.upscaled_text(100, 145, "EARS",                          display.color(255,255,0),upscaling=3)
    display.upscaled_text(40, 230, "C JTB 2024 All Rights Reserved",display.color(0,0,255),upscaling=1)    
    gc.collect()
    backlight.on()
    
