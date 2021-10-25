from tkinter import *
import sys
import os
import time
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from 공부계획.공부계획_일일계획표_window import 일일공부계획_window
from information_management.user_information import 공부계획_manage_user_information

class 공부계획_window(공부계획_manage_user_information):
    def __init__(self):
        super().__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("공부계획")
        self.window.geometry("400x800")

        self.present_month=self.return_present_time().tm_mon

        self.calendar_day={}   #달력구성-일
        for i in range(1, 32):
            self.calendar_day[i]=Button(self.window, command=일일공부계획_window(planning_day=self.carculate_yday(month=self.present_month, day=i)))
        
        self.next_month_button=Button(
            self.window, 
            font=("배달의민족 주아", 15), 
            text="next month", 
            command=lambda: self.change_month(1)
        )
        self.next_month_button.place(x=50, y=0, width=80, height=50)
        self.previous_month_button=Button(
            self.window, 
            font=("배달의민족 주아", 15), 
            text="previous month", 
            command=lambda: self.change_month(-1)
        )
        self.previous_month_button.place(x=270, y=0, width=80, height=50)

        self.show_present_month=Label(self.window, text=str(self.present_month)+"월", font=("배달의민족 주아", 15), relief="solid")
        self.show_present_month.place(x=130, y=0, width=140, height=50)

    def change_month(self, index):
        self.present_month+=index

        self.show_present_month=Label(self.window, text=str(self.present_month)+"월", font=("배달의민족 주아", 15), relief="solid")
        
        month_list=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y_coordinate=50
        for i in range(1, month_list[self.present_month]):
            wday={self.return_present_time().tm_wday, self.return_present_time().tm_yday}
            wday=wday[0]+wday[1]-self.carculate_yday(month=self.present_month, day=i)
            self.calendar_day[i].place(relwidth=1/7, relx=(wday%7)/7, y=y_coordinate, height=50)
        if month_list[self.present_month]<month_list[self.present_month-index]:
            for i in range(month_list[self.present_month]+1, month_list[self.present_month-index]+1):
                self.calendar_day[i].place_forget()

    def carculate_yday(self, month, day):
        month_list=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year=self.return_present_time().tm_year
        if (year%4)==0:
            if (year%100)==0:
                if (year%400)==0:
                    month_list[1]=29
                pass
            month_list[1]=29
        return_value=0
        for i in range(month-1):
            return_value=return_value+month_list[i]
        return return_value+day
 