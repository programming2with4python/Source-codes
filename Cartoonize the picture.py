import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def cartoonify(file_path):
    # Read the image
    img = cv2.imread(file_path)

    # Get the edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Convert to RGB and return
    return cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

def open_file():
    file_path = filedialog.askopenfilename()
    cartoon_image = cartoonify(file_path)
    
    # Display the cartoonified image in the GUI window
    cartoon_image = Image.fromarray(cartoon_image)
    cartoon_image.thumbnail((800, 800))
    cartoon_image = ImageTk.PhotoImage(cartoon_image)
    
    label.config(image=cartoon_image)
    label.image = cartoon_image

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    
    if file_path:
        # Get the current image from the label and save it to the specified file
        cartoon_image = label.image
        cartoon_image.save(file_path)

root = tk.Tk()
root.title("Cartoonify")
root.geometry("800x800")

open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack()

save_button = tk.Button(root, text="Save Image", command=save_file)
save_button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
