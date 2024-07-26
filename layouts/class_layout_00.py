#!/usr/bin/env python3
# coding: utf-8
# class_layout_00.py :- Show Initial Display
"""
    EARS Layout 00.
    
    This class provides the Initial Display for the EARS application.
    Version: 1.0.0
    Dated: 20240725
    Author: jB
"""
# Declare Builtins Imports
import gc

# Declare 3rd Party Imports
from color_setup import ssd  # Create a display instance
from gui.core.nanogui import refresh
from gui.core.writer import CWriter
from gui.core.colors import *

from gui.widgets.label import Label
import gui.fonts.freesans20 as freesans20

from lib.utilities_filesystem import *

# Define Class
class Ears_LO_00:
# Start Class Intrinsic Functions    
    def __init__(self) -> None:
        """ Class __init__ function. """
        gc.enable()
        self.ClassVersion = "1.0.0"
        self.ClassName    = "Ears_LO_00"
        self.ConfigName   = file_exists("config.json")
        try:
            refresh(ssd)                    # Initialise and clear display.
            CWriter.set_textpos(ssd, 0, 0)  # Set Cursor to top/top
        except OSError:
            # Flash an LED
            pass # TEMPORARY UNTIL WE GET NAVIGATION ON LINE

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
    
# Start Class Extrinsic Functions

    def get_display(self) -> None:
        """
            The Initial Display.
            
            Returns Nothing
        """
        try:
            wri = CWriter(ssd, freesans20, RED, BLACK, verbose=False)
            wri.set_clip(True, True, False)
            Label(wri, 24, 55, 'Equipment & Ammunition')
            Label(wri, 44, 90, 'Reporting System')
            wri = CWriter(ssd, freesans20, GREEN, BLACK, verbose=False)
            Label(wri, 84, 140, 'EARS')
            if not self.ConfigName:
                wri = CWriter(ssd, freesans20, WHITE, BLACK, verbose=False)
                Label(wri, 140, 80, 'NOT CONFIGURED')

            wri = CWriter(ssd, freesans20, BLUE, BLACK, verbose=False)
            Label(wri, 210, 15, 'C JTB 2024 All Rights Reserved')
            refresh(ssd)          
        except OSError:
            # Flash an LED
            pass # TEMPORARY UNTIL WE GET NAVIGATION ON LINE
        finally:
            gc.collect()


if __name__ == "__main__":
    test_of_class = Ears_LO_00()
    print("Class Testing by running directly\n")
    print(f"Class Name             = {test_of_class.getClassName()}\n")    
    print(f"Class Version          = {test_of_class.getClassVersion()}\n")   
    print(f"Show Layout            = Check Display\n")    
    test_of_class.get_display()