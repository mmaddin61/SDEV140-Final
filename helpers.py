"""
Name: Michael Maddin
Class: SDEV140
Program: Final

This module contains misc helper functions.
"""

from tkinter import messagebox

# Function converts a floating-point value to a currency string
def float_to_dollars(value):
    return "$%.2f" % value

# Function displays an error messagebox
def show_error(msg):
    messagebox.showerror("Error", msg)