from tkinter import *
import sys
import os
from multiprocessing import Process, process
import time

sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.user_information import 공부계획_manage_user_information
from interface.공부계획.알리미_window import show_message
from PIL import Image
from PIL import ImageTk

x={"hour":0, "minute":0, "second":0}

class 오늘의공부_window(공부계획_manage_user_information):
    def __init__(self):
        super(오늘의공부_window, self).__init__()
        
        if len(self.plan_list_for_month[self.return_present_time().tm_yday])==0:
            show_message("오늘은 아무런 계획이 없습니다")
            return
        # 창 설정
        self.window = Tk()
        self.window.title("오늘의공부")
        self.window.geometry("400x800")
        self.window.resizable(False, False)

        #자료 생성
        self.studied_time={"hour" : 0, "minute": 0, "second" : 0} #총 공부시간
        self.late_time={"late" : {"color": "LightGoldenrod2", "text": "Too late"}, "finish" : {"color": "SpringGreen3", "text": "분 소요"}, "yet" : {"color" : "DarkSlateGray2", "text": "공부시작"}}
        
        self.go_to_timer=Button(self.window, font=("배달의민족 주아", 13), text="")     #늦었으면 Too late, 제대로 끝냈으면 nn분 소요, 아직 하기 전이면 공부시작으로 나타냄.
        self.go_to_timer.place(relx=1/3, y=750, relwidth=1/3, height=50)

        # 교재 타이틀
        self.book_title = Message(self.window, font=("배달의민족 주아", 12), text="계획이 없습니다")
        self.book_title.place(x=25, y=30, height=80, width=200)

        # 교재 이미지
        self.book_image = Label(self.window, borderwidth=2, relief="sunken")
        self.book_image.place(x=25, y=120, height=250, width=200)

        # 현재 위치/책 전체 개수
        self.searching_order = Label(self.window, font=("배달의민족 주아", 12), text="  /  ")
        self.searching_order.place(x=250, y=125, width=125, height=50)

        #총 공부한 시간 보여주기
        self.show_studied_time=Label(self.window, text="총 공부시간: "+str(self.studied_time["hour"])+":"+str(self.studied_time["minute"])+":"+str(self.studied_time["second"]), font=("배달의민족 주아", 15))
        self.show_studied_time.place(x=0, y=0, width=1, relheight=1/8)

        #이전 교재 보여주기 버튼
        self.prior_button = Button(self.window, text = "이전 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book_information(index_moving = -1))
        self.prior_button.place(relx = 0, y = 750, height = 50, relwidth = 1/3)

        #다음 교재 보여주기 버튼
        self.next_button = Button(self.window, text = "다음 교재로 가기", font = ("배달의민족 주아", 10), command = lambda: self.show_book_information(index_moving = 1))
        self.next_button.place(relx = 2/3, y = 750, height = 50, relwidth = 1/3)

        #계획한 시간대 보여주기
        self.time_label=Label(self.window, font=("배달의민족 주아", 12), text=" \n ~ \n ")
        self.time_label.place(x=250, y=200, width=125, height=125)

        #인덱스 초기화
        self.book_index=0

        self.show_book_information()    #책 정보보여줌

    
        # 루프
        self.window.mainloop()
        self.window.resizable(width=False, height=False)

    def show_book_information(self, index_moving=0):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 찜한 책 모음 가져오기
        searching_result = self.plan_list_for_month[self.return_present_time().tm_yday]

        # 인덱스 조정
        if self.book_index == 0 and index_moving == (-1):
            self.book_index = len(searching_result) - 1
        elif self.book_index < len(searching_result) - 1:
            self.book_index += index_moving
        elif self.book_index >= len(searching_result) - 1:
            self.book_index = 0
        # 책제목 리스트
        title_list = []
        for i in range(0, len(searching_result)):
            title_list.append(list(searching_result[i].keys())[0])

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        self.present_book = searching_result[self.book_index]
        self.present_book_title = title_list[self.book_index]
        cover_url = self.present_book[self.present_book_title]["cover"]
        os.system("curl " + cover_url + " > image_sources\교재선택_image_file.jpg")
        # 이미지 크기 조정
        size_adjusting_image = Image.open("image_sources\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (200, 250), Image.ANTIALIAS
        )

        resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book_image.config(image=resized_image)
            
        # 타이틀 수정
        book_title_text = title_list[self.book_index]
        self.book_title.config(text=book_title_text)

        if int(self.present_book["start_time"]["hour"]+self.present_book["start_time"]["minute"])<self.return_present_time().tm_hour*100+self.return_present_time().tm_min:
            if self.present_book["achievement"]==0:
                self.change_background_color("late")
            else:
                self.change_background_color("finish")
        else:
            self.change_background_color("yet")

        # 인덱스 수정
        searching_order_text = "%s / %s" % (self.book_index + 1, len(searching_result))
        self.searching_order.config(text=searching_order_text)

        self.window.mainloop()

    def start_study(self, time_left):
        if time_left=="yet":
            오늘의공부_공부중_window(studied_time=self.studied_time, book_dictionary=self.present_book)
            self.studied_time["hour"]+=x["hour"]
            self.studied_time["minute"]+=x["minute"]
            self.studied_time["second"]+=x["second"]
            self.present_book["achievement"]=x["hour"]*60+x["minute"]
        else:
            show_message("이미 늦었거나 완료한 계획입니다")
            return

    def change_background_color(self, time_left):
        self.go_to_timer.config(text=self.late_time[time_left]["text"], bg=self.late_time[time_left]["color"], command= lambda: self.start_study(time_left=time_left))
        self.window.config(bg=self.late_time[time_left]["color"])
        self.searching_order.config(bg=self.late_time[time_left]["color"])
        self.book_title.config(bg=self.late_time[time_left]["color"])
        self.next_button.config(bg=self.late_time[time_left]["color"])
        self.prior_button.config(bg=self.late_time[time_left]["color"])
        self.time_label.config(text=self.present_book["start_time"]["hour"]+":"+self.present_book["start_time"]["minute"]+"\n~\n"+self.present_book["end_time"]["hour"]+":"+self.present_book["end_time"]["minute"], bg=self.late_time[time_left]["color"])


class 오늘의공부_공부중_window():
    def __init__(self, studied_time, book_dictionary):

        # 창 설정
        self.window = Tk()
        self.window.title("오늘의공부_공부중")
        self.window.geometry("400x800")
        self.window.config(bg='black')

        #전역변수 초기화
        x={"hour":0, "minute":0, "second":0}

        #자료 정의
        self.chdrhdqntlrks=studied_time
        self.ryworhdqntlrks={"hour":0, "minute":0, "second":0}
        self.wlqwndtlrks={"hour":0, "minute":0, "second":0}

        #총 공부시간
        self.show_chdrhdqntlrks=Message(self.window, font=("배달의민족 주아", 20), text="총 공부시간\n"+str(self.chdrhdqntlrks["hour"])+":"+str(self.chdrhdqntlrks["minute"])+":"+str(self.chdrhdqntlrks["second"]), bg='black', fg='white', anchor="center", justify='center')
        self.show_chdrhdqntlrks.place(x=100, y=0, width=200, height=80)

        #교재 공부시간
        self.show_ryworhdqntlrks=Message(self.window, font=("배달의민족 주아", 15), text="교재 공부시간\n"+str(self.ryworhdqntlrks["hour"])+":"+str(self.ryworhdqntlrks["minute"])+":"+str(self.ryworhdqntlrks["second"]), bg='black', fg='green', anchor="center", justify='center')
        self.show_ryworhdqntlrks.place(x=0, y=80, width=200, height=70)

        #집중시간
        self.show_wlqwndtlrks=Message(self.window, font=("배달의민족 주아", 15), text="집중시간\n"+str(self.ryworhdqntlrks["hour"])+":"+str(self.ryworhdqntlrks["minute"])+":"+str(self.ryworhdqntlrks["second"]), bg='black', fg='red', anchor="center", justify='center')
        self.show_wlqwndtlrks.place(x=200, y=80, width=200, height=70)

        #교재 제목
        self.wpahr=Label(self.window, font=("배달의민족 주아", 10), text=list(book_dictionary.keys())[0], bg="SteelBlue1")
        self.wpahr.place(x=0, y=180, width=400, height=40)

        #교재 표지
        self.vywl=Label(self.window)
        size_adjusting_image = Image.open("image_sources\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (300, 450), Image.ANTIALIAS
        )
        resized_image = ImageTk.PhotoImage(image, master = self.window)  # 새창에서 그림띄우면 마스터 정의 꼭
        self.vywl.config(image=resized_image, text="")
        self.vywl.place(x=50, y=250, width=300, height=450)

        #완전정지버튼
        self.dhkswjswjdwl=Button(self.window, font=("배달의민족 주아", 15), text="공부완료", command= lambda: x==self.ryworhdqntlrks)    #x=self.ryworhdqntlrks과 같은 기능임. 수정하지 말 것
        self.dhkswjswjdwl.place(y=700, x=290, height=100, width=110)
        p1=Process(target=self.count_time(book_dictionary))
        p2=Process(target=lambda:self.window.mainloop())

        p1.start()
        p2.start()
        p1.join()
        p2.join()


    def count_time(self, book_dictionary):
        if x!={"hour":0, "minute":0, "second":0}:
            return
        while (int(공부계획_manage_user_information.return_present_time(self).tm_hour)*60+int(공부계획_manage_user_information.return_present_time(self).tm_min)<int(book_dictionary["end_time"]["hour"]*60)+int(book_dictionary["end_time"]["minute"])):
            self.show_ryworhdqntlrks.config(text="교재 공부시간\n"+str(self.ryworhdqntlrks["hour"])+":"+str(self.ryworhdqntlrks["minute"])+":"+str(self.ryworhdqntlrks["second"]))
            self.plus_second(self.wlqwndtlrks)
            self.show_wlqwndtlrks.config(text="집중시간\n"+str(self.ryworhdqntlrks["hour"])+":"+str(self.ryworhdqntlrks["minute"])+":"+str(self.ryworhdqntlrks["second"]))
            self.plus_second(self.chdrhdqntlrks)
            self.show_chdrhdqntlrks.config(text="총 공부시간\n"+str(self.chdrhdqntlrks["hour"])+":"+str(self.chdrhdqntlrks["minute"])+":"+str(self.chdrhdqntlrks["second"]))
            time.sleep(1)
    def end_code(self):
        x==self.ryworhdqntlrks
        self.window.destroy()    

    def plus_second(self, objective):
        objective["second"]+=1
        if objective["second"]>=60:
            objective["minute"]+=1
            objective["second"]-=60
            if objective["minute"]>=60:
                objective["hour"]+=1
                objective["minute"]-=60
