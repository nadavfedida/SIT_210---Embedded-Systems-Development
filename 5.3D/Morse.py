from ast import Del
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO 
import time
RPi.GPIO.setmode(RPi.GPIO .BCM)
led = LED(14)

## tk and GUI setting
win = Tk()
win.title("Nadav - Morse Code converter")
MyFont = tkinter.font.Font(family = "Arial", size = 12, weight = "bold")

# GUI 
left_frame = Frame(win)
right_frame = Frame(win)
mid_frame = Frame(win)
left_frame.pack(side = LEFT)
right_frame.pack(side = RIGHT)
mid_frame.pack(side = RIGHT)

word = tkinter.StringVar()

#Morse code variable (times)
dotTime = .25
dashTime = .6
letterBreak = .3
wordBreak = 1


def Dot():
    led.on()
    time.sleep(dotTime)
    led.off()
    time.sleep(letterBreak)

def Dash():
    led.on()
    time.sleep(dashTime)
    led.off()
    time.sleep(letterBreak)

def WordBreak():
    time.sleep(wordBreak)


def blinkName(Input):
    #Word = Input.lower()
    for i in Input:
        if i == "a":  # dot dash
            print("hello")
            Dot()
            Dash()

        if i == "b": # dash dot dot dot 
            Dash()
            Dot()
            Dot()
            Dot()

        if i == "c": # dash dot dash dot
            Dash()
            Dot()
            Dash()
            Dot()

        if i == "d": # dash dot dot 
            Dash()
            Dot()
            Dot()

        if i == "e": # dot 
            Dot()

        if i == "f": # dot dot dash dot
            Dot()
            Dot()
            Dash()
            Dot()

        if i == "g": # dash dash dot
            Dash()
            Dash()
            Dot()

        if i == "h": # dot dot dot dot
            Dot()
            Dot()
            Dot()
            Dot()

        if i == "i": # dot dot
            Dot()
            Dot()

        if i == "j": # dot dash dash dash
            Dot()
            Dash()
            Dash()
            Dash()
        if i == "k": # dash dot dash
            Dash()
            Dot()
            Dash()

        if i == "l": #dot dash dot dot
            Dot()
            Dash()
            Dot()
            Dot()

        if i == "m": # dash dash
            Dash()
            Dash()

        if i == "n": #dash dot
            Dash()
            Dot()

        if i == "o": # dash dash dash
            Dash()
            Dash()
            Dash()

        if i == "p": # dot dash dash dot
            Dot()
            Dash()
            Dash()
            Dot()

        if i == "q": # dash dash dot dash
            Dash()
            Dash()
            Dot()
            Dash()


        if i == "r": # dot dash dot
            Dot()
            Dash()
            Dot()

        if i == "s": #dot dot dot
            Dot()
            Dot()
            Dot()

        if i == "t": # dash
            Dash()

        if i == "u": #dot dot dash
            Dot()
            Dot()
            Dash()

        if i == "v": #dot dot dot dash
            Dot()
            Dot()
            Dot()
            Dash()

        if i == "w": # dot dash dash
            Dot()
            Dash()
            Dash()

        if i == "x": # dash dot dot dash
            Dash()
            Dot()
            Dot()
            Dash()

        if i == "y": # dash dot dash dash
            Dash()
            Dot()
            Dash()
            Dash()

        if i == "z": # dash dash dot dot
            Dash()
            Dash()
            Dot()
            Dot()
        if i == " ": # work break
            WordBreak()




def Blinky():
    EnteredWord = word.get().lower()
    if len(EnteredWord) > 12:
        print("TOO LONG")
        return
    for letter in EnteredWord:
        blinkName(letter)


# Function to cleanly close the GUI
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Set up labels
label = Label(left_frame)
label.pack()
label.config(text = "Enter word ")



convertButton = Button(win, text = 'Convert', font = MyFont, command = Blinky, bg = 'bisque2', height = 1)
convertButton.pack()

word = Entry(win, font = MyFont, width = 19)
word.pack()

# EXIT BUTTON
exit_button = Button(win, text = "Quit", font = MyFont, command = close, bg = 'red', height = 1, width = 6)
exit_button.pack(side = RIGHT)

win.protocol("WM_DELETE_WINDOW", close) # attatch to close function and exit cleanly

win.mainloop() # keep GUI running 