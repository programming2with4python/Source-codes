# Importing modules
from tkinter import *
from tkinter import ttk
from googletrans import Translator

# Creating window
window = Tk()
window.title("GUI Language Translator")
window.geometry("600x300")

# Creating input and output text widgets
input_text = Text(window, font=("Arial", 12))
input_text.place(x=30, y=30, width=250, height=200)
output_text = Text(window, font=("Arial", 12))
output_text.place(x=320, y=30, width=250, height=200)
output_text.config(state="disabled")

# Creating language options
languages = ["English", "Spanish", "French", "German", "Italian", "Chinese", "Japanese", "Hindi"]
language_codes = ["en", "es", "fr", "de", "it", "zh-CN", "ja", "hi"]

input_lang = StringVar()
input_choice = ttk.Combobox(window, textvariable=input_lang, values=languages)
input_choice.place(x=40, y=250)
input_choice.set("English")

output_lang = StringVar()
output_choice = ttk.Combobox(window, textvariable=output_lang, values=languages)
output_choice.place(x=435, y=250)
output_choice.set("Spanish")

# Creating translate button
from translate import Translator

def translate():
    # Getting the input and output languages
    input_lan = input_lang.get()
    output_lan = output_lang.get()
    # Getting the input text
    input_txt = input_text.get(1.0, END)
    # Creating a translator object
    translator = Translator(to_lang=output_lan)
    # Translating the input text
    output_txt = translator.translate(input_txt)
    # Displaying the output text
    output_text.config(state="normal")
    output_text.delete(1.0, END)
    output_text.insert(END, output_txt)
    output_text.config(state="disabled")

translate_button = Button(window, text="Translate", command=translate)
translate_button.place(x=274, y=250)

# Running the window loop
window.mainloop()
