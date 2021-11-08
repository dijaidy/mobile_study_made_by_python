from tkinter import *
import sys
import os
import time
from PIL import Image, ImageTk
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from 공부계획.공부계획_일일계획표_window import 일일공부계획_window
from information_management.user_information import 찜한교재_manage_user_information
from information_management.user_information import 공부계획_manage_user_information

class 공부계획_window(공부계획_manage_user_information, 찜한교재_manage_user_information):
    def __init__(self):
        super().__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("공부계획")
        self.window.geometry("400x800")

        self.present_month=self.return_present_time().tm_mon

        self.show_month=Label(self.window, text=str(self.present_month)+"월", font=("배달의민족 주아", 15), relief="solid")
        self.show_month.place(x=130, y=0, width=140, height=50) #몇 월인지 보여주는 label

        self.next_month_button=Button(
            self.window, 
            font=("배달의민족 주아", 14), 
            text="next month", 
            command=lambda: self.change_month(1)
        )
        self.next_month_button.place(x=270, y=0, width=130, height=50)

        self.previous_month_button=Button(
            self.window, 
            font=("배달의민족 주아", 13), 
            text="previous month", 
            command=lambda: self.change_month(-1)
        )
        self.previous_month_button.place(x=0, y=0, width=130, height=50)

        self.month_list=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.return_present_time().tm_year%4)==0:
            if (self.return_present_time().tm_year%100)==0:
                if (self.return_present_time().tm_year%400)==0:
                    self.month_list[1]=29
                pass
            self.month_list[1]=29

        self.calendar_day=[
            Button(self.window, font=("배달의민족 주아", 12), text="1", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=1))), 
            Button(self.window, font=("배달의민족 주아", 12), text="2", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=2))), 
            Button(self.window, font=("배달의민족 주아", 12), text="3", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=3))), 
            Button(self.window, font=("배달의민족 주아", 12), text="4", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=4))), 
            Button(self.window, font=("배달의민족 주아", 12), text="5", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=5))), 
            Button(self.window, font=("배달의민족 주아", 12), text="6", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=6))), 
            Button(self.window, font=("배달의민족 주아", 12), text="7", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=7))), 
            Button(self.window, font=("배달의민족 주아", 12), text="8", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=8))), 
            Button(self.window, font=("배달의민족 주아", 12), text="9", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=9))), 
            Button(self.window, font=("배달의민족 주아", 12), text="10", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=10))), 
            Button(self.window, font=("배달의민족 주아", 12), text="11", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=11))), 
            Button(self.window, font=("배달의민족 주아", 12), text="12", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=12))), 
            Button(self.window, font=("배달의민족 주아", 12), text="13", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=13))), 
            Button(self.window, font=("배달의민족 주아", 12), text="14", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=14))), 
            Button(self.window, font=("배달의민족 주아", 12), text="15", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=15))), 
            Button(self.window, font=("배달의민족 주아", 12), text="16", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=16))), 
            Button(self.window, font=("배달의민족 주아", 12), text="17", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=17))), 
            Button(self.window, font=("배달의민족 주아", 12), text="18", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=18))), 
            Button(self.window, font=("배달의민족 주아", 12), text="19", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=19))), 
            Button(self.window, font=("배달의민족 주아", 12), text="20", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=20))), 
            Button(self.window, font=("배달의민족 주아", 12), text="21", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=21))), 
            Button(self.window, font=("배달의민족 주아", 12), text="22", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=22))), 
            Button(self.window, font=("배달의민족 주아", 12), text="23", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=23))), 
            Button(self.window, font=("배달의민족 주아", 12), text="24", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=24))), 
            Button(self.window, font=("배달의민족 주아", 12), text="25", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=25))), 
            Button(self.window, font=("배달의민족 주아", 12), text="26", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=26))), 
            Button(self.window, font=("배달의민족 주아", 12), text="27", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=27))), 
            Button(self.window, font=("배달의민족 주아", 12), text="28", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=28))), 
            Button(self.window, font=("배달의민족 주아", 12), text="29", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=29))), 
            Button(self.window, font=("배달의민족 주아", 12), text="30", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=30))), 
            Button(self.window, font=("배달의민족 주아", 12), text="31", command=lambda: 일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=31)))
        ]   #달력구성-일

        #버튼들 배치
        self.change_month(index=0)

        self.window.mainloop()


    def change_month(self, index):

        if (self.present_month == 1 and index == (-1)) or (self.present_month == 12 and index == 1):
            index=0
        else:
            self.present_month+=index
        
        self.show_month.configure(text=str(self.present_month)+"월")

        y_coordinate=50
        x_coordinate=self.carculate_wday(month=self.present_month, day=1)

        for i in range(0, self.month_list[self.present_month-1]):
            self.calendar_day[i].place(x=(x_coordinate%7)*57, y=y_coordinate, width=57, height=50)

            if (x_coordinate%7) == 6:
                y_coordinate += 50
            x_coordinate+=1
            

        if self.month_list[self.present_month-1]<self.month_list[self.present_month-index-1]+1: #present_month의 최대 날짜 이후의 버튼을 숨김
            for i in range(self.month_list[self.present_month-1], 31):
                self.calendar_day[i].place_forget()

    

    def carculate_yday(self, month, day):
        return_value=0
        for i in range(month-1):
            return_value=return_value+self.month_list[i]
        return return_value+day

    def carculate_wday(self, month, day):
        year=self.return_present_time().tm_year - 1
        wday=(365*year+year//4-year//100-year//400+self.carculate_yday(month=month, day=day))%7
        if wday == 0:
            wday = 6
        else:
            wday -= 1

        return wday-3