"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains the ProductGUI class which handles the product details window.
"""

from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from product import Product
from abstract_gui import AbstractGUI
from inventory_adjustment_gui import InventoryAdjustmentGUI
from database import *
import helpers

LIGHT_GRAY = "#c9c9c9"

# Class for the product details window
class ProductGUI(AbstractGUI):
    # Constructor
    def __init__(self, product):
        AbstractGUI.__init__(self)
        self.product = product
        
        self.nameLabel = Label(self.headerFrame, text=product.get_name(), font=("TkDefaultFont", 18))    # Product name
        
        self.locationFrame = LabelFrame(self.headerFrame)   # Location frame
        self.aisleLable = Label(self.locationFrame, text=self.product.get_location().get_aisle(), bg=LIGHT_GRAY)   # Aisle
        self.bayLable = Label(self.locationFrame, text=self.product.get_location().get_bay(), bg=LIGHT_GRAY)   # Bay
        self.levelLable = Label(self.locationFrame, text=self.product.get_location().get_level(), bg=LIGHT_GRAY)   # Level
        
        self.imgFrame = Frame(self.bodyFrame, bg="black")    # Image frame
        self.img = ImageTk.PhotoImage(Image.open(product.get_img_path()).resize((150,150))) # Product image
        self.imgLabel = Label(self.imgFrame, image=self.img)    # Product image label
        
        self.detailsFrame = LabelFrame(self.bodyFrame)    # Product details frame
        self.skuLabel = Label(self.detailsFrame, text=product.get_sku())    # SKU
        self.descriptionLabel = Label(self.detailsFrame, text=product.get_description(), wraplength=200, justify=LEFT)    # Description
        self.manufacturerLabel = Label(self.detailsFrame, text=product.get_manufacturer())  # Manufacturer
        self.priceLabel = Label(self.detailsFrame, text=helpers.float_to_dollars(product.get_price()))  # Price
        
        self.inventoryFrame = LabelFrame(self.detailsFrame) # Inventory frame
        self.countLabel = Label(self.inventoryFrame, text=product.get_count())    # Count
        self.adjustButton = Button(self.inventoryFrame, text="Adjust", command=self.on_adjust_click)    # Adjust button
        
        self.refreshButton = Button(self.footerFrame, text="Refresh", command=self.refresh)
        self.closeButton = Button(self.footerFrame, text="Close", command=self.on_close_click)

    # Callback for the adjust inventory button
    def on_adjust_click(self):
        gui = InventoryAdjustmentGUI(self.product)  # Create inventory adjustment window
        gui.show_window()   # Display inventory adjustment window
        
    # Callback for the close button
    def on_close_click(self):
        self.close_window()
        
    # Overrides AbstractGUI
    def refresh(self):
        database = Database(DB_FILE_NAME)
        refreshedData = database.search_sku(self.product.get_sku()) # Get the product's record
        
        # Copy data
        self.skuLabel.config(text=refreshedData.get_sku())
        self.nameLabel.config(text=refreshedData.get_name())
        self.descriptionLabel.config(text=refreshedData.get_description())
        self.manufacturerLabel.config(text=refreshedData.get_manufacturer())
        self.img = ImageTk.PhotoImage(Image.open(refreshedData.get_img_path()).resize((150,150)))
        self.imgLabel.config(image=self.img)
        self.priceLabel.config(text=helpers.float_to_dollars(refreshedData.get_price()))
        self.countLabel.config(text=refreshedData.get_count())
        self.aisleLable.config(text=refreshedData.get_location().get_aisle())
        self.bayLable.config(text=refreshedData.get_location().get_bay())
        self.levelLable.config(text=refreshedData.get_location().get_level())

    # Overrides AbstractGUI
    def show_window(self):

        # Root Window
        self.window.title("Product Details")  # Set window title
        self.window.option_add("*Font", self.defaultFont) # Change the font
        
        # Header Frame
        self.headerFrame.pack(side=TOP)  # Pack the header frame
        self.nameLabel.grid(row=0, column=1)    # Pack the name label
        
        # Location Frame
        self.locationFrame.grid(row=1, column=1, padx=10, pady=10, ipady=5)
        Label(self.locationFrame, text="Aisle").grid(row=1, column=0, padx=5)   # "Aisle"
        self.aisleLable.grid(row=2, column=0, padx=5)   # Pack the aisle label
        Label(self.locationFrame, text="Bay").grid(row=1, column=1, padx=5) # "Bay"
        self.bayLable.grid(row=2, column=1, padx=5) # Pack the bay label
        Label(self.locationFrame, text="Level").grid(row=1, column=2, padx=5)   # "Level"
        self.levelLable.grid(row=2, column=2, padx=5)   # Pack the level label
        
        # Body Frame
        self.bodyFrame.pack(side=TOP)    
        
        # Image Frame
        self.imgFrame.config(highlightbackground="black")   # Set background to black for border effect
        self.imgFrame.grid(row=0, column=0)   # Pack the image frame
        self.imgLabel.grid(row=1, column=0)  # Pack the image label

        # Details Frame
        self.detailsFrame.grid(row=0, column=1, padx=10, pady=10)
        Label(self.detailsFrame, text="SKU:").grid(sticky="E", row=0, column=0, padx=5, pady=5) # "SKU:"
        self.skuLabel.grid(sticky="W", row=0, column=1) # Place the SKU label
        Label(self.detailsFrame, text="Description:").grid(sticky="E", row=1, column=0, padx=5, pady=5)
        self.descriptionLabel.grid(sticky="W", row=1, column=1)
        Label(self.detailsFrame, text="Manufacturer:").grid(sticky="E", row=2, column=0, padx=5, pady=5)
        self.manufacturerLabel.grid(sticky="W", row=2, column=1)
        Label(self.detailsFrame, text="Price:").grid(sticky="E", row=3, column=0, padx=5, pady=5)   # "Price:"
        self.priceLabel.grid(sticky="W", row=3, column=1)   # Place the price label
        
        # Inventory Frame
        self.inventoryFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipady=5)
        Label(self.inventoryFrame, text="On Hand:").grid(sticky="E", row=1, column=0) # "On Hand:"
        self.countLabel.grid(sticky="W", row=1, column=1)   # Place the count label
        self.adjustButton.grid(row=2, column=0, columnspan=2)
        
        # Footer Frame
        self.footerFrame.pack(side=BOTTOM, pady=10)
        self.refreshButton.grid(row=0, column=0, padx=5)
        self.closeButton.grid(row=0, column=1, padx=5)
        
        self.window.mainloop()