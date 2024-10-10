# Menu screens_1003.py
# Display Screen Test

import random
import gc

import gui.includes.inc_gui_display as gui

""" Create and Show the Random Rectangles Display. """    
def ran_rect():
    # Random rectangles, empty and full.
    gc.enable()
    
    if gui.backlight.value() == False:
        gui.backlight.on()
    
    color = gui.display.color(0,0,0)
    gui.display.fill(color)

    x = 0
    while x < 3:

        full = True
        for i in range(500):
            fill_color = gui.display.color(random.getrandbits(8),
                                       random.getrandbits(8),
                                       random.getrandbits(8))
            gui.display.rect(random.getrandbits(8),
                         random.getrandbits(8),
                         random.getrandbits(6),
                         random.getrandbits(6),
                         fill_color,
                         full)
            full = not full # Switch between full and empty rectangles.
        x += 1
        
        
    color = gui.display.color(0,0,0)
    gui.display.fill(color)    
    gc.collect()    
    gui.backlight.off()    

if __name__ == "__main__":
    ran_rect()