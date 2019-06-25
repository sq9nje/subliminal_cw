#!/usr/bin/env python3

from morsecodelib import sound as morseSound
from morsecodelib.config import config as morseConfig
import tkinter as tk
import random

def play_character():
    c = random.choice(characters)
    lbl.configure(text=c)
    app.update()
    player.text_to_sound(c)
    app.after(1000, play_character) 

morseConfig.WORDS_PER_MINUTE = 25
morseConfig.FREQUENCY = 600
player = morseSound.MorseSoundPlayer()

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "O", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

app = tk.Tk()
app.title('Subliminal CW')
app.geometry('200x120')
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
lbl = tk.Label(app, font=("Courier", 75, 'bold'), text='')
lbl.grid(column=0, row=0)

app.after(1000, play_character)
app.mainloop()