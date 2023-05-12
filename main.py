from tkinter import *
from PIL import ImageTk, Image
from StartPage import StartPage
from PlayerFour import FourPlayer
from PlayerTwo import TwoPlayer

# This dictionary holds the different pages that can be swapped to in the application
pages = {
    "StartPage": StartPage,
    "TwoPlayer": TwoPlayer,
    "FourPlayer": FourPlayer
}


# This class holds the main screen and function in which the different pages will be placed on top of and loads the
# Start Page which welcomes the user and asks which game mode they would like to use
# being a Two Player or Four Player format
class Stacks(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.switch_frame("StartPage")

# This function is used throughout the different pages and is used from them when the user wishes to
# navigate to different pages. Originally intended to be a drop-down menu, will revisit after this course
    def switch_frame(self, page_name):
        switch = pages[page_name]
        new_frame = switch(self)
        self.frame = new_frame
        self.frame.pack()

    def close(self):
        root.destroy()
        root.quit()


# This is mainloop, holds the size of the window, title, icon image,  and sets the resizeable to false
if __name__ == "__main__":
    root = Stacks()
    root.geometry('413x445')
    root.resizable(False, False)
    root.title("MTG Stacks")
    main_image = Image.open('Mtg_card.png')
    main_image_resize = main_image.resize((175, 225))
    main_image_image = ImageTk.PhotoImage(image=main_image_resize)
    main_image_label = Label(root, image=main_image_image)
    main_image_label.pack()
    root.iconphoto(False, main_image_image)
    root.mainloop()
