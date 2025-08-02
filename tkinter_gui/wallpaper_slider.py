from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()

root.title("Wallpaper slider")
root.geometry("500x450")
root.configure(background="black")
root.iconbitmap("cat_icon.ico")

counter = 1

def swap_image():
    global counter
    img_label.config(image=img_list[counter % 9])
    counter = counter + 1
    print(counter)

# files will store all the image files inside a list
# which later will be used to create object of every img
files = os.listdir('wallpapers')
img_list = []

for file in files:
    img = Image.open(os.path.join('wallpapers', file))
    img_resize = img.resize((400, 300))
    img_list.append(ImageTk.PhotoImage(img_resize))

img_label = Label(root, image=img_list[0])
img_label.pack(pady=(25, 20))

btn = Button(root, text="Next", fg="black", bg="white", width=10, height=1, command=swap_image)
btn.pack()
btn.config(font=('verdana', 14))

root.mainloop()