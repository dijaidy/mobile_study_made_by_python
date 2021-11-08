from tkinter import *
import sys
import os
import webbrowser
from tkinter import ttk as tk
from PIL import Image, ImageTk
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)

from information_management.user_information import 찜한교재_manage_user_information
from information_management.user_information import 공부계획_manage_user_information

class 일일공부계획_window(공부계획_manage_user_information, 찜한교재_manage_user_information):
    def __init__(self, planning_day):
        super().__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("일일공부계획")
        self.window.geometry("400x800")
        self.canvas=Canvas(self.window, width=400, height=400)  #트킨터에서 도형을 그리기 위한 바탕 설정
        self.canvas.place(x=0, y=0) #바탕 위치 설정
        self.clock=self.canvas.create_oval(40, 40, 360, 360)    #시계정의
        self.planned_time={}      #여기서 계획표에서 공부 시작시간, 끝내는 시간 보여주는 부채꼴을 만들 것임
        self.plan_list=self.plan_list_for_month[planning_day]
        self.plan_list_key=self.plan_list.keys()  #공부계획의 키(교재)를 추출하여 리스트로 정리
        for i in range(len(self.plan_list)-1):    #시간표를 보여주는 부채꼴 생성
            if i>10:
                break
            angle={}
            angle=self.correct_angle(start_hour=self.plan_list[self.plan_list_key[i]]["start_time"]["hour"], start_minute=self.plan_list[self.plan_list_key[i]]["start_time"]["minute"], end_hour=self.plan_list[self.plan_list_key[i]]["end_time"]["hour"], end_minute=self.plan_list[self.plan_list_key[i]]["end_time"]["minute"])
            for_start=angle[0]
            for_extent=angle[1]
            self.planned_time[i]=self.canvas.create_arc(40, 40, 360, 360, start=for_start, extent=for_extent)

        # 책 전체개수/현재 위치
        self.searching_order = Label(self.window, font=("배달의민족 주아", 10), text="  /  ")
        self.searching_order.place(x=250, y=415, width=125, height=40)
        
        #이전 교재 보여주기 버튼
        self.prior_button = Button(self.window, text = "이전 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book(index_moving = -1))
        self.prior_button.place(relx = 0, y = 770, height = 30, width = 150)

        #계획 등록 버튼
        self.plan_maker_button = Button(self.window, text="저장", font= ("배달의민족 주아", 10), command = lambda: self.plan_maker(planning_day=planning_day))
        

        #다음 교재 보여주기 버튼
        self.next_button = Button(self.window, text = "다음 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book(index_moving = 1))
        self.next_button.place(relx = 2/3, y = 770, height = 30, width = 150)

        # 교재 이미지
        self.book_image = Label(self.window, borderwidth=2, relief="sunken", text="자료 없음")
        self.book_image.place(x=25, y=470, height=200, width=160)

        # 교재 타이틀
        self.book_title = Message(self.window, font=("배달의민족 주아", 13))
        self.book_title.place(x=0, y=400, height=70, width=160)

        #시간 입력
        self.start_time = Entry(self.window, font=("배달의민족 주아", 10))
        self.end_time = Entry(self.window, font=("배달의민족 주아", 10))
        self.start_time.place(x=200, y=570, width=140, height=50)
        self.end_time.place(x=200, y=620, width=140, height=50)

        # 기타 인스턴스변수 생성
        self.book_index = 0
        self.present_book = {}
        self.present_book_title = ""

        self.show_book()

    def plan_maker(self, planning_day):
        start_time={
            "hour" : self.start_time.get()[0:1], 
            "minute" : self.start_time.get()[2:3]
        }
        end_time={
            "hour" : self.end_time.get()[0:1], 
            "minute" : self.end_time.get()[2:3]
        }
        self.plus_plan_list(book_dict=self.chosen_book_dict[self.present_book_title], start_time=start_time, end_time=end_time, day=planning_day)

    def show_book(self, index_moving = 0):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 인덱스 조정
        if (self.book_index == 0) and (index_moving == -1):
            self.book_index = len(self.chosen_book_dict)-1
        elif self.book_index < len(self.chosen_book_dict)-1:
            self.book_index += index_moving
        elif self.book_index >= len(self.chosen_book_dict)-1:
            self.book_index = 0
        # 책제목 리스트
        title_list = list(self.chosen_book_dict.keys())

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = self.chosen_book_dict[title_list[self.book_index]]
        self.present_book = book
        self.present_book_title = title_list[self.book_index]
        url = book["cover"]

        os.system("curl " + url + " > image_sources\교재선택_image_file.jpg")

        # 이미지 크기 조정
        size_adjusting_image = Image.open("image_sources\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (size_adjusting_image.size[0] * 2, size_adjusting_image.size[1] * 2), Image.ANTIALIAS
        )

        resized_image = ImageTk.PhotoImage(image, master = self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book_image.config(image=resized_image, text="")

        # 타이틀 수정
        book_title_text = title_list[self.book_index]
        self.book_title.config(text = book_title_text)

        #인덱스 수정
        searching_order_text = "%s / %s" % (len(self.chosen_book_dict), self.book_index+1)
        self.searching_order.config(text=searching_order_text)

        self.window.mainloop()  