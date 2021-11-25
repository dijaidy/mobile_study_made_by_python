from tkinter import *
import time

class show_message(object):
    def __init__(self, message):
        super(show_message, self).__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("알림창")
        self.window.geometry("300x100")
    
        self.message=Label(self.window, text=(str(message)), font=("배달의민족 주아", 14))
        self.message.place(x=0, y=0, relheight=1, relwidth=1)
        # 루프
        self.window.mainloop()
        self.window.resizable(width=False, height=False)