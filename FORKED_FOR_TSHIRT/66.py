from tkinter import *
from pygame import mixer
root=Tk()
mixer.init()
def play():
    mixer.music.load('alan-walker-julie-bergan-seungri-Y4MZ59Tj.mp3')
    mixer.music.play()
def stop():
    mixer.music.stop()
def volume(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)
   
Button(root,text='play',command=play).pack()
Button(root,text='stop',command=stop).pack()
scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=volume)
scale.set(50)
scale.pack()
root.mainloop()

