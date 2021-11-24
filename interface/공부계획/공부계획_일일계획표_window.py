from tkinter import *
import sys
import os
from tkinter import ttk as tk
from PIL import Image, ImageTk
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)

from information_management.user_information import 찜한교재_manage_user_information
from information_management.user_information import 공부계획_manage_user_information
from interface.공부계획.알리미_window import show_message

class 일일공부계획_window(공부계획_manage_user_information, 찜한교재_manage_user_information):
    def __init__(self, planning_day):
        super(일일공부계획_window, self).__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("일일공부계획")
        self.window.geometry("400x800")
        self.canvas=Canvas(self.window, width=400, height=400)  #트킨터에서 도형을 그리기 위한 바탕 설정
        self.canvas.place(x=0, y=0)
        self.tlrksvy=Message(self.window, font=("배달의민족 주아", 13), text="시간표")
        self.tlrksvy.place(y=5, x=160, width=80, height=30)
        self.clock=self.canvas.create_oval(40, 40, 360, 360, fill="LightSkyBlue3")    #시계정의
        self.planned_time={}      #여기서 계획표에서 공부 시작시간, 끝내는 시간 보여주는 부채꼴을 만들 것임
        self.plan_list=self.plan_list_for_month[planning_day]
        self.planning_day=planning_day
        self.show_plan()

        # 책 전체개수/현재 위치
        self.searching_order = Label(self.window, font=("배달의민족 주아", 10), text="  /  ")
        self.searching_order.place(x=250, y=415, width=125, height=40)
        
        #이전 교재 보여주기 버튼
        self.prior_button = Button(self.window, text = "이전 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book(index_moving = -1))
        self.prior_button.place(relx = 0, y = 770, height = 30, relwidth = 1/3)

        #계획 등록 버튼
        self.plan_maker_button = Button(self.window, text="저장", font= ("배달의민족 주아", 10), command = lambda: self.plan_maker(planning_day=planning_day))
        self.plan_maker_button.place(relx=1/3, y=770, height = 30, relwidth= 1/3)

        #다음 교재 보여주기 버튼
        self.next_button = Button(self.window, text = "다음 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book(index_moving = 1))
        self.next_button.place(relx = 2/3, y = 770, height = 30, relwidth = 1/3)

        # 교재 이미지
        self.book_image = Label(self.window, borderwidth=2, relief="sunken", text="자료 없음")
        self.book_image.place(x=25, y=470, height=200, width=160)

        # 교재 타이틀
        self.book_title = Message(self.window, font=("배달의민족 주아", 12))
        self.book_title.place(x=0, y=400, height=70, width=160)

        #시간 입력
        self.start_time = Entry(self.window, text="시작시간 입력 ex: 12:00", font=("배달의민족 주아", 10))
        self.end_time = Entry(self.window, text="끝나는 시간 입력 ex: 15:00", font=("배달의민족 주아", 10))
        self.start_time.place(x=200, y=570, width=140, height=50)
        self.end_time.place(x=200, y=620, width=140, height=50)

        # 기타 인스턴스변수 생성
        self.book_index = 0
        self.present_book = {}
        self.present_book_title = ""

        self.show_book()

        self.window.mainloop()

    def plan_maker(self):
        if int(self.start_time.get()[0:])>int(self.end_time.get()[0:]) or int(self.start_time.get()[0:])>2400 or int(self.end_time.get()[0:])>2400:
            show_message("24시 이후의 계획은 다음 날에 하시길 바랍니다")
            return
        start_time={
            "hour" : self.start_time.get()[0:2], 
            "minute" : self.start_time.get()[2:]
        }
        end_time={
            "hour" : self.end_time.get()[0:2], 
            "minute" : self.end_time.get()[2:]
        }
        self.plus_plan_list(book_dict={self.present_book_title : self.chosen_book_dict[self.present_book_title]}, start_time=start_time, end_time=end_time, day=self.planning_day)
        show_message("교재가 저장되었습니다\n중복저장될 수 있으므로 유의하시길 바랍니다")
        self.plan_list=self.plan_list_for_month[self.planning_day]
        self.show_plan()

    def plan_destroyer(self, book_dict):
        self.delete_plan_list(book_dict=book_dict, day=self.planning_day)
        show_message("계획이 삭제되었습니다")
        self.plan_list=self.plan_list_for_month[self.planning_day]
        self.show_plan()

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
        searching_order_text = "%s / %s" % (self.book_index+1, len(self.chosen_book_dict))
        self.searching_order.config(text=searching_order_text)

        #입력칸 초기화
        self.start_time.delete(0, "end")
        self.end_time.delete(0, "end")

        #현재 보여주는 책으로 계획을 세웠는가에 따라 버튼의 기능을 저장, 삭제로 바꿈
        simple_bool=False
        i=0
        while (i<len(self.plan_list)):
            if (self.present_book_title in self.plan_list[i].keys()):
                simple_bool=True
                break
            i+=1
        if (simple_bool==False):
            self.plan_maker_button = Button(self.window, text="저장", font= ("배달의민족 주아", 10), command = lambda: self.plan_maker())
            self.plan_maker_button.place(relx=1/3, y=770, height = 30, relwidth= 1/3)
        else:
            del(self.planned_time[i])
            self.plan_maker_button = Button(self.window, text="삭제", font= ("배달의민족 주아", 10), command= lambda: self.plan_destroyer(i))
            self.plan_maker_button.place(relx=1/3, y=770, height = 30, relwidth= 1/3)
            #계획 중에 있는 책이면 계획한 시간대가 어딘지 보여줌
            self.start_time.insert(0, self.plan_list[i]["start_time"]["hour"]+self.plan_list[i]["start_time"]["minute"])
            self.end_time.insert(0, self.plan_list[i]["end_time"]["hour"]+self.plan_list[i]["end_time"]["minute"])

        self.window.mainloop()  

    def show_plan(self):
        angle=[]
        if (len(self.plan_list)==0): 
            show_message("이 날에는 아무런 계획이 없습니다")
        else: 
            i=0
            self.clock=self.canvas.create_oval(40, 40, 360, 360, fill="LightSkyBlue3")    #시계정의
            while(i<=len(self.plan_list)-1):    #시간표를 보여주는 부채꼴 생성
                angle=self.correct_angle(start_hour=self.plan_list[i]["start_time"]["hour"], start_minute=self.plan_list[i]["start_time"]["minute"], end_hour=self.plan_list[i]["end_time"]["hour"], end_minute=self.plan_list[i]["end_time"]["minute"])
                for_start=angle[0]
                for_extent=angle[1]
                self.planned_time[i]=self.canvas.create_arc(40, 40, 360, 360, start=for_start, extent=for_extent, fill="SteelBlue1")
                
                i+=1
