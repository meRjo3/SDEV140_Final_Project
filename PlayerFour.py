from tkinter import *
import tkinter.ttk
from PIL import ImageTk, Image

# This module houses some of the tools to play a four player game of Magic The Gathering
# This includes individual total counters for the players, and a list of effects that might occur
# and displays them in a contained frame in the order they would happen.
# With the bottom of the stack happening last and the top of the stack happening first


# This Frame Class is what gets loaded when the four_players button is hit on the StartPage

class FourPlayer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Player 1 Life Total Management, includes the Canvas, labels, buttons, and the functions
        # That manage the Player 1 life total throughout the game

        class Player1:
            def __init__(self):

                # The function that pulls the variable holding the Player 1 life total
                # then increases that variable by 1 and updates the displayp1life label to show the adjusted total

                def player1lifeup():
                    nonlocal player1lifetotal
                    player1lifetotal += 1
                    displayp1life["text"] = player1lifetotal
                    print(player1lifetotal)

                # The function that pulls the variable holding the Player 1 life total
                # then decreases that variable by 1 and updates the displayp1life label to show the adjusted total

                def player1lifedown():
                    nonlocal player1lifetotal
                    player1lifetotal -= 1
                    displayp1life["text"] = player1lifetotal
                    print(player1lifetotal)

                # The player1lifetotal variable here is the starting value when the page gets loaded and get called upon
                # when the player1lifeup and player1lifedown functions commands are used but their respective buttons
                # This is also where the canvas and labels that display the Player1 information lives

                player1lifetotal = 40
                player1canvas = Canvas(bg='red', height=190, width=200)
                player1canvas.place(x=0, y=3)
                player1frame = Label(text="Player One HP", font=('Arial', 18))
                player1frame.place(x=10, y=10)
                displayp1life = Label(text=player1lifetotal, font=('Arial', 20))
                displayp1life.place(x=75, y=50)

                # Player 1 Buttons that call the player1lifeup and player1lifedown functions
                # these adjust this specific player's life total

                p1plusbutton = Button(command=player1lifeup, text="+", height=1, width=1,
                                      font=('Arial', 12), )
                p1plusbutton.place(x=75, y=125)
                p1minusbutton = Button(text="-", height=1, width=1, font=('Arial', 12),
                                       command=player1lifedown)
                p1minusbutton.place(x=95, y=125)

        # Player 2 Life Total Management, includes the Canvas, labels, buttons, and the functions
        # that manage the Player 2 life total throughout the game

        class Player2:
            def __init__(self):

                # The function that pulls the variable holding the Player 2 life total
                # then increases that variable by 1 and updates the displayp2life label to show the adjusted total

                def player2lifeup():
                    nonlocal player2lifetotal
                    player2lifetotal += 1
                    displayp2life["text"] = player2lifetotal
                    print(player2lifetotal)

                # The function that pulls the variable holding the Player 2 life total
                # then decreases that variable by 1 and updates the displayp2life label to show the adjusted total

                def player2lifedown():
                    nonlocal player2lifetotal
                    player2lifetotal -= 1
                    displayp2life["text"] = player2lifetotal
                    print(player2lifetotal)

                # The player1lifetotal here is the starting value when the page gets loaded and get called upon
                # when the player1lifeup and player1lifedown functions commands are used but their respective buttons
                # This is also where the canvas and labels that display the Player1 information lives

                player2lifetotal = 40
                player2canvas = Canvas(bg='blue', height=190, width=200)
                player2canvas.place(x=207, y=3)
                player2frame = Label(text="Player Two HP", font=('Arial', 18))
                player2frame.place(x=225, y=10)
                displayp2life = Label(text=player2lifetotal, font=('Arial', 20))
                displayp2life.place(x=295, y=50)

                # Player 2 Buttons that call the player2lifeup and player2lifedown functions
                # these adjust this specific player's life total

                p2plusbutton = Button(text="+", height=1, width=1, font=('Arial', 12),
                                      command=player2lifeup)
                p2plusbutton.place(x=295, y=125)
                p2minusbutton = Button(text="-", height=1, width=1, font=('Arial', 12),
                                       command=player2lifedown)
                p2minusbutton.place(x=315, y=125)

        # Player 3 Life Total Management, includes the Canvas, labels, buttons, and the functions
        # that manage the Player 3 life total throughout the game

        class Player3:
            def __init__(self):

                # The function that pulls the variable holding the Player 3 life total
                # then increases that variable by 1 and updates the displayp3life label to show the adjusted total

                def player3lifeup():
                    nonlocal player3lifetotal
                    player3lifetotal += 1
                    displayp3life["text"] = player3lifetotal
                    print(player3lifetotal)

                # The function that pulls the variable holding the Player 3 life total
                # then decreases that variable by 3 and updates the displayp1life label to show the adjusted total

                def player3lifedown():
                    nonlocal player3lifetotal
                    player3lifetotal -= 1
                    displayp3life["text"] = player3lifetotal
                    print(player3lifetotal)

                # The player3lifetotal here is the starting value when the page gets loaded and get called upon
                # when the player3lifeup and player3lifedown functions commands are used but their respective buttons
                # This is also where the canvas and labels that display the Player3 information lives

                player3lifetotal = 40
                player3canvas = Canvas(bg='green', height=190, width=200)
                player3canvas.place(x=0, y=200)
                player3frame = Label(text="Player Three HP", font=('Arial', 18))
                player3frame.place(x=10, y=215)
                displayp3life = Label(text=player3lifetotal, font=('Arial', 20))
                displayp3life.place(x=75, y=275)

                # Player 3 Buttons that call the player3lifeup and player3lifedown functions
                # these adjust this specific player's life total

                p3plusbutton = Button(text="+", height=1, width=1, font=('Arial', 12),
                                      command=player3lifeup)
                p3plusbutton.place(x=75, y=350)
                p3minusbutton = Button(text="+", height=1, width=1, font=('Arial', 12),
                                       command=player3lifedown)
                p3minusbutton.place(x=95, y=350)

        # Player 4 Life Total Management, includes the Canvas, labels, buttons, and the functions
        # that manage the Player 4 life total throughout the game

        class Player4:
            def __init__(self):

                # The function that pulls the variable holding the Player 4 life total
                # then increases that variable by 1 and updates the displayp4life label to show the adjusted total

                def player4lifeup():
                    nonlocal player4lifetotal
                    player4lifetotal += 1
                    displayp4life["text"] = player4lifetotal
                    print(player4lifetotal)

                # The function that pulls the variable holding the Player 4 life total
                # then decreases that variable by 4 and updates the displayp1life label to show the adjusted total

                def player4lifedown():
                    nonlocal player4lifetotal
                    player4lifetotal -= 1
                    displayp4life["text"] = player4lifetotal
                    print(player4lifetotal)

                # The player4lifetotal here is the starting value when the page gets loaded and get called upon
                # when the player4lifeup and player4lifedown functions commands are used but their respective buttons
                # This is also where the canvas and labels that display the Player4 information lives

                player4lifetotal = 40
                player4canvas = Canvas(bg='purple', height=190, width=200)
                player4canvas.place(x=207, y=200)
                player4frame = Label(text="Player Four HP", font=('Arial', 18))
                player4frame.place(x=225, y=215)
                displayp4life = Label(text=player4lifetotal, font=('Arial', 20))
                displayp4life.place(x=295, y=275)

                # Player 4 Buttons that call the player4lifeup and player4lifedown functions
                # these adjust this specific player's life total

                p4plusbutton = Button(text="+", height=1, width=1, font=('Arial', 12),
                                      command=player4lifeup)
                p4plusbutton.place(x=295, y=350)
                p4minusbutton = Button(text="-", height=1, width=1, font=('Arial', 12),
                                       command=player4lifedown)
                p4minusbutton.place(x=315, y=350)

        # This function binds a widget to different mouse button events and functions
        # which create a drag and drop feature.
        # Writing the code this way allows me to use this function to make specific widgets draggable by
        # entering the name of the widget between the () like in make_draggable(p1_etb_label)

        def draggable(widget):
            widget.bind("<Button-1>", drag_start)
            widget.bind("<B1-Motion>", drag_motion)

        # This function takes the widget that was bound in the make_draggable
        # and notes the widget's starting x and y coordinates of the widget and where it was clicked.

        def drag_start(event):
            widget = event.widget
            widget.startX = event.x
            widget.startY = event.y

        # This function creates new x and y coordinates for the widget being dragged
        # by comparing the coordinates of the widget and where the mouse button event occurs and where the event ends
        # and the previous x and y coordinate values get replaced in widget.place

        def drag_motion(event):
            widget = event.widget
            x = widget.winfo_x() - widget.startX + event.x
            y = widget.winfo_y() - widget.startY + event.y
            widget.place(x=x, y=y)

        # This function clears all widgets that exist in the Stacksframe

        def clear_frame():
            for widgets in Stacksframe.winfo_children():
                widgets.destroy()

        # This is where a separate window is created and is called by the stackwindow button
        # Holds the comboboxes for different players, image labels representing effects,
        # and a frame where those image labels are packed onto

        def open_four_player_stack_window():
            four_player_stack_window = Toplevel(master)
            four_player_stack_window.title("Stacks")
            four_player_stack_window.geometry("404x445")
            four_player_stack_window.resizable(False, False)
            canvas = Label(four_player_stack_window, bg='black', width=200, height=200)
            canvas.place(x=0, y=0)
            bottom_stack = Label(four_player_stack_window, text="Bottom of the Stack", font=('Arial', 12))
            bottom_stack.place(x=150, y=3)
            top_stack = Label(four_player_stack_window, text="Top of the Stack", font=('Arial', 12))
            top_stack.place(x=150, y=418)

            global Stacksframe
            Stacksframe = LabelFrame(four_player_stack_window, bg='white', width=230, height=385)
            Stacksframe.pack_propagate(False)
            Stacksframe.place(x=150, y=30)

            # A list holding some of the different effects a player can choose from

            effects = [
                "Add/Remove Counters",
                "Copied Spell",
                "Counter Spell",
                "ETB",
                "LTB",
                "Spell Effect",
                "Triggered Ability"
            ]

            # The label representing Player 1 and their ComboBox is found here
            # Set the state of the combobox to readonly so no text can be applied to it

            player1label = Label(four_player_stack_window, bg='white', text="Player 1 Effects", font=('Arial', 10))
            player1label.place(x=3, y=100)
            player1effect = tkinter.ttk.Combobox(four_player_stack_window, state="readonly", values=effects)

            # When the ComboBox has a value selected, this function sees that player1effect has a selection.
            # This effect grabs that selection, checks it against the elif conditions, and calls another function
            # based on which effect value was selected

            def pick_effect(e):
                if player1effect.get() == "ETB":
                    etb_selected()
                elif player1effect.get() == "LTB":
                    ltb_selected()
                elif player1effect.get() == "Counter Spell":
                    counter_spell_selected()
                elif player1effect.get() == "Add/Remove Counters":
                    counters_selected()
                elif player1effect.get() == "Spell Effect":
                    spell_effect_selected()
                elif player1effect.get() == "Copied Spell":
                    copied_spell_selected()
                elif player1effect.get() == "Triggered Ability":
                    trigger_selected()

                # These functions get called by the pick_effect function when it has found which elif is true
                # then it creates and display an image label based on which effect value was selected

            # This function gets when the "ETB" effect value is selected in the ComboBox.
            # It creates and packs the p1_etb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def etb_selected():
                global p1_etb_image
                p1_etb = Image.open('P1_ETB.jpg')
                p1_resize_etb = p1_etb.resize((175, 225))
                p1_etb_image = ImageTk.PhotoImage(p1_resize_etb)
                p1_etb_label = Label(Stacksframe, image=p1_etb_image)
                p1_etb_label.pack()
                draggable(p1_etb_label)

            # This function gets when the "LTB" effect value is selected in the ComboBox.
            # It creates and packs the p1_ltb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def ltb_selected():
                global p1_ltb_image
                p1_ltb = Image.open('P1_LTB.jpg')
                p1_resize_ltb = p1_ltb.resize((175, 225))
                p1_ltb_image = ImageTk.PhotoImage(p1_resize_ltb)
                p1_ltb_label = Label(Stacksframe, image=p1_ltb_image)
                p1_ltb_label.pack()
                draggable(p1_ltb_label)

            # This function gets when the "Counter Spell" effect value is selected in the ComboBox.
            # It creates and packs the p1_cs_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def counter_spell_selected():
                global p1_cs_image
                p1_counter_spell = Image.open('P1_Counter_spell.jpg')
                p1_resize_cs = p1_counter_spell.resize((175, 225))
                p1_cs_image = ImageTk.PhotoImage(p1_resize_cs)
                p1_cs_label = Label(Stacksframe, image=p1_cs_image)
                p1_cs_label.pack()
                draggable(p1_cs_label)

            # This function gets when the "Add/Remove Counters" effect value is selected in the ComboBox.
            # It creates and packs the p1_counters_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def counters_selected():
                global p1_counters_image
                p1_counters = Image.open('P1_Counters.jpg')
                p1_resize_counters = p1_counters.resize((175, 225))
                p1_counters_image = ImageTk.PhotoImage(p1_resize_counters)
                p1_counters_label = Label(Stacksframe, image=p1_counters_image)
                p1_counters_label.pack()
                draggable(p1_counters_label)

            # This function gets when the "Triggered Ability" effect value is selected in the ComboBox.
            # It creates and packs the p1_triggered_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def trigger_selected():
                global p1_triggered_effect_image
                p1_triggered_effect = Image.open('P1_Triggered.jpg')
                p1_resize_triggered_effect = p1_triggered_effect.resize((175, 225))
                p1_triggered_effect_image = ImageTk.PhotoImage(p1_resize_triggered_effect)
                p1_triggered_effect_label = Label(Stacksframe, image=p1_triggered_effect_image)
                p1_triggered_effect_label.pack()
                draggable(p1_triggered_effect_label)

            # This function gets when the "Spell Effect" effect value is selected in the ComboBox.
            # It creates and packs the p1_spell_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def spell_effect_selected():
                global p1_spell_effect_image
                p1_spell_effect = Image.open('P1_Spell_Effect.jpg')
                p1_resize_spell_effect = p1_spell_effect.resize((175, 225))
                p1_spell_effect_image = ImageTk.PhotoImage(p1_resize_spell_effect)
                p1_spell_effect_label = Label(Stacksframe, image=p1_spell_effect_image)
                p1_spell_effect_label.pack()
                draggable(p1_spell_effect_label)

            # This function gets when the "Copied Spell" effect value is selected in the ComboBox.
            # It creates and packs the p1_copied_spell_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def copied_spell_selected():
                global p1_copied_spell_image
                p1_copied_spell = Image.open('P1_copied_spell.jpg')
                p1_resize_copied_spell = p1_copied_spell.resize((175, 225))
                p1_copied_spell_image = ImageTk.PhotoImage(p1_resize_copied_spell)
                p1_copied_spell_label = Label(Stacksframe, image=p1_copied_spell_image)
                p1_copied_spell_label.pack()
                draggable(p1_copied_spell_label)

            # Here is where the Player1 combobox is placed and attaches the pick_effect function to it

            player1effect.bind("<<ComboboxSelected>>", pick_effect)
            player1effect.place(x=3, y=125)

            # The label representing Player 2 and their ComboBox is found here
            # Set the state of the combobox to readonly so no text can be applied to it

            player2label = Label(four_player_stack_window, text="Player 2 Effects", font="Arial, 10")
            player2label.place(x=3, y=150)
            player2effect = tkinter.ttk.Combobox(four_player_stack_window, state="readonly", values=effects)

            # When the ComboBox has a value selected, this function sees that player2effect has a selection.
            # This effect grabs that selection, checks it against the elif conditions, and calls another function
            # based on which effect value was selected

            def pick_effect(e):
                if player2effect.get() == "ETB":
                    p2etb_selected()
                elif player2effect.get() == "LTB":
                    p2ltb_selected()
                elif player2effect.get() == "Counter Spell":
                    p2counter_spell_selected()
                elif player2effect.get() == "Add/Remove Counters":
                    p2counters_selected()
                elif player2effect.get() == "Spell Effect":
                    p2spell_effect_selected()
                elif player2effect.get() == "Copied Spell":
                    p2copied_spell_selected()
                elif player2effect.get() == "Triggered Ability":
                    p2trigger_selected()

                # These functions get called by the pick_effect function when it has found which elif is true
                # then it creates and display an image label based on which effect value was selected

            # This function gets when the "ETB" effect value is selected in the ComboBox.
            # It creates and packs the p2_etb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2etb_selected():
                global p2_etb_image
                p2_etb = Image.open('P2_ETB.jpg')
                p2_resize_etb = p2_etb.resize((175, 225))
                p2_etb_image = ImageTk.PhotoImage(p2_resize_etb)
                p2_etb_label = Label(Stacksframe, image=p2_etb_image)
                p2_etb_label.pack()
                draggable(p2_etb_label)

            # This function gets when the "LTB" effect value is selected in the ComboBox.
            # It creates and packs the p2_ltb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2ltb_selected():
                global p2_ltb_image
                p2_ltb = Image.open('P2_LTB.jpg')
                p2_resize_ltb = p2_ltb.resize((175, 225))
                p2_ltb_image = ImageTk.PhotoImage(p2_resize_ltb)
                p2_ltb_label = Label(Stacksframe, image=p2_ltb_image)
                p2_ltb_label.pack()
                draggable(p2_ltb_label)

            # This function gets when the "Counter Spell" effect value is selected in the ComboBox.
            # It creates and packs the p2_cs_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2counter_spell_selected():
                global p2_cs_image
                p2_counter_spell = Image.open('P2_Counter_spell.jpg')
                p2_resize_cs = p2_counter_spell.resize((175, 225))
                p2_cs_image = ImageTk.PhotoImage(p2_resize_cs)
                p2_cs_label = Label(Stacksframe, image=p2_cs_image)
                p2_cs_label.pack()
                draggable(p2_cs_label)

            # This function gets when the "Add/Remove Counters" effect value is selected in the ComboBox.
            # It creates and packs the p2_counters_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2counters_selected():
                global p2_counters_image
                p2_counters = Image.open('P2_Counters.jpg')
                p2_resize_counters = p2_counters.resize((175, 225))
                p2_counters_image = ImageTk.PhotoImage(p2_resize_counters)
                p2_counters_label = Label(Stacksframe, image=p2_counters_image)
                p2_counters_label.pack()
                draggable(p2_counters_label)

            # This function gets when the "Triggered Ability" effect value is selected in the ComboBox.
            # It creates and packs the p2_triggered_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2trigger_selected():
                global p2_triggered_effect_image
                p2_triggered_effect = Image.open('P2_Triggered.jpg')
                p2_resize_triggered_effect = p2_triggered_effect.resize((175, 225))
                p2_triggered_effect_image = ImageTk.PhotoImage(p2_resize_triggered_effect)
                p2_triggered_effect_label = Label(Stacksframe, image=p2_triggered_effect_image)
                p2_triggered_effect_label.pack()
                draggable(p2_triggered_effect_label)

            # This function gets when the "Spell Effect" effect value is selected in the ComboBox.
            # It creates and packs the p2_spell_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2spell_effect_selected():
                global p2_spell_effect_image
                p2_spell_effect = Image.open('P2_Spell_Effect.jpg')
                p2_resize_spell_effect = p2_spell_effect.resize((175, 225))
                p2_spell_effect_image = ImageTk.PhotoImage(p2_resize_spell_effect)
                p2_spell_effect_label = Label(Stacksframe, image=p2_spell_effect_image)
                p2_spell_effect_label.pack()
                draggable(p2_spell_effect_label)

            # This function gets when the "Copied Spell" effect value is selected in the ComboBox.
            # It creates and packs the p2_copied_spell_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p2copied_spell_selected():
                global p2_copied_spell_image
                p2_copied_spell = Image.open('P2_copied_spell.jpg')
                p2_resize_copied_spell = p2_copied_spell.resize((175, 225))
                p2_copied_spell_image = ImageTk.PhotoImage(p2_resize_copied_spell)
                p2_copied_spell_label = Label(Stacksframe, image=p2_copied_spell_image)
                p2_copied_spell_label.pack()
                draggable(p2_copied_spell_label)

            # Here is where the Player2 combobox is placed and attaches the pick_effect function to it

            player2effect.bind("<<ComboboxSelected>>", pick_effect)
            player2effect.place(x=3, y=175)

            # The label representing Player 3 and their ComboBox is found here
            # Set the state of the combobox to readonly so no text can be applied to it

            player3label = Label(four_player_stack_window, text="Player 3 Effects", font="Arial, 10")
            player3label.place(x=3, y=200)
            player3effect = tkinter.ttk.Combobox(four_player_stack_window, state="readonly", values=effects)

            # When the ComboBox has a value selected, this function sees that player3effect has a selection.
            # This effect grabs that selection, checks it against the elif conditions, and calls another function
            # based on which effect value was selected

            def pick_effect(e):
                if player3effect.get() == "ETB":
                    p3etb_selected()
                elif player3effect.get() == "LTB":
                    p3ltb_selected()
                elif player3effect.get() == "Counter Spell":
                    p3counter_spell_selected()
                elif player3effect.get() == "Add/Remove Counters":
                    p3counters_selected()
                elif player3effect.get() == "Spell Effect":
                    p3spell_effect_selected()
                elif player3effect.get() == "Copied Spell":
                    p3copied_spell_selected()
                elif player3effect.get() == "Triggered Ability":
                    p3trigger_selected()

                # These functions get called by the pick_effect function when it has found which elif is true
                # then it creates and display an image label based on which effect value was selected

            # This function gets when the "ETB" effect value is selected in the ComboBox.
            # It creates and packs the p3_etb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3etb_selected():
                global p3_etb_image
                p3_etb = Image.open('P3_ETB.jpg')
                p3_resize_etb = p3_etb.resize((175, 225))
                p3_etb_image = ImageTk.PhotoImage(p3_resize_etb)
                p3_etb_label = Label(Stacksframe, image=p3_etb_image)
                p3_etb_label.pack()
                draggable(p3_etb_label)

            # This function gets when the "LTB" effect value is selected in the ComboBox.
            # It creates and packs the p3_ltb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3ltb_selected():
                global p3_ltb_image
                p3_ltb = Image.open('P3_LTB.jpg')
                p3_resize_ltb = p3_ltb.resize((175, 225))
                p3_ltb_image = ImageTk.PhotoImage(p3_resize_ltb)
                p3_ltb_label = Label(Stacksframe, image=p3_ltb_image)
                p3_ltb_label.pack()
                draggable(p3_ltb_label)

            # This function gets when the "Counter Spell" effect value is selected in the ComboBox.
            # It creates and packs the p3_cs_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3counter_spell_selected():
                global p3_cs_image
                p3_counter_spell = Image.open('P3_Counter_spell.jpg')
                p3_resize_cs = p3_counter_spell.resize((175, 225))
                p3_cs_image = ImageTk.PhotoImage(p3_resize_cs)
                p3_cs_label = Label(Stacksframe, image=p3_cs_image)
                p3_cs_label.pack()
                draggable(p3_cs_label)

            # This function gets when the "Add/Remove Counters" effect value is selected in the ComboBox.
            # It creates and packs the p3_counters_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3counters_selected():
                global p3_counters_image
                p3_counters = Image.open('P3_Counters.jpg')
                p3_resize_counters = p3_counters.resize((175, 225))
                p3_counters_image = ImageTk.PhotoImage(p3_resize_counters)
                p3_counters_label = Label(Stacksframe, image=p3_counters_image)
                p3_counters_label.pack()
                draggable(p3_counters_label)

            # This function gets when the "Triggered Ability" effect value is selected in the ComboBox.
            # It creates and packs the p3_triggered_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3trigger_selected():
                global p3_triggered_effect_image
                p3_triggered_effect = Image.open('P3_Triggered.jpg')
                p3_resize_triggered_effect = p3_triggered_effect.resize((175, 225))
                p3_triggered_effect_image = ImageTk.PhotoImage(p3_resize_triggered_effect)
                p3_triggered_effect_label = Label(Stacksframe, image=p3_triggered_effect_image)
                p3_triggered_effect_label.pack()
                draggable(p3_triggered_effect_label)

            # This function gets when the "Spell Effect" effect value is selected in the ComboBox.
            # It creates and packs the p3_spell_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3spell_effect_selected():
                global p3_spell_effect_image
                p3_spell_effect = Image.open('P3_Spell_Effect.jpg')
                p3_resize_spell_effect = p3_spell_effect.resize((175, 225))
                p3_spell_effect_image = ImageTk.PhotoImage(p3_resize_spell_effect)
                p3_spell_effect_label = Label(Stacksframe, image=p3_spell_effect_image)
                p3_spell_effect_label.pack()
                draggable(p3_spell_effect_label)

            # This function gets when the "Copied Spell" effect value is selected in the ComboBox.
            # It creates and packs the p3_copied_spell_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p3copied_spell_selected():
                global p3_copied_spell_image
                p3_copied_spell = Image.open('P3_copied_spell.jpg')
                p3_resize_copied_spell = p3_copied_spell.resize((175, 225))
                p3_copied_spell_image = ImageTk.PhotoImage(p3_resize_copied_spell)
                p3_copied_spell_label = Label(Stacksframe, image=p3_copied_spell_image)
                p3_copied_spell_label.pack()
                draggable(p3_copied_spell_label)

            # Here is where the Player3 combobox is placed and attaches the pick_effect function to it

            player3effect.bind("<<ComboboxSelected>>", pick_effect)
            player3effect.place(x=3, y=225)

            # The label representing Player 2 and their ComboBox is found here
            # Set the state of the combobox to readonly so no text can be applied to it

            player4label = Label(four_player_stack_window, text="Player 4 Effects", font="Arial, 10")
            player4label.place(x=3, y=250)
            player4effect = tkinter.ttk.Combobox(four_player_stack_window, state="readonly", values=effects)

            # When the ComboBox has a value selected, this function sees that player4effect has a selection.
            # This effect grabs that selection, checks it against the elif conditions, and calls another function
            # based on which effect value was selected

            def pick_effect(e):
                if player4effect.get() == "ETB":
                    p4etb_selected()
                elif player4effect.get() == "LTB":
                    p4ltb_selected()
                elif player4effect.get() == "Counter Spell":
                    p4counter_spell_selected()
                elif player4effect.get() == "Add/Remove Counters":
                    p4counters_selected()
                elif player4effect.get() == "Spell Effect":
                    p4spell_effect_selected()
                elif player4effect.get() == "Copied Spell":
                    p4copied_spell_selected()
                elif player4effect.get() == "Triggered Ability":
                    p4trigger_selected()

                # These functions get called by the pick_effect function when it has found which elif is true
                # then it creates and display an image label based on which effect value was selected

            # This function gets when the "ETB" effect value is selected in the ComboBox.
            # It creates and packs the p4_etb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4etb_selected():
                global p4_etb_image
                p4_etb = Image.open('P4_ETB.jpg')
                p4_resize_etb = p4_etb.resize((175, 225))
                p4_etb_image = ImageTk.PhotoImage(p4_resize_etb)
                p4_etb_label = Label(Stacksframe, image=p4_etb_image)
                p4_etb_label.pack()
                draggable(p4_etb_label)

            # This function gets when the "LTB" effect value is selected in the ComboBox.
            # It creates and packs the p4_ltb_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4ltb_selected():
                global p4_ltb_image
                p4_ltb = Image.open('P4_LTB.jpg')
                p4_resize_ltb = p4_ltb.resize((175, 225))
                p4_ltb_image = ImageTk.PhotoImage(p4_resize_ltb)
                p4_ltb_label = Label(Stacksframe, image=p4_ltb_image)
                p4_ltb_label.pack()
                draggable(p4_ltb_label)

            # This function gets when the "Counter Spell" effect value is selected in the ComboBox.
            # It creates and packs the p4_cs_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4counter_spell_selected():
                global p4_cs_image
                p4_counter_spell = Image.open('P4_Counter_spell.jpg')
                p4_resize_cs = p4_counter_spell.resize((175, 225))
                p4_cs_image = ImageTk.PhotoImage(p4_resize_cs)
                p4_cs_label = Label(Stacksframe, image=p4_cs_image)
                p4_cs_label.pack()
                draggable(p4_cs_label)

            # This function gets when the "Add/Remove Counters" effect value is selected in the ComboBox.
            # It creates and packs the p4_counters_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4counters_selected():
                global p4_counters_image
                p4_counters = Image.open('P4_Counters.jpg')
                p4_resize_counters = p4_counters.resize((175, 225))
                p4_counters_image = ImageTk.PhotoImage(p4_resize_counters)
                p4_counters_label = Label(Stacksframe, image=p4_counters_image)
                p4_counters_label.pack()
                draggable(p4_counters_label)

            # This function gets when the "Triggered Ability" effect value is selected in the ComboBox.
            # It creates and packs the p4_triggered_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4trigger_selected():
                global p4_triggered_effect_image
                p4_triggered_effect = Image.open('P4_Triggered.jpg')
                p4_resize_triggered_effect = p4_triggered_effect.resize((175, 225))
                p4_triggered_effect_image = ImageTk.PhotoImage(p4_resize_triggered_effect)
                p4_triggered_effect_label = Label(Stacksframe, image=p4_triggered_effect_image)
                p4_triggered_effect_label.pack()
                draggable(p4_triggered_effect_label)

            # This function gets when the "Spell Effect" effect value is selected in the ComboBox.
            # It creates and packs the p4_spell_effect_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4spell_effect_selected():
                global p4_spell_effect_image
                p4_spell_effect = Image.open('P4_Spell_Effect.jpg')
                p3_resize_spell_effect = p4_spell_effect.resize((175, 225))
                p4_spell_effect_image = ImageTk.PhotoImage(p3_resize_spell_effect)
                p4_spell_effect_label = Label(Stacksframe, image=p4_spell_effect_image)
                p4_spell_effect_label.pack()
                draggable(p4_spell_effect_label)

            # This function gets when the "Copied Spell" effect value is selected in the ComboBox.
            # It creates and packs the p4_copied_spell_image widget into the Stacksframe
            # It also tells the draggable function make this widget draggable

            def p4copied_spell_selected():
                global p4_copied_spell_image
                p4_copied_spell = Image.open('P4_copied_spell.jpg')
                p4_resize_copied_spell = p4_copied_spell.resize((175, 225))
                p4_copied_spell_image = ImageTk.PhotoImage(p4_resize_copied_spell)
                p4_copied_spell_label = Label(Stacksframe, image=p4_copied_spell_image)
                p4_copied_spell_label.pack()
                draggable(p4_copied_spell_label)

            # Here is where the Player4 combobox is placed and attaches the pick_effect function to it

            player4effect.bind("<<ComboboxSelected>>", pick_effect)
            player4effect.place(x=3, y=275)

            # This button calls the clear_frame function which destroys all image widgets in the Stacksframe

            clearstack = Button(four_player_stack_window, text="Clear the Stack", font=('Arial', 12),
                                command=clear_frame)
            clearstack.place(x=3, y=3)

        # This class holds the widgets that create the black background
        class background:
            canvas = Label(bg='black', width=200, height=200)
            canvas.place(x=0, y=0)

        class FunctionButtons:
            def __init__(self):

                # This buttons "refreshes" the page by repacking itself
                # Found that this was a simple to reset the player life totals
                # clear all image widgets that might still be on the Stacksframe
                # The switch_frame function for this can be found on the main py file

                new_game = Button(text="New Game", font=('Arial', 12),
                                  command=lambda: master.switch_frame("FourPlayer"))
                new_game.place(x=3, y=400)

                # This button packs the Four Player Frame, loads in new life totals, different numbers of players,
                # and clears any images that might still exist on the Stacksframe
                # The switch_frame function can be found of the main py file

                four_player = Button(text="Two Players", font=('Arial', 12),
                                     command=lambda: master.switch_frame("TwoPlayer"))
                four_player.place(x=98, y=400)

                # This button calls the close function from the main py and closes the application

                game_exit = Button(text="Quit", font=('Arial', 12),
                                   command=lambda: master.close())
                game_exit.place(x=328, y=400)

                # This button calls and create a new window called the Stack Window
                # This is where players can choose from a list of effects which will visually create
                # the stack that is happening in a game

                stack_window = Button(text="Stacks Window", font=('Arial', 12), command=open_four_player_stack_window)
                stack_window.place(x=203, y=400)

        # These call the different classes and displays the in the frame
        FunctionButtons()
        Player1()
        Player2()
        Player3()
        Player4()
        background()
