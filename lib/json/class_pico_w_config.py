#!/usr/bin/env python3
# coding: utf-8
# class_pico_w_config.py :- Used Pico W Application Configuration
"""
    EARS Config File.
    
    This class creates and destroys the EARS Configuration File.
    Version: 1.0.0
    Dated: 20240727
    Author: jB
"""

# Declare Builtins Imports
import json

# Declare 3rd Party Imports

# Define Class
class Ears_CONFIG:

# Start Class Intrinsic Functions    
    def __init__(self) -> None:
        """
            Class __init__ function.
        """
        self.ClassVersion = "1.0.0"
        self.ClassName    = "Ears_CONFIG"
        self.config       = None

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

    def getConfigFile(self) -> bool:
        retval=False
        try:
            # load the config file from flash
            with open("config.json") as f:
                self.config = json.load(f)    
            retval=True    
        except Exception:
            retval=False
        finally:
            f.close()
            return retval
        
    def setConfigFile(self) -> bool:
        retval=False
        try:
            # load the config file from flash
            with open("config.json", "w") as f:
                json.dump(self.config, f)
            retval=True   
        except Exception:
            retval=False
        finally:
            f.close()
            return retval

if __name__ == "__main__":
    co = Ears_CONFIG()
    print("Class Testing by running directly\n")
    print(f"Class Name    = {co.getClassName()}\n")
    print(f"Class Version = {co.getClassVersion()}\n")
