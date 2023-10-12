"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This program is intended to assist warehouse operations personnel with locating products,
viewing product details, and managing inventory counts.
"""

from tkinter import *
from database import *
from product_gui import *
import helpers
    
# Main class for the program
# NOTE: Does not inherit AbstractGUI since this is the root window
class InventoryManager:
    # Constructor
    def __init__(self):
        self.root = Tk()
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.config(size=12)
        self.searchFrame = Frame(self.root)
        self.searchLabel = Label(self.searchFrame, text="Search")
        self.searchEntry = Entry(self.searchFrame, font=("TkDefaultFont", 12))
        self.searchButton = Button(self.searchFrame, text="Search", command=self.on_search_button_click)
        self.footerFrame = Frame(self.root)
        self.exitButton = Button(self.footerFrame, text="Exit", command=self.on_exit_click)
        
    # Callback for the search button
    def on_search_button_click(self):
        searchStr = self.searchEntry.get()
        if len(searchStr) == 0:
            helpers.show_error("Input cannot be empty!")    # Show error if the search entry is empty
            return
        
        database = Database(DB_FILE_NAME)
        try:
            product = database.search_sku(searchStr)    # Lookup product by SKU
            productGui = ProductGUI(product)    # Create the product window
            productGui.show_window()    # Display the product window
        except sqlite3.Error:
            helpers.show_error("An error occurred while reading the database!") # Error message shows if there was an error with sqlite3
            return
        except IndexError:
            helpers.show_error("Could not find product!")   # Error message shows if no records were returned from the database
            return
        
    # Callback for the exit button
    def on_exit_click(self):
        self.root.destroy()
        
    # Program entry
    def run(self):
        self.root.title("Inventory Manager")    # Set window title
        self.root.geometry("300x200")   # Set window size
        self.root.resizable(False,False)    # Disable window resizing
        
        # Search frame
        self.searchFrame.pack(side=TOP)
        Label(self.searchFrame, text="SKU:").grid(sticky="W", row=0, column=0, padx=5)
        self.searchEntry.grid(row=0, column=1, pady=5)
        self.searchButton.grid(row=1, column=0, columnspan=2)
        
        # Footer frame
        self.footerFrame.pack(side=BOTTOM, pady=10)
        self.exitButton.pack(side=BOTTOM)
        
        self.root.mainloop()    # Enter main loop
        
    
if __name__ == "__main__":
    InventoryManager().run()