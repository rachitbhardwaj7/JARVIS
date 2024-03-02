from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("450x900")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)

    img = Image.open("0aeec838dfb97807049e748e3d43a450.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)

    mixer.music.load("startup.mp3")
    mixer.music.play()

    for frame in ImageSequence.Iterator(img):
        frame = frame.resize((450, 900))
        frame = ImageTk.PhotoImage(frame)
        lbl.config(image=frame)
        root.update()
        time.sleep(0.05)

# Call the play_gif() function to display the GIF animation
play_gif()

# Start the Tkinter main loop
root.mainloop()
