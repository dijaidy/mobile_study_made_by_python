from tkinter import *
import time
from PIL import Image, ImageTk
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from information_management.api_loading import API_loading

api_loading_source = API_loading()

class 학교수업복습_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("학교수업복습")
        self.window.geometry("400x800")       
        self.window.resizable(width=False, height=False)

        # 타이틀 설정
        self.title = Label(self.window, font=('배달의민족 주아', 25), text='학교 수업 복습', bg='skyblue', justify=LEFT, anchor=W, padx=15)
        self.title.pack(side=TOP, anchor=N, fill=X, ipady=10)
        
        # 날짜 설정
        self.today = datetime.today()
        self.showing_date = self.today
        #요일
        days = ['월요일', '화요일', '수요일', '목요일','금요일', '토요일','일요일']
        self.showing_date_week = days[self.showing_date.weekday()]
        # 날짜 표시
        self.showing_date_text = self.showing_date.strftime("%y.%m.%d("+self.showing_date_week+')')
        self.date = Label(self.window, font=('배달의민족 주아', 17), anchor=CENTER,  text=self.showing_date_text)
        self.date.pack(side=TOP, anchor=N, fill=X, ipady=10)

        # 부제: 오늘의 복습 순서
        self.subtitle = Label(self.window, font=('배달의민족 주아', 20), anchor=CENTER, pady=10, text='오늘의 복습 순서')
        self.subtitle.pack(side=TOP, anchor=N, fill=X, ipady=5)

        # 시간표 프레임
        self.timetable_frame = Frame(self.window, width=400, height=400)
        
        # 시간표 불러오기
        print(api_loading_source.load_school_timetable())
        self.label_list = []

        for i in range(1, 7+1):
            Label(self.timetable_frame, font=('배달의민족 주아', 15), anchor=CENTER, text='')



        # 루프
        self.window.mainloop()