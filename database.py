"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module abstracts sqlite3 to help with code organization in other modules.
Parameterized queries are used.
"""

import sqlite3
import helpers
from product import *
from location import *

DB_FILE_NAME = "products_data.db"   # Database file name constant

# Class representing a locally-stored SQLite database
class Database:
    # Constructor
    def __init__(self, dbFile):
        self.dbFile = dbFile    # Name of the database file
        
    # Function searches the database for a product with a matching SKU and returns a new Product instance
    def search_sku(self, sku):
        connection = sqlite3.connect(self.dbFile)   # Connect to database
        cursor = connection.cursor()    # Reference to connection.cursor
        
        # Parameterized query that fetches the product's data as well as the aisle, bay, and level using a join
        query = ("SELECT p.sku, p.name, p.description, p.manufacturer, p.imgName, p.price, p.count, l.aisle, l.bay, l.level "
        "FROM products p "
        "INNER JOIN locations l ON l.locationID = p.locationID "
        "WHERE sku = ?")
        result = cursor.execute(query, (sku,)).fetchall()[0]    # Execute query and get the results as a list
        
        # Create new Location and Product instances using the results from the query
        # If no products matching the SKU were found, result will be empty and an exception will be thrown and is caught by the caller
        location = Location(result[7],
                            result[8],
                            result[9])
        product = Product(result[0],
                          result[1],
                          result[2],
                          result[3],
                          result[4],
                          result[5],
                          result[6],
                          location)
        
        cursor.close()  # Close cursor
        connection.close()  # Close connection
        return product
        
    # Function sets the database's inventory count equal to count
    def update_count(self, sku, count):
        connection = sqlite3.connect(self.dbFile)
        cursor = connection.cursor()
        
        query = ("UPDATE products "
        "SET count = ? "
        "WHERE sku = ? ")
        cursor.execute(query, (count,sku))
        
        connection.commit() # Save changes to database
        cursor.close()
        connection.close()
        