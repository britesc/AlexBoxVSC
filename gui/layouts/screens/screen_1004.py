# Menu screens_1004.py
# Display System Info

import os
import gc
import machine
import ubinascii

import gui.includes.inc_gui_display as gui

""" Show System Information. """    
def sys_info():
    gc.enable()
    uname_t = os.uname()
    gui.display_boxes(0,255,255,"c","System Info","system.565")

    res_first, res_second = uname_t[4][:len(uname_t[4])//2+2], uname_t[4][len(uname_t[4])//2+2:] 
 
    gui.display.upscaled_text(28,55, res_first.strip(),gui.display.color(0,255,255),upscaling=2)
    gui.display.upscaled_text(55,83, res_second.strip(),gui.display.color(0,255,255),upscaling=2)
    gui.display.upscaled_text(110,111, uname_t[2].strip(),gui.display.color(0,255,255),upscaling=2)
    gui.display.upscaled_text(55,139, f"Freq {machine.freq() / 1000000} Hz",gui.display.color(0,255,255),upscaling=2)
    
    
    gui.display.upscaled_text(65,173, "Device Ser #",gui.display.color(0,255,255),upscaling=2)
    my_id = ubinascii.hexlify(machine.unique_id()).decode()
    gui.display.upscaled_text(28,201, my_id,gui.display.color(255,0,255),upscaling=2)
       
    gc.collect()
    
if __name__ == "__main__":
    sys_info()
    if gui.backlight.value() == False:
        gui.backlight.on()