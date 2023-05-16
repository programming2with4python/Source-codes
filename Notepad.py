# Importing tkinter module
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import font

# Creating the root window
root = Tk()
root.title("Notepad")

# Creating the text area
text_area = Text(root, font=("Arial", 12), bg="#F0F0F0", fg="#000000")
text_area.pack(expand=True, fill=BOTH)

# Creating the menu bar
menu_bar = Menu(root)

# Creating the file menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

# Creating the edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Creating the format menu
format_menu = Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font", command=lambda: choose_font())
format_menu.add_command(label="Background Color", command=lambda: choose_bg_color())
format_menu.add_command(label="Text Color", command=lambda: choose_fg_color())
menu_bar.add_cascade(label="Format", menu=format_menu)

# Creating the help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_about())
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configuring the root window with the menu bar
root.config(menu=menu_bar)

# Defining the function to create a new file
def new_file():
    # Asking for confirmation if the text area is not empty
    if len(text_area.get("1.0", END)) > 1:
        answer = messagebox.askyesno("Save File", "Do you want to save the current file?")
        if answer == True:
            save_file()
    # Clearing the text area and resetting the title
    text_area.delete("1.0", END)
    root.title("Notepad")

# Defining the function to open an existing file
def open_file():
    # Asking for confirmation if the text area is not empty
    if len(text_area.get("1.0", END)) > 1:
        answer = messagebox.askyesno("Save File", "Do you want to save the current file?")
        if answer == True:
            save_file()
    # Opening a file dialog and reading the file content
    file = filedialog.askopenfile(mode="r")
    if file is not None:
        content = file.read()
        text_area.delete("1.0", END)
        text_area.insert("1.0", content)
        file.close()
        # Updating the title with the file name
        root.title("Notepad - " + file.name.split("/")[-1])

# Defining the function to save the current file
def save_file():
    # Opening a save as dialog and writing the file content
    file = filedialog.asksaveasfile(mode="w")
    if file is not None:
        content = text_area.get("1.0", END)
        file.write(content)
        file.close()
        # Updating the title with the file name
        root.title("Notepad - " + file.name.split("/")[-1])

# Defining the function to choose a font for the text area
def choose_font():
    # Opening a font chooser dialog and applying the selected font
    font_tuple = font.askfont(root)
    if font_tuple:
        font_name = font_tuple["family"]
        font_size = font_tuple["size"]
        font_weight = font_tuple["weight"]
        font_style = font_tuple["slant"]
        font_underline = font_tuple["underline"]
        font_overstrike = font_tuple["overstrike"]
        text_area.config(font=(font_name, font_size, font_weight, font_style, font_underline, font_overstrike))

# Defining the function to choose a background color for the text area
def choose_bg_color():
    # Opening a color chooser dialog and applying the selected color
    color_code = colorchooser.askcolor(title ="Choose background color")
    if color_code:
        text_area.config(bg=color_code[1])

# Defining the function to choose a text color for the text area
def choose_fg_color():
    # Opening a color chooser dialog and applying the selected color
    color_code = colorchooser.askcolor(title ="Choose text color")
    if color_code:
        text_area.config(fg=color_code[1])

# Defining the function to show the about message
def show_about():
    messagebox.showinfo("About Notepad", "This is an improved Notepad application created with Python and Tkinter.")

# Running the main loop
root.mainloop()
