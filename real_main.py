"""
    2 Core Driver.
"""

# Declare Builtins Imports
import machine
from utime import sleep
import _thread
import gc

# Declare 3rd Party Imports
from json import class_json_config as jc


# Declare Application Specific Imports
from lib.version_info import *
import gui.includes.inc_gui_display as gui

"""
    Priority
    
    10 - Initialise Display
    
"""

"""
    main function only called if we are the primary invocation.
"""

def main() -> None:
    try:
        print(f"Hello from {EARS["AppName"]}-Main! Version: {EARS["VersionMajor"]}.{EARS["VersionMinor"]}.{EARS["VersionBuild"]}\n")

        # Priority 10
        print("main.py - Setting Up Disply\n")

        # Priority 38
        print("main.py - Creating Core 1 Thread\n")
        core1_thread = _thread.start_new_thread(core1_thread_actions,())
        print("main.py - Creating Core 0 Thread\n")        
        core0_thread_actions()

#         gui.ran_rect()
#        gui.hero_announce()
#         gui.menu_title("First Test")
#         gui.test_image()
#         gui.test_ears()
        gui.hero_box("Main")
        gui.display_window()
        icons_list = ["/images/n/c/return.565","/images/n/c/system.565", "/images/n/c/config.565"]
        headings_list = ["Return","System", "Config"]
        gui.display_window_lines(0, icons_list, headings_list)
        
    except Exception as err:
        print(f"Unfortunately the Application has encountered an error and is unable to continue.\n")
        print(f"Exception {err=}, {type(err)=}\n")
        
"""
    Things that should run using core 0.
"""
def core0_thread_actions() -> None:
    print(f"This is Core 0")
    sleep(0.5)


"""
    Things that should run using core 1.
"""
def core1_thread_actions() -> None:
    print(f"This is Core 1")
    sleep(0.5)
      
    
if __name__ == "__main__":
    main()
