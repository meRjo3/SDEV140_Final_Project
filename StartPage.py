from tkinter import *

# This frame is the starting frame that gets loaded when the app launches
# It has some text, an image and two buttons that change frames two either a two or four player game


# This class is the starting page that gets displayed
class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        welcome_text = Label(self, text="Welcome to MTG Stacks," "\n" "How Many Players are in this Game?",
                             font=('Arial', 18), bg='white')
        welcome_text.pack(side="top", fill="x", pady=10)

        # This button switches the current frame to the Two PLayer Game Frame
        # The switch_frame command is found in the main py file
        # This works because the main file import imports the other frame over top itself allowing it to access those
        # frames and widgets. In this case, this frame sits over top the main py file, it sees this button get clicked
        # runs the code. Lambda, holds the command in place until it can see the actual command on the main py file
        two_player = Button(self, text="Two Players", font=('Arial', 12),
                            command=lambda: master.switch_frame("TwoPlayer"))
        two_player.pack()
        # This button switches the current frame to the Four Player game Frame
        # Once again, the switch_frame command in found in the main py file
        four_players = Button(self, text="Four Players", font=('Arial', 12),
                              command=lambda: master.switch_frame("FourPlayer"))
        four_players.pack()

