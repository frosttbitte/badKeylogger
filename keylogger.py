import sys
from tkinter import Tk, Label
from tkinter.ttk import *
import time

def key_pressed(event):
    w = Label(window, text="Key Pressed: " + event.char)
    w.place(x=50,y=50)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}' .format(x,y))



def up(e):
    print('lmao\n', e.char, '\n', e)

def close(event):
    window.destroy()
    print(f"Window closed.")

#Logs to text file
class Logger:
 
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')
 
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
 
    def flush(self):
        self.console.flush()
        self.file.flush()

#Local time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

window = Tk()
window.bind("<Escape>", close)
window.bind('<Motion>', motion)
window.bind("<KeyPress>", key_pressed)
window.bind('<KeyRelease>', up)



path = 'C:/Users/Alex/Desktop/fox2/logs.txt'
sys.stdout = Logger(path)
print(f"Starting Log: {current_time}")


window.mainloop()

