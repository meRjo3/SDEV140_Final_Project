from tkinter import *
# Starting Application window
Four_Player = Tk()


def showstaxs():
    pass


def donothing():
    pass


Four_Player.geometry("404x415")
Four_Player.title("MTG Stacks")
menubar = Menu(Four_Player)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Staxs", command=showstaxs)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Four_Player.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


# Main Header
label = Label(Four_Player, text="MTG Stacks", font=('Arial', 20))
label.place(x=125, y=0)


# Player 1 Life Total Management
class Player1:
    def __init__(self):
        def player1lifeup():
            # Make it do the math!
            nonlocal player1lifetotal
            player1lifetotal += 1
            displayp1life["text"] = player1lifetotal
            print(player1lifetotal)

        def player1lifedown():
            nonlocal player1lifetotal
            player1lifetotal -= 1
            displayp1life["text"] = player1lifetotal
            print(player1lifetotal)

        player1lifetotal = 40
        player1canvas = Canvas(Four_Player, bg='red', height=190, width=200)
        player1canvas.place(x=0, y=30)
        player1frame = Label(Four_Player, text="Player One HP", font=('Arial', 18))
        player1frame.place(x=10, y=40)
        displayp1life = Label(Four_Player, text=player1lifetotal, font=('Arial', 20))
        displayp1life.place(x=75, y=100)

    # Player 1 Buttons
        p1plusbutton = Button(Four_Player, command=player1lifeup, text="+", height=1, width=1, font=('Arial', 12), )
        p1plusbutton.place(x=75, y=150)
        p1minusbutton = Button(Four_Player, text="-", height=1, width=1, font=('Arial', 12), command=player1lifedown)
        p1minusbutton.place(x=95, y=150)


# Player 2 Life Total Management
class Player2:
    def __init__(self):
        def player2lifeup():
            nonlocal player2lifetotal
            player2lifetotal += 1
            displayp2life["text"] = player2lifetotal
            print(player2lifetotal)

        def player2lifedown():
            nonlocal player2lifetotal
            player2lifetotal -= 1
            displayp2life["text"] = player2lifetotal
            print(player2lifetotal)

        player2lifetotal = 40
        player2canvas = Canvas(Four_Player, bg='blue', height=190, width=200)
        player2canvas.place(x=200, y=30)
        player2frame = Label(Four_Player, text="Player Two HP", font=('Arial', 18))
        player2frame.place(x=225, y=40)
        displayp2life = Label(Four_Player, text=player2lifetotal, font=('Arial', 20))
        displayp2life.place(x=295, y=100)

        # Player 2 Buttons
        p2plusbutton = Button(Four_Player, text="+", height=1, width=1, font=('Arial', 12), command=player2lifeup)
        p2plusbutton.place(x=295, y=150)
        p2minusbutton = Button(Four_Player, text="-", height=1, width=1, font=('Arial', 12), command=player2lifedown)
        p2minusbutton.place(x=315, y=150)


# Player 3 Life Total Management
class Player3:
    def __init__(self):
        def player3lifeup():
            nonlocal player3lifetotal
            player3lifetotal += 1
            displayp3life["text"] = player3lifetotal
            print(player3lifetotal)

        def player3lifedown():
            nonlocal player3lifetotal
            player3lifetotal -= 1
            displayp3life["text"] = player3lifetotal
            print(player3lifetotal)

        player3lifetotal = 40
        player3canvas = Canvas(Four_Player, bg='green', height=190, width=198)
        player3canvas.place(x=0, y=222)
        player3frame = Label(Four_Player, text="Player Three HP", font=('Arial', 18))
        player3frame.place(x=10, y=235)
        displayp3life = Label(Four_Player, text=player3lifetotal, font=('Arial', 20))
        displayp3life.place(x=75, y=300)

        # Player 3 Buttons
        p3plusbutton = Button(Four_Player, text="+", height=1, width=1, font=('Arial', 12), command=player3lifeup)
        p3plusbutton.place(x=75, y=350)
        p3minusbutton = Button(Four_Player, text="+", height=1, width=1, font=('Arial', 12), command=player3lifedown)
        p3minusbutton.place(x=95, y=350)


# Player 4 Life Total Management
class Player4:
    def __init__(self):
        def player4lifeup():
            nonlocal player4lifetotal
            player4lifetotal += 1
            displayp4life["text"] = player4lifetotal
            print(player4lifetotal)

        def player4lifedown():
            nonlocal player4lifetotal
            player4lifetotal -= 1
            displayp4life["text"] = player4lifetotal
            print(player4lifetotal)

        player4lifetotal = 40
        player4canvas = Canvas(Four_Player, bg='purple', height=190, width=200)
        player4canvas.place(x=200, y=222)
        player4frame = Label(Four_Player, text="Player Four HP",  font=('Arial', 18))
        player4frame.place(x=225, y=235)
        displayp4life = Label(Four_Player, text=player4lifetotal,  font=('Arial', 20))
        displayp4life.place(x=295, y=300)

        # Player 4 Buttons
        p4plusbutton = Button(Four_Player, text="+", height=1, width=1, font=('Arial', 12), command=player4lifeup)
        p4plusbutton.place(x=295, y=350)
        p4minusbutton = Button(Four_Player, text="-", height=1, width=1, font=('Arial', 12), command=player4lifedown)
        p4minusbutton.place(x=315, y=350)


P1 = Player1()
P2 = Player2()
P3 = Player3()
P4 = Player4()

Four_Player.config(menu=menubar)
Four_Player.mainloop()
