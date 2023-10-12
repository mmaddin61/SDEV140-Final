"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains the Location class which represents an aisle, bay, and level in
a warehouse.
"""

# Class representing a physical location
class Location:
    # Constructor
    def __init__(self, aisle, bay, level):
        self.aisle = aisle
        self.bay = bay
        self.level = level
        
    # Getters
    def get_aisle(self):
        return self.aisle
    def get_bay(self):
        return self.bay
    def get_level(self):
        return self.level
    
    # Setters
    def set_aisle(self, aisle):
        self.aisle = aisle
    def set_bay(self, bay):
        self.bay = bay
    def set_level(self, row):
        self.level = row




