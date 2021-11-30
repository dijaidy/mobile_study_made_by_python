from tkinter import *
import time
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import sys
import os
import json
import webbrowser

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from information_management.api_loading import API_loading

api_loading_source = API_loading()

class 학교수업복습_window:
    def __init__(self, nickname):
        # 창 설정
        self.window = Tk()
        self.window.title("학교수업복습")
        self.window.geometry("400x800")       
        self.window.resizable(width=False, height=False)

        # 닉네임
        self.nickname = nickname

        # 타이틀 설정
        self.title = Label(self.window, font=('배달의민족 주아', 25), text='학교 수업 복습', bg='skyblue', justify=LEFT, anchor=W, padx=15)
        self.title.pack(side=TOP, anchor=N, fill=X, ipady=10)
        
        # 날짜 설정
        self.today = datetime.today()
        self.showing_date = self.today

        #요일
        self.days = ['월', '화', '수', '목','금', '토', '일']
        self.week_nm = self.showing_date.weekday()
        self.date_week = self.days[self.week_nm]

        # 날짜 표시
        self.showing_date_text = self.showing_date.strftime("오늘: %y.%m.%d("+self.date_week+')')
        self.today_date = Label(self.window, font=('배달의민족 주아', 20), anchor=CENTER,  text=self.showing_date_text)
        self.today_date.pack(side=TOP, anchor=N, fill=X, ipady=10)

        # 시간표 불러오기
        with open(r'information\users_information_file.json', 'r', encoding='utf-8') as in_file:
            user_file = json.load(in_file)
            user_file = user_file[self.nickname]
            self.school = user_file['school']
            self.grade = user_file['grade']
            self.school_class = user_file['school_class']
        tuple = api_loading_source.load_school_timetable(self.school, self.grade, self.school_class)
        self.school_timetable = tuple[0]
        self.from_day_original = tuple[1]
        self.to_day_original = tuple[2]
        self.from_day = self.from_day_original.strftime('%y.%m.%d(월)')
        self.to_day = self.to_day_original.strftime('%y.%m.%d(금)')
        timetable_date_text = '%s ~ %s' % (self.from_day, self.to_day)


        # 시간표 프레임
        self.timetable_frame = Frame(self.window, width=400, bg='white')
        self.timetable_frame.pack(side=TOP, anchor=N, fill=X, pady=(50,0))   
        
        self.back_button = Button(self.window, text='뒤로가기', font=('배달의민족 주아', 15), anchor=CENTER, pady=10, command=self.back)
        
        self.timetable_frame2 = Frame(self.window, width=400, bg='white')

        # 이번주 복습
        self.title_label = Label(self.timetable_frame, font=('배달의민족 주아', 18), anchor=CENTER, pady=10, text = '복습하고자 하는 이번주 학교수업 찾기', bg='skyblue', fg='black')
        self.title_label.pack(side=TOP, fill=X, padx=2, pady=2)

        # 시간표 표시 날짜
        self.timetable_date = Label(self.timetable_frame, font=('배달의민족 주아', 17), anchor=CENTER, text=timetable_date_text, bg='skyblue', fg='white')
        self.timetable_date.pack(side=TOP, anchor=N, fill=X, ipady=10, padx=2, pady=2)
        
        # 요일 표시
        self.button_list = []
        for i in range(0, 5):
            date = self.days[i]
            button = Button(self.timetable_frame, font=('배달의민족 주아', 15), anchor=CENTER, pady=10, text=date+'요일', bg='skyblue',fg='white', command=lambda x=i:self.present_selected_date_timetable(x, self.days[x]))
            button.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=2, pady=2)
            self.button_list.append(button)

        self.label_list = []







        # 루프
        self.window.mainloop()

    def present_selected_date_timetable(self, week_nm, date):
        # 시간표 위치조정
        for i in range(0, 5):
            self.button_list[i].destroy()

        # 뒤로가기 버튼
        self.back_button.pack(side=TOP, anchor=N, fill=X)

        # 제목바꾸기

        
        # 프레임 전환
        self.timetable_frame.pack_forget()
        self.timetable_frame2 = Frame(self.window, width=400, bg='white')
        self.timetable_frame2.pack(side=TOP, anchor=N, fill=X, pady=(10, 0))
        self.title_label2 = Label(self.timetable_frame2, font=('배달의민족 주아', 18), anchor=CENTER, pady=10, text = '복습하고자 하는 학교수업 선택', bg='skyblue', fg='black')
        self.title_label2.pack(side=TOP, fill=X, padx=2, pady=2)

        timetable_date_text = self.from_day_original + timedelta(days=week_nm)
        timetable_date_text = timetable_date_text.strftime('%y.%m.%d('+date+')')
        self.timetable_date.config(text = timetable_date_text + '  시간표')

        #시간표 띄우기
        self.school_timetable2 = self.school_timetable[date]   
        self.timetable_frame2_list = [] 
        self.timetable_list = []
        
        for i in range(1, 8):

            timetable_frame2 = Frame(self.timetable_frame2, width=400, bg='white')
            timetable_frame2.pack(side=TOP, anchor=N, fill=X, pady=2)
            self.timetable_frame2_list.append(timetable_frame2)


            # 교시
            Label(self.timetable_frame2_list[i-1], font=('배달의민족 주아', 17), anchor=CENTER, text=str(i), bg='skyblue', fg='white', width=10)\
                .pack(side=LEFT, anchor=N, fill=BOTH, padx=2, ipady=10)

            # 수업
            if str(i) in self.school_timetable2:
                text = self.school_timetable2[str(i)].replace('-', '')
                lesson = Button(self.timetable_frame2_list[i-1], font=('배달의민족 주아', 17), anchor=CENTER, text=text, bg='skyblue', fg='white', command=lambda x=i: self.open_edunet(self.school_timetable2[str(x)].replace('-', '')))
                lesson.pack(side=LEFT, anchor=N, fill=BOTH, expand=True, padx=2, ipady=10)
            else:
                text = '수업없음'
                lesson = Button(self.timetable_frame2_list[i-1], font=('배달의민족 주아', 17), anchor=CENTER, text=text, bg='skyblue', fg='white')
                lesson.pack(side=LEFT, anchor=N, fill=BOTH, expand=True, padx=2, ipady=10)
                
    def open_edunet(self, subject):
        with open(r'information\subject_id_dict.json', 'r', encoding='utf-8') as in_file:
            subject_id_dict = json.load(in_file)
            if subject in subject_id_dict[self.grade]:
                link = 'https://www.edunet.net/nedu/contsvc/subjectForm.do?menu_id=3&sub_clss_id=%s' % subject_id_dict[self.grade][subject]
                webbrowser.open(link)
            else:
                print("해당 과목은 복습을 지원하지 않음.")

    def back(self):
        self.timetable_frame2.destroy()
        self.timetable_frame.pack(side=TOP, anchor=N, fill=X, pady=(50,0))
        self.back_button.pack_forget()
        # 요일 표시
        self.button_list = []
        for i in range(0, 5):
            date = self.days[i]
            button = Button(self.timetable_frame, font=('배달의민족 주아', 15), anchor=CENTER, pady=10, text=date+'요일', bg='skyblue',fg='white', command=lambda x=i:self.present_selected_date_timetable(x, self.days[x]))
            button.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=2, pady=2)
            self.button_list.append(button)




