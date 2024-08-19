#!/usr/bin/env python3
# coding: utf-8
# class_gui_main.py :- Show Initial Display
"""
    EARS Display Main.
    
    This class provides the Display for the EARS application.
    Version: 1.0.0
    Dated: 20240818
    Author: jB
"""
# Declare Builtins Imports
import gc
from machine import Pin, SPI, PWM
import random

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


# Define Class
class Ears_GUI_Main:
# Start Class Intrinsic Functions    
    def __init__(self) -> None:
        """ Class __init__ function. """
        gc.enable()
        self.ClassVersion = "1.0.0"
        self.ClassName    = "Ears_GUI_Main"
        self.reset         = machine.Pin(RST, machine.Pin.OUT)
        self.dc            = machine.Pin(DC, machine.Pin.OUT)
        self.cs            = machine.Pin(CS, machine.Pin.OUT, value=1)
        backlight          = Pin(BL,Pin.OUT)
        
        display = st7789_ext.ST7789(
            SPI(1, baudrate=40000000, phase=0, polarity=1),
            HEIGHT, WIDTH,
            reset=self.reset,
            dc=self.dc,
            cs=self.cs
        )

#         backlight.on()
        display.init(landscape=True,mirror_y=True ,inversion=True)
        print(f"Class Display          = {display}\n")
        self.display = display
#         gc.collect()
        
        # Random rectangles, empty and full.
        color = display.color(0,0,0)
        display.fill(color)
        backlight.on()
        
        x = 0
        while x < 3:
            print(f"In while Loop {x}\n")
            full = True
            for i in range(500):
                print(f"In for Loop {i}\n")
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
#         backlight.off()        

    def __str__(self) -> str:
        """ The __str__ Function """
        return self.ClassName

    def __repr__(self) -> str:
        
        """ The __repr__ Function """
        return self.ClassName

    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion
    
    def getClassName(self) -> str:
        """ The Name String of this Class """
        return self.ClassName
    
    # Start Class Specific Functions
    def __getDisplay(self) -> str:
        """ The Display Class """
        return self.display
    
    

if __name__ == "__main__":
    test_of_class = Ears_GUI_Main()
    print("Class Testing by running directly\n")
    print(f"Class Name             = {test_of_class.getClassName()}\n")    
    print(f"Class Version          = {test_of_class.getClassVersion()}\n")
    print(f"Class Dir()            = {dir()}\n")
    print(f"Class Globals()        = {globals()}\n")
    print(f"Class Localss()        = {locals()}\n")
    print(f"Class Display          = {test_of_class.__getDisplay()}\n")