from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led_1=LED(14) # RED
led_2=LED(15) # GREEN
led_3=LED(16) # YELLOW


win = Tk()
win.title("LED Radio Buttons")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

left_frame = Frame(win)
right_frame = Frame(win)
mid_frame = Frame(win)
left_frame.pack(side = LEFT)
right_frame.pack(side = RIGHT)
mid_frame.pack(side = RIGHT)


radioButton = IntVar()
radioButton.set("0")

def toggle_led():
    led_1.off()
    led_3.off()
    led_2.off()

    value = radioButton.get()

    if value == 3:
        led_3.on()
    if value == 1:
        led_1.on()
    if value == 2:
        led_2.on()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

label = Label(left_frame)
label.pack()
label.config(text = "Click button to change LED")


#radio buttons
LED_1 = Radiobutton(left_frame, text = "RED", variable=radioButton, value = 1, command = toggle_led)
LED_1.pack()

LED_2 = Radiobutton(left_frame, text = "GREEN", variable=radioButton, value = 2, command = toggle_led)
LED_2.pack()

LED_3 = Radiobutton(left_frame, text = "YELLOW", variable=radioButton, value = 3, command = toggle_led)
LED_3.pack()


exit_button = Button(win, text = "Close Program", font = myFont, command = close, bg = 'red', height = 1, width = 12)
exit_button.pack(side = BOTTOM)
win.protocol("WM_DELETE_WINDOW", close) 
win.mainloop()









