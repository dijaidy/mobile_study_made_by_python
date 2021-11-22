from tkinter import *
import time

class 랭킹_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("랭킹")
        self.window.geometry("400x800")

        self.text=Label(self.window, text="지원하지 않는 기능입니다")
        self.text.pack()
        time.sleep(5)
        self.window.destroy()