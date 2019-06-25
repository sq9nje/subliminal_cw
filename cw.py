#!/usr/bin/env python3

from morsecodelib import sound as morseSound
from morsecodelib.config import config as morseConfig
import tkinter as tk
import random
import argparse

def play_character():
    c = random.choice(characters)
    lbl.configure(text=c)
    app.update()
    player.text_to_sound(c)
    app.after(conf.delay, play_character) 

def parse_config():
    parser = argparse.ArgumentParser(description='Learn CW while you work!')
    parser.add_argument('-s', '--wpm', action='store', dest='wpm', default=20, help='Speed in WPM. Default 20')
    parser.add_argument('-t', '--tone', action='store', dest='tone', default=600, help='Tone frequency in Hz. Default 600')
    parser.add_argument('-d', '--delay', action='store', dest='delay', default=1000, help='Delay between characters in ms. Default 1000')
    parser.add_argument('--debug', action='store_true', dest='debug', default=False, help='Dispaly debug information.')
    return parser.parse_args()

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "O", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

if __name__ == '__main__':
    conf = parse_config()
    if conf.debug:
        print('Speed     = {!r}'.format(conf.wpm))
        print('Tone      = {!r}'.format(conf.tone))
        print('Delay     = {!r}'.format(conf.delay))

    morseConfig.WORDS_PER_MINUTE = conf.wpm
    morseConfig.FREQUENCY = conf.tone

    app = tk.Tk()
    player = morseSound.MorseSoundPlayer()

    app.title('Subliminal CW')
    app.geometry('200x120')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    
    lbl = tk.Label(app, font=("Courier", 75, 'bold'), text='')
    lbl.grid(column=0, row=0)
    
    app.after(conf.delay, play_character)
    app.mainloop()