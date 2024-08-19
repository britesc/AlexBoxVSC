#!/usr/bin/env python3
# coding: utf-8
# inc_gui_main.py :- Show Initial Display
"""
    EARS GUI Main.
    
    This class controls the Display for the EARS application.
    Version: 1.0.0
    Dated: 20240816
    Author: jB
"""
# Declare Builtins Imports
import gc
import random
from machine import Pin, SPI, PWM
from time import sleep

# Declare 3rd Party Imports
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

   
def init_display() -> None:
    """ Class __init__ function. """
    gc.enable()
    P_reset         = machine.Pin(RST, machine.Pin.OUT)
    P_dc            = machine.Pin(DC, machine.Pin.OUT)
    P_cs            = machine.Pin(CS, machine.Pin.OUT, value=1)
    backlight     = Pin(BL,Pin.OUT)
        
    display = st7789_ext.ST7789(
            SPI(1, baudrate=40000000, phase=0, polarity=1),
            HEIGHT, WIDTH,
            reset=P_reset,
            dc=P_dc,
            cs=P_cs
        )

    backlight.off()
    display.init(landscape=True,mirror_y=True ,inversion=True)
    gc.collect()
"""
        BLACK = display.color(0,0,0)
        WHITE   = display.color(255,255,255)
        RED   = display.color(255,0,0)
        ORANGE   = display.color(255,128,0)
        LIME   = display.color(0,255,0)
        BLUE   = display.color(0,0,255)
        YELLOW   = display.color(255,255,0)
        CYAN   = display.color(0,255,255)
        MAGENTA   = display.color(255,0,255)
        SILVER   = display.color(192,192,192)
        GRAY   = display.color(128,128,128)
        MAROON   = display.color(128,0,0)
        OLIVE   = display.color(128,128,0)
        GREEN   = display.color(0,128,0)
        PURPLE   = display.color(128,0,128)
        TEAL   = display.color(0,128,128)
        NAVY   = display.color(0,0,128)
"""       


def getClassVersion() -> str:
    """ The Version String of this Class """
    return ClassVersion
    
def getClassName() -> str:
    """ The Name String of this Class """
    return ClassName


# Start Class Extrinsic Functions

def show_random_rectangles(self) -> None:
    """ Random rectangles, empty and full. """
    color = display.color(128,0,128)
    display.fill(color)
    backlight.on()
    x = 0
    while x < 3:
        full = True
        for i in range(500):
            fill_color = display.color(random.getrandbits(8),
                                       random.getrandbits(8),
                                       random.getrandbits(8))
            display.rect(
                    random.getrandbits(8),
                    random.getrandbits(8),
                    random.getrandbits(6),
                    random.getrandbits(6),
                    fill_color,
                    full)
            full = not full # Switch between full and empty rectangles.
        x += 1

        backlight.off()
        
        
def show_random_circles(self) -> None:
    """ Random circles, empty and full. """
    color = display.color(128,0,128)
    display.fill(color)

    backlight.on()
    x = 0
    while x < 2:
        full = True
        for i in range(100):
            fill_color = display.color(random.getrandbits(8),
                                           random.getrandbits(8),
                                           random.getrandbits(8))
            display.circle(
                    random.getrandbits(8),
                    random.getrandbits(8),
                    random.getrandbits(6),
                    fill_color,
                    full)
            full = not full # Switch between full and empty circles.        
        x += 1
        backlight.off()
    

if __name__ == "__main__":
    print(f"Class Name             = {test_of_class.getClassName()}\n")    
    print(f"Class Version          = {test_of_class.getClassVersion()}\n")
    print(f"Display Height         = {get_display_height()}\n")
    print(f"Display Width          = {get_display_width()}\n")
    
   
    print("Display Rectangles\n")
    show_random_rectangles()
    print("Display Cicles\n")
    show_random_circles()
