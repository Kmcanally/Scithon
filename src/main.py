from tkinter import *
from tkinter.ttk import *
#import pygame


# main window named root
root = Tk()

# setting the dimensions of the window
root.geometry("500x500")

# adding a title to root
root.title("Scithon")

object_Menu = Button(root, text = "shapes").place(relx = 1, rely = 0, anchor = "ne")

#* mainloop is used when application is ready to run and tells the code to keep displaying
root.mainloop()


