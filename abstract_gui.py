"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains the AbstractGUI class that is inherited by top level GUI classes.
"""

from abc import abstractmethod
from tkinter import *
from tkinter import font

# Abstract class inherited by the program's top level GUIs
class AbstractGUI:   
    # Constructor
    def __init__(self):
        self.window = Toplevel()
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.config(size=12)
        self.headerFrame = Frame(self.window)
        self.bodyFrame = Frame(self.window)
        self.footerFrame = Frame(self.window)
        
    # Function updates the GUI to reflect changes in the database
    @abstractmethod
    def refresh(self):
        pass

    # Function displays the window
    @abstractmethod
    def show_window(self):
        pass
    
    # Function closes the window
    def close_window(self):
        """Closes the window.
        """
        self.window.destroy()
