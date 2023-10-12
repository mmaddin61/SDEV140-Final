"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains the InventoryAdjustmentGUI class that manages the inventory adjustment window.
"""

from tkinter import *
from tkinter import messagebox
from abstract_gui import AbstractGUI
from database import *

# Class for the inventory adjustment window
class InventoryAdjustmentGUI(AbstractGUI):
    # Constructor
    def __init__(self, product):
        AbstractGUI.__init__(self)
        self.product = product
        self.countLabel = Label(self.bodyFrame, text=product.get_count())
        self.adjustEntry = Entry(self.bodyFrame)
        self.buttonFrame = Frame(self.bodyFrame)
        self.addButton = Button(self.buttonFrame, text="Add", command=self.on_add_click)
        self.subtractButton = Button(self.buttonFrame, text="Subtract", command=self.on_subtract_click)
        self.zeroButton = Button(self.buttonFrame, text="Zero Count", command=self.on_zero_click)
        self.closeButton = Button(self.footerFrame, text="Close", command=self.on_close_click)
        
    # Callback for the add button
    def on_add_click(self):
        adjustAmount = 0
        try:
            adjustAmount = int(self.adjustEntry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "You must enter an integer value!")
            return
        if adjustAmount < 1:
            messagebox.showerror("Invalid Input", "You must enter a positive value!")
            return
        newCount = self.product.get_count() + adjustAmount
        database = Database(DB_FILE_NAME)
        self.product.set_count(newCount)
        database.update_count(self.product.get_sku(), newCount)
        self.refresh()
        
    # Callback for the subtract button
    def on_subtract_click(self):
        adjustAmount = 0
        try:
            adjustAmount = int(self.adjustEntry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "You must enter an integer value!")
            return
        if adjustAmount < 1:
            messagebox.showerror("Invalid Input", "You must enter a positive value!")
            return
        newCount = self.product.get_count() - adjustAmount
        if newCount < 0:
            newCount = 0
        self.product.set_count(newCount)
        database = Database(DB_FILE_NAME)
        database.update_count(self.product.get_sku(), newCount)
        self.refresh()
        
    # Callback for the zero count button
    def on_zero_click(self):
        self.product.set_count(0)
        database = Database(DB_FILE_NAME)
        database.update_count(self.product.get_sku(), 0)
        self.refresh()
    
    # Callback for the cancel button
    def on_close_click(self):
        self.close_window()
        
    # Overrides AbstractGUI
    def refresh(self):
        database = Database(DB_FILE_NAME)
        refreshData = database.search_sku(self.product.get_sku())
        self.countLabel.config(text=refreshData.get_count())
        
    # Overrides AbstractGUI
    def show_window(self):
        self.window.title("Inventory Adjustment")
        self.window.geometry("400x200")
        self.window.resizable(False,False)
        
        # Header frame
        self.headerFrame.pack(side=TOP)
        Label(self.headerFrame, text="Inventory Adjustment", font=("TkDefaultFont", 18)).grid(row=0, column=0)
        
        # Body frame
        self.bodyFrame.pack(side=TOP)
        Label(self.bodyFrame, text="On Hand:").grid(sticky="E", row=0, column=0, padx=5)
        self.countLabel.grid(sticky="W", row=0, column=1, padx=5)
        Label(self.bodyFrame, text="Adjust Amount:").grid(row=1, column=0, padx=5)
        self.adjustEntry.grid(row=1, column=1, padx=5, pady=5)
        self.buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)
        self.addButton.grid(row=2, column=0, padx=5)
        self.subtractButton.grid(row=2, column=1, padx=5)
        self.zeroButton.grid(row=2, column=2, padx=5)
        
        # Footer frame
        self.footerFrame.pack(side=BOTTOM, pady=10)
        self.closeButton.pack(side=RIGHT)
        
        self.window.mainloop()
