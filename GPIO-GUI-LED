####################################################
#  Author:        Simon C.
#  Last Updated:  03/01/2022
#  Revision:      X1
#  Description:   GPIO GUI
####################################################

# Libraries:
import RPi.GPIO as GPIO
import tkinter as tk
from time import sleep

# Initialize
GPIO14 = 14
GPIO15 = 15
GPIO14_state = True
GPIO15_state = True

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO14, GPIO.OUT)
GPIO.setup(GPIO15, GPIO.OUT)

# Tk Root Widget
master = tk.Tk()
master.title("GPIO Control")
master.geometry("300x100")

# Label GPIO14 Button to indicate HIGH/LOW
def GPIO14button():
	global GPIO14_state
	if GPIO14_state == True:
		GPIO.output(GPIO14, GPIO14_state)
		GPIO14_state = False
		ONlabel = tk.Label(master, text = " ON", fg = "green")
		ONlabel.grid(row = 0, column = 1)
	else:
		GPIO.output(GPIO14, GPIO14_state)
		GPIO14_state = True
		ONlabel = tk.Label(master, text = "OFF", fg = "red")
		ONlabel.grid(row = 0, column = 1)

def GPIO15button():
	global GPIO15_state
	if GPIO15_state == True:
		GPIO.output(GPIO15, GPIO15_state)
		GPIO15_state = False
		ONlabel = tk.Label(master, text = " ON", fg = "green")
		ONlabel.grid(row = 1, column = 1)
	else:
		GPIO.output(GPIO15, GPIO15_state)
		GPIO15_state = True
		ONlabel = tk.Label(master, text = "OFF", fg = "red")
		ONlabel.grid(row = 1, column = 1)

# Tkinker Buttons
ONbutton = tk.Button(master, text = "GPIO 14", bg = "green", command = GPIO14button)
ONbutton.grid(row = 0, column = 0)

ONbutton = tk.Button(master, text = "GPIO 15", bg = "green", command = GPIO15button)
ONbutton.grid(row = 1, column = 0)

Exitbutton = tk.Button(master, text = "EXIT", bg = "red", command = master.destroy)
Exitbutton.grid(row = 2, column = 0)
master.mainloop()
