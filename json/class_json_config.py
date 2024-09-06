#!/usr/bin/env python3
# coding: utf-8
# class_json_config.py :- Used to Read and Write JSON Config
"""
    EARS JSON Config.
    
    This class Reads aand Wites the JSON Config.
    Version: 1.0.0
    Dated: 20240820
    Author: jB
"""

# Declare Builtins Imports
import ujson
#import uos
import hashlib
import ubinascii

# Declare 3rd Party Imports
from lib import utilities_filesystem as fs
from lib.version_info import *

# Define Class
class Ears_Config:
    
# Start Class Intrinsic Functions    
    def __init__(self) -> None:
        """
            Class __init__ function.
        """
        self.ClassVersion = "1.0.1"
        self.ClassName    = "Ears_Config"
        self.cfdata       = {}
        
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
    def read_json_config(self) -> dict | bool:
        """ Read the full JSON Config File. """
        try:
            """ Check if File Exists """
            if fs.dir_exists("/json"):
                print("Folder Found!")
                """ Check if file exists! """
                if fs.file_exists("/json/config.json"):
                    print("Config File Found!")
                    with open("/json/config.json", "rt") as fp:
                        self.cfdata = ujson.load(fp)
#                         print(self.cfdata)
#                         print(self.cfdata["config"]["user"])
#                         print(self.cfdata["config"]["user"]["version"])
                        value = self.cfdata
                        EARS["CFData"] = self.cfdata
                else:
                    value = False                
            else:
                print("Config Folder Not Found!")
                value = False
        except Exception as err:
            value = False 
        finally:
            return value
        
    def compare_config_versions(self, what: str ) -> int:
        """ Make sure the Config File is Compatible. """
        if what == self.cfdata["config"]["origin"]["version"]:
            print("They are Equal\n")
            return 1
        if what > self.cfdata["config"]["origin"]["version"]:
            print("String is Greater\n")
            return 2
        if what < self.cfdata["config"]["origin"]["version"]:
            print("String is Lesser\n")
            return 3
        return 0
    
    def getOriginUserZap(self)  -> str | bool:
        """ Get the Registered User. """
        if self.cfdata["config"]["origin"]["userzap"]:
            return self.cfdata["config"]["origin"]["userzap"]
        else:
            return False 
            
    def getPasswordHash(self, password: str)  -> str:
        """ Get the Registered User. """
        print(f"Password = {password}\n")
        hash = hashlib.sha1(password)
        return ubinascii.hexlify(hash.digest())
            

if __name__ == "__main__":
    ec = Ears_Config()
    print("Class Testing by running directly\n")
    print(f"Class Name     = {ec.getClassName()}\n")
    print(f"Class Version  = {ec.getClassVersion()}\n")
    print(f"Json File      = {ec.read_json_config()}\n")
    mem_config =  ec.read_json_config()
    print(f"Config Version = {mem_config["config"]["origin"]["version"]}\n")
    print(f"EARS Config Version = {EARS["ConfigVersion"]}\n")
    ev = EARS["ConfigVersion"]
    print(f"Json File Compatibility = {ec.compare_config_versions(ev)}\n")
    print(f"Reg User            = {ec.getOriginUserZap()}\n")
    print(f"Password Hash       = {ec.getPasswordHash("Julian")}\n")
    