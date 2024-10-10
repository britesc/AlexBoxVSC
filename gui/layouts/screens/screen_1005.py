# Menu screens_1005.py
# Display Power / UPS

from machine import RTC
import utime
import gc

import gui.includes.inc_gui_display as gui
from lib.version_info import *

""" Create and Display Internal RTC. """
def display_rtc():
    gc.enable()
    rtc = RTC()
    gui.display_boxes(0,255,255,"c","RTC","clock.565")    

    if gui.backlight.value() == False:
        gui.backlight.on()
        
    while True:
        was = rtc.datetime()        
        year  = was[0]
        mons  = was[1]        
        days  = was[2]
        wday  = was[3]
        hour  = was[4]
        mins  = was[5]
        secs  = was[6]        
        yday  = was[7]
        tday  = EARS['DaysLong'][wday-1][:3]
        tmon  = EARS["MonthsLong"][mons -1][:3]
        OutDDM = f"{tday} {days} {tmon} {year}"        
        gui.display.upscaled_text(50,55, OutDDM,gui.display.color(0,255,255),upscaling=2)
#         year, mons, day, hour, mins, secs, wday, yday
#         print(f"Year  = {was}")
#         print(f"Mons  = {mons} {tmon}")
#         print(f"Days  = {days}")
#         print(f"Wday  = {wday} {tday}")
#         print(f"Hours = {hour}")
#         print(f"Mins  = {mins}")
#         print(f"Secs  = {secs}")
#         print(f"Yday  = {yday}")

        

#         print(OutDDM)
        
        now = rtc.datetime()        
        
        if now[3] != was[3]:
            gui.display.rect(5,55,316,25,gui.display.color(0,0,0),True )
            OutDDM = f"{tday} {days} {tmon} {year}"
            gui.display.upscaled_text(50,55, OutDDM,gui.display.color(0,255,255),upscaling=2)        
        
        if now[6] != was[6]:
            hr = int(now[4])
            hr = '{:02d}'.format(hr)
            mi = int(now[5])
            mi = '{:02d}'.format(mi)
            se = int(now[6])
            se = '{:02d}'.format(se)
            gui.display.rect(5,86,316,25,gui.display.color(0,0,0),True )
            OutHMS = f"{hr}{mi}{se}"
            gui.display.upscaled_text(90,86, OutHMS,gui.display.color(0,255,255),upscaling=3)
        

#     gui.display.upscaled_text(5,86, vol,gui.display.color(0,255,255),upscaling=2)
#     gui.display.upscaled_text(5,117, cur,gui.display.color(0,255,255),upscaling=2)
#     gui.display.upscaled_text(5,148, per,gui.display.color(0,255,255),upscaling=2)
    gc.collect()
    

        
if __name__ == "__main__":
    display_rtc()        