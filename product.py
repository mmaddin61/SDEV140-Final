"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains the Product class.
"""

from location import *

# Class representing a product
class Product:
    # Constructor
    def __init__(self,
                 sku,
                 name,
                 description,
                 manufacturer,
                 imgName,
                 price,
                 count,
                 location):
        self.sku = sku
        self.name = name
        self.description = description
        self.manufacturer = manufacturer
        self.imgName = imgName
        self.price = price
        self.count = count
        self.location = location
        

    # Getters
    def get_sku(self):
        return self.sku
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_manufacturer(self):
        return self.manufacturer
    def get_img_name(self):
        return self.imgName
    def get_img_path(self):
        return "images/%s" % self.imgName
    def get_price(self):
        return self.price
    def get_count(self):
        return self.count
    def get_location(self):
        return self.location
    
    # Setters
    def set_sku(self, sku):
        self.sku = sku
    def set_name(self, name):
        self.name = name
    def set_description(self, description):
        self.description = description
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def set_img_name(self, imgName):
        self.imgName = imgName
    def set_price(self, price):
        self.price = price
    def set_count(self, count):
        self.count = count
    def set_location(self, location):
        self.location = location
    def set_location(self, aisle, bay, level):
        self.location = Location(aisle, bay, level)
        
    # Function adds count to the inventory count
    def add_units(self, count):
        self.count += count
        
    # Function subtracts count from the inventory count
    def remove_units(self, count):
        self.count -= count
        
    # Function sets inventory count to zero
    def remove_all_units(self):
        self.count = 0
    
