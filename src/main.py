from tkinter import *
from tkinter.ttk import *
#import pygame


def GUI():
    # main window named root
    root = Tk()

    # title of "root"
    root.title("Scithon")

    # dimensions of root
    window_height = 720
    window_width = 1080

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # creating a button in the north east of the root
    object_Menu = Button(root, text = "shapes").place(relx = 1, rely = 0, anchor = "ne")

    #* mainloop is used when application is ready to run and tells the code to keep displaying
    root.mainloop()

GUI()



