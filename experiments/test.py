import dht, machine, time, random, os
from machine import Pin, SPI
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

display.init(landscape=True,mirror_y=True  ,inversion=False)
backlight = Pin(BL,Pin.OUT)
backlight.on()

color = display.color(0,0,0)
display.fill(color)
color = display.color(0,255,0)

while True:

    upscaled = ["START","TEST","NOW..."]
    for i in range(3):
        display.upscaled_text(20*i,20*i,upscaled[i],display.color(15+80*i,15+80*i,15+80*i),upscaling=3)

    # Write some text.
    x = -15 
    y = 0
    for i in range(20):
        x += 2
        y += 8
        display.text(x,y,'Text drawing,Hello!',display.color(255,255,255),display.color(0,0,0))

    # If the file lenna.565 was lodaded in the device, show
    # it on the screen.
    for i in range(20):
        x = random.getrandbits(6)
        y = random.getrandbits(6)
        display.image(x,y,"/gui/images/lenna.565")
        time.sleep(20)
    # Random points using raw pixels.
    start = time.ticks_ms()
    for i in range(1000):
        x = random.getrandbits(8)
        y = random.getrandbits(8)
        display.pixel(x,y,color)
    elapsed = time.ticks_ms()-start
    print(f"1k pixels in {elapsed} ms")

    # Random rectangles, empty and full.
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
        full = not full # Switch between full and empty circles.

    # Random circles, empty and full.
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

    # Random lines
    display.fill(display.color(0,0,0))
    full = True
    start = time.ticks_ms()
    for i in range(100):
        fill_color = display.color(random.getrandbits(8),
                                   random.getrandbits(8),
                                   random.getrandbits(8))
        display.line(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8),
            fill_color)
    elapsed = time.ticks_ms()-start
    print(f"Milliseconds per random line {elapsed/100} ms")

    # Random triangles
    full = True
    for i in range(100):
        fill_color = display.color(random.getrandbits(8),
                                   random.getrandbits(8),
                                   random.getrandbits(8))
        display.triangle(
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            random.getrandbits(7),
            fill_color, full)
        full = not full # Switch between full and empty triangles.
