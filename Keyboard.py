from tkinter import messagebox
import tkinter as tk

# Create the main window and frames
root = tk.Tk()
root.title("Keyboard")
display_frame = tk.Frame(root)
keyboard_frame = tk.Frame(root)

# Create a Text widget to display the input text
input_text = tk.Text(display_frame, height=5, width=40)
input_text.pack()

# Create a function to update the input text
def update_input_text(new_text):
    input_text.insert(tk.END, new_text)

# Create a function to delete the last character from the input text
def delete_last_character():
    input_text.delete("end-2c")

# Create a variable to keep track of whether the up arrow button is pressed or not
is_uppercase = False

# Create a function to change the state of the up arrow button and the case of the text when the button is clicked
def toggle_uppercase():
    global is_uppercase
    is_uppercase = not is_uppercase
    if is_uppercase:
        up_arrow_button.config(relief=tk.SUNKEN, bg="green")
    else:
        up_arrow_button.config(relief=tk.RAISED, bg="lightgray")

# Create a function to display the button pressed
def display_input(button_text):
    global is_uppercase
    if button_text == "Space":
        update_input_text(" ")
    elif is_uppercase:
        update_input_text(button_text.upper())
    else:
        update_input_text(button_text.lower())

# Create a list of button names that should have a pink color
pink_buttons = ["Space", "Tab", "Caps", "Shift", "Ctrl", "Alt", "Delete"]

# Create a function to create the keyboard buttons
def create_button(button_text, row_num, col_num, width=5, command=None):
    if command is None:
        command = lambda: display_input(button_text)
    if button_text in pink_buttons:
        button_color = "pink"
    elif button_text.isalpha():
        button_color = "lightblue"
    else:
        button_color = "lightgray"
    button = tk.Button(keyboard_frame, text=button_text, width=width, height=2, command=command, bg=button_color)
    button.grid(row=row_num, column=col_num)

# Create the buttons for the first row
create_button("~", 0, 0)
create_button("!", 0, 1)
create_button("@", 0, 2)
create_button("#", 0, 3)
create_button("$", 0, 4)
create_button("%", 0, 5)
create_button("^", 0, 6)
create_button("&", 0, 7)
create_button("*", 0, 8)
create_button("(", 0, 9)
create_button(")", 0,10)
create_button("_" ,0 ,11)
create_button("+" ,0 ,12)

# Create the buttons for the second row
create_button("Tab", 1, 0)
create_button("Q", 1, 1)
create_button("W", 1, 2)
create_button("E", 1, 3)
create_button("R", 1, 4)
create_button("T", 1, 5)
create_button("Y", 1, 6)
create_button("U", 1, 7)
create_button("I", 1, 8)
create_button("O", 1, 9)
create_button("P", 1,10)
create_button("{",1 ,11)
create_button("}",1 ,12)

# Create the buttons for the third row
create_button("Caps",2 ,0 )
create_button("A",2 ,1 )
create_button("S",2 ,2 )
create_button("D",2 ,3 )
create_button("F",2 ,4 )
create_button("G",2 ,5 )
create_button("H",2 ,6 )
create_button("J",2 ,7 )
create_button("K",2 ,8 )
create_button("L",2 ,9 )
create_button(":",2 ,10 )
create_button("\"" ,2 ,11 )
create_button("|" ,2 ,12 )

# Create the buttons for the fourth row
create_button("Shift", 3, 0)
create_button("Z", 3, 1)
create_button("X", 3, 2)
create_button("C", 3, 3)
create_button("V", 3, 4)
create_button("B", 3, 5)
create_button("N", 3, 6)
create_button("M", 3, 7)
create_button("<", 3, 8)
create_button(">", 3, 9)
create_button("?", 3,10)
create_button("Shift" ,3 ,11)

# Create the buttons for the fifth row
up_arrow_button = tk.Button(keyboard_frame, text="↑", width=5, height=2, command=toggle_uppercase, bg="lightgray")
up_arrow_button.grid(row=4, column=1)

# create other buttons for the fifth row
create_button("Ctrl" ,4 ,0 )
create_button("Space" ,4 ,6 )
create_button("Alt" ,4 ,11 )
create_button("Ctrl" ,4 ,12 )
create_button("Delete" ,3 ,12 , command=delete_last_character)

# Add the frames to the main window and start the GUI
display_frame.pack()
keyboard_frame.pack()
root.mainloop()
