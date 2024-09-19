import random
import gc
from machine import Pin, SPI, PWM
from utime import sleep
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
    display.image(5,5,"/images/s/c/ears.565")
#     display.upscaled_text(5,5,'EARS:',ears_color,upscaling=3)
    display.upscaled_text(50,15,title,title_color,upscaling=2)
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
    
""" Display Test Image. """
def test_image():
    color = display.color(0,0,0)
    display.fill(color)
#     display.image(20,20,"/images/lenna.565")
    display.image(20,20,"/images/s/c/ears.565")
    gc.collect()
    backlight.on()
    sleep(5)
    display.image(20,20,"/images/s/c/black-36.565")
    sleep(5)
    backlight.off()
    
""" Animated Ears """
def test_ears():
    color = display.color(0,0,0)
    display.fill(color)
    row = 90
    column = 280
    delay = 0
#     display.image(column,row,"/images/s/c/ears.565")
    backlight.on()
    while column > 50:
        display.image(column,row,"/images/s/c/ears.565")
        display.image(column,row,"/images/s/c/black-36.565")
        column=column-1
    backlight.off()
        
""" Show EARS logo """
def hero_logo():
    display.image(column,row,"/images/s/c/ears.565")
    if backlight.value() == False:
        backlight.on()

""" Draw Box """
def hero_box(title: str):
    color = display.color(0,0,0)
    display.fill(color)
    display.rect(1,1,318,43,display.color(255,255,0),False)
    display.image(3,3,"/images/s/c/ears.565")
    display.upscaled_text(50,15,title,display.color(255,255,0),upscaling=2)
#     display.rect(1,48,318,192,display.color(255,255,0),False)

        
""" Update Main Window """
def display_window():
    display.rect(1,48,318,192,display.color(0,0,0),True )
    display.rect(1,48,318,192,display.color(255,255,0),False)
#     display.image(6,54,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,62,"Take",display.color(255,255,0),upscaling=2)
#     display.image(6,82,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,90,"Your",display.color(255,255,0),upscaling=2)
#     display.image(6,110,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,118,"Clothes",display.color(255,255,0),upscaling=2)
#     display.image(6,138,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,146,"Off",display.color(255,255,0),upscaling=2)
#     display.image(6,166,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,174,"Right",display.color(255,255,0),upscaling=2)
#     display.image(6,194,"/images/n/c/alert-24.565")
#     display.upscaled_text(50,202,"Now!",display.color(255,255,0),upscaling=2)
    if backlight.value() == False:
        backlight.on()
        
""" Update display window line 1 """
def display_window_line_1(icon: str, text: str):
    display.image(6,54,icon)
    display.upscaled_text(50,62,text,display.color(255,255,0),upscaling=2)
    
""" Update display window line 2 """
def display_window_line_2(icon: str, text: str):
    display.image(6,82,icon)
    display.upscaled_text(50,90,text,display.color(255,255,0),upscaling=2)
    
""" Update display window line 3 """
def display_window_line_3(icon: str, text: str):
    display.image(6,110,icon)
    display.upscaled_text(50,118,text,display.color(255,255,0),upscaling=2)
    
""" Display Window Lines """
def display_window_lines(pos: int, icons: list, headings: list):
    icons_column = 6
    headingings_clounm = 50
    column_increment = 28
    list_items = len(headings) # example 5
    max_rows = 5
    rows = 0
    
    if pos < 0:
        pos = 0
    if pos > list_items:
        pos = list_items
     
    for index in range(pos, len(icons)):
        
        row_place1 = 54 + (column_increment * (index - pos))
        display.image(icons_column,row_place1,icons[index])
        row_place2 = 62 + (column_increment * (index - pos))
        display.upscaled_text(headingings_clounm,row_place2, headings[index],display.color(255,255,0),upscaling=2)
        rows = rows + 1
        if rows > max_rows:
            break  
                