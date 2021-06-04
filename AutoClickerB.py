import time
import threading
import tkinter 
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode





button = Button.left
start_stop_key = KeyCode(char='l')
exit_key = KeyCode(char='/')



class ClickMouse(threading.Thread):
    def __init__(self,button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True
    

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                
mouse = Controller()
click_thread = ClickMouse(button)
click_thread.start()

gui = tkinter.Tk()
 
myLabel1 = tkinter.Label(gui,text="    Program is Currently running, To stop or start autoclicking press L " + " Press / to end the program   ")
myLabel2 = tkinter.Label(gui,text="                                 ")
myLabel3 = tkinter.Label(gui,text="    Edited by @bolony21, Source code/Tutorial from: https://nitratine.net/blog/post/python-auto-clicker/  ")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=2,column=0)



gui.update()



def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        gui.destroy()
        
        


with Listener(on_press=on_press) as listener:
    listener.join()





