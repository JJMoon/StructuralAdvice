from Tkinter import *

class MessageDlg:
    def __init__ (self, Message):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        
        self.btn = Button(frame, text=Message, command=frame.quit)
        self.btn.pack(side=LEFT)
        root.mainloop()
