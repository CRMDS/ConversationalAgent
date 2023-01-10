from gtts import gTTS
from playsound import playsound
from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('Text to Speech Synthesis')
root.config(bg='white')

Label(root, text='TEXT TO SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

Msg = StringVar()
input_field = Entry(root, textvariable=Msg, width='60')
input_field.place(x=20, y=100)

def tts():
	Message = input_field.get()
	speech = gTTS(text=Message)
	speech.save("audio.mp3")
	playsound("audio.mp3")

def Exit():
	root.destroy()

def Reset():
	Msg.set("")

Button(root, text='PLAY', font='arial 15 bold', command=tts, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='Red').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=175, y=140)

root.mainloop()