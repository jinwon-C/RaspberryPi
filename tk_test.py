import tkinter as tk
import os

def hello():
    os.system('python3 tk_print.py')
def Cancel():
    win.destroy()


win = tk.Tk()
btHello = tk.Button(win, text = "OK", command = hello)
btCancel = tk.Button(win, text ='Cacel', command = Cancel)
#btQuit = tk.Button(win, text = 'Quit', command = tk.quit)

btHello.pack()
btCancel.pack()
#btQuit.pack()

win.mainloop()
