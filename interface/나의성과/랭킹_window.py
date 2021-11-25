from tkinter import *
import time
from PIL import Image, ImageTk


class 랭킹_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("랭킹")
        self.window.geometry("400x800")
        # 이미지 크기 조정
        size_adjusting_image = Image.open("image_sources\미완성_카테고리_사진.png")
        image = size_adjusting_image.resize(
            (400, 450),  # 어떤지 보기 #어떤지 보기#어떤지 보기#어떤지 보기#어떤지 보기  #어떤지 보기
            Image.ANTIALIAS,
        )

        resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.image = Label(self.window, image=resized_image)
        self.image.place(x=0, y=0, width=400, height=600)
        self.text = Label(self.window, font=('배달의민족 주아', 25), text='지원 예정인 기능입니다.')
        self.text.place(x=0, y=600, width=400, height=200)

        # 루프
        self.window.mainloop()
        self.window.resizable(width=False, height=False)