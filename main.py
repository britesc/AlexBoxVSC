"""
    2 Core Driver.
"""

# Declare Builtins Imports
import machine
from utime import sleep
import _thread
import gc

# Declare 3rd Party Imports


# Declare Application Specific Imports
from lib.version_info import *
# from layouts import class_layout_00 as cl_00
import gui.includes.inc_gui_display

"""
    Priority
    
    10 - Initialise Display
    
"""

"""
    main function only called if we are the primary invocation.
"""

def main() -> None:
    try:
        print(f"Hello from {AppName}-Main! Version: {VersionString}\n")
        
        # Priority 10
        print("main.py - Setting Up Disply\n")
        
        # Priority 38
        print("main.py - Creating Core 1 Thread\n")
        core1_thread = _thread.start_new_thread(core1_thread_actions,())
        print("main.py - Creating Core 0 Thread\n")        
        core0_thread_actions()

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
