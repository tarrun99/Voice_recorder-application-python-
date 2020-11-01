
from tkinter import *
import sounddevice as sd 
import soundfile as sf 

def Voice_rec():
    fs = 48000
    duration = 5
    myrecording = sd.rec(int(duration * fs),samplerate = fs ,channels=2)
   
    sd.wait()
    return sf.write('mt_Audio_file.flac', myrecording, fs)

master = Tk()

Label(master, text="Voice Recorder :" ).grid(row=0, sticky=W, rowspan=5)
b = Button(master, text="start", command=Voice_rec)
b.grid(row = 0, column = 2, columnspan= 2, rowspan = 2, padx = 5, pady = 5)

mainloop()      