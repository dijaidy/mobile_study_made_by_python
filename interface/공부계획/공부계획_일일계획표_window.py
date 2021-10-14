from tkinter import *

class 공부계획_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("공부계획")
        self.window.geometry("400x800")
        self.canvas=Canvas(self.window, width=400, height=400)  #트킨터에서 도형을 그리기 위한 바탕 설정
        self.canvas.place(x=0, y=0) #바탕 위치 설정
        self.clock=self.canvas.create_oval(x1 = 40, y1 = 40, x2 = 360, y2 = 360)