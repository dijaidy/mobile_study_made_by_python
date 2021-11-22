from tkinter import *
from tkinter import ttk as tk
import sys
import os
import json
from PIL import Image, ImageTk
import webbrowser
import tkinter.ttk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.user_information import 찜한교재_manage_user_information

# 폰트 설정
title_font = ("배달의민족 주아", 23)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)


class 찜한교재목록_window(찜한교재_manage_user_information):
    def __init__(self):
        # 찜한교재_manage_user_information 상속받기
        super(찜한교재목록_window, self).__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("찜한교재현황")
        self.window.geometry("400x800")

        # 현재 위치/책 전체 개수
        self.searching_order = Label(self.window, font=menu_font, text="  /  ")
        self.searching_order.place(x=250, y=125, width=125, height=50)

        # 이전 교재 보여주기 버튼
        self.prior_button = Button(
            self.window,
            text="이전 교재로 가기",
            font=menu_font,
            command=lambda: self.show_book_information(
                index_moving=-1,
                sort_standard=self.combobox1.get(
                    self.combobox1.curselection()[0], self.combobox1.curselection()[0]
                )[0],
            ),
        )
        self.prior_button.place(relx=0, y=750, height=50, width=200)

        # 다음 교재 보여주기 버튼
        self.next_button = Button(
            self.window,
            text="다음 교재로 가기",
            font=menu_font,
            command=lambda: self.show_book_information(
                index_moving=1,
                sort_standard=self.combobox1.get(
                    self.combobox1.curselection()[0], self.combobox1.curselection()[0]
                )[0],
            ),
        )
        self.next_button.place(relx=1 / 2, y=750, height=50, width=200)

        # 검색어입력창
        self.search_entry = Entry(self.window, font=menu_font)
        self.search_entry.place(relx=0, relwidth=4 / 5, rely=0, height=50)

        # 검색하기 버튼
        self.search_button = Button(
            self.window, text="검색(필터)", font=('배달의민족 주아', 14), command=self.show_book_information
        )
        self.search_button.place(relx=4 / 5, relwidth=1 / 5, rely=0, height=50)

        # 과목분류_텍스트
        self.subject_sort_text = Message(
            self.window,
            font=("배달의민족 주아", 12),
            justify=CENTER,
            anchor=CENTER,
            text="과목",
            width=200,
        )
        self.subject_sort_text.place(x=0, y=60, width=200, height=20)

        # 성취도분류_텍스트
        self.achievement_sort_text = Message(
            self.window, font=("배달의민족 주아", 12), justify=CENTER, anchor=CENTER, text="성취도"
        )
        self.achievement_sort_text.place(x=200, y=60, width=200, height=20)

        # 카테고리 가져오기
        self.subject_list = []  # 전 카테고리 딕셔너리
        with open("information\subject_list_file.json", "r", encoding="UTF-8") as in_file:
            self.subject_list = json.load(in_file)['subject']

        # 과목분류 콤보박스
        self.subject_list.insert(0, '전체')
        self.subject_sort_combobox = tkinter.ttk.Combobox(
            self.window, values=self.subject_list, state="readonly"
        )
        self.subject_sort_combobox.place(x=20, y=80, width=160, height=30)
        self.subject_sort_combobox.current(0)

        #성취도 시작 범위 텍스트
        achievement_start_range_text = Label(self.window, font=('배달의민족 주아', 10), justify=CENTER, anchor=CENTER, text='시작 범위')
        achievement_start_range_text.place(x=200, y=80, width=100, height=20)
        #성취도 끝 범위 텍스트
        achievement_end_range_text = Label(self.window, font=('배달의민족 주아', 10), justify=CENTER, anchor=CENTER, text='끝 범위')
        achievement_end_range_text.place(x=300, y=80, width=100, height=20)

        # 성취도분류 조정
        self.achievement_start_value = StringVar(self.window)
        self.achievement_end_value = StringVar(self.window)
        achievement_start_value_list = [str(i) + '%' for i in range(0, 101, 5)]
        achievement_end_value_list = [str(i) + '%' for i in range(0, 101, 5)]

        self.achievement_start_spinbox = Spinbox(self.window, values=achievement_start_value_list, textvariable=self.achievement_start_value)
        self.achievement_start_spinbox.place(x=220, y=100, width=80, height=20)
        self.achievement_end_spinbox= Spinbox(self.window, values=achievement_end_value_list, textvariable=self.achievement_end_value)
        self.achievement_end_spinbox.place(x=300, y=100, width=80, height=20)
        self.achievement_start_value.set('0%')
        self.achievement_end_value.set('100%')


        self.achievement_start_spinbox.bind('<Button-1>', self.adjust_start_achievement)
        self.achievement_end_spinbox.bind('<Button-1>', self.adjust_end_achievement)
        self.achievement_start_spinbox.bind('<ButtonRelease-1>', self.adjust_start_achievement)
        self.achievement_end_spinbox.bind('<ButtonRelease-1>', self.adjust_end_achievement)

        self.book_frame = LabelFrame(self.window, width=380, height=650)
        self.book_frame.pack(side=TOP, pady=140, fill='x')

        # 교재 이미지
        self.book_image = Label(self.book_frame, borderwidth=2, relief="sunken", text="자료 없음", width=120, height=160)
        self.book_image.grid(row=1, column=0, rowspan=3)

        # 이미지 크기 조정
        size_adjusting_image = Image.open("ignore_image\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (120,160), Image.ANTIALIAS
        )

        resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book_image.config(image=resized_image, text="")

        # 교재 타이틀
        self.book_title = Message(self.book_frame, font=('배달의민족 주아', 14), text='타이틀테스트', anchor=N, justify=LEFT,width=265, background='skyblue')
        self.book_title.grid(row=0, column=0, columnspan=3, sticky=W)

        # 교재 정보
        self.book_info = Message(self.book_frame, font=('배달의민족 주아', 12), justify=LEFT, text='내용 테스트', width=265)
        self.book_info.grid(row=2, column=1, columnspan=2, sticky=W)
        #self.open_web_button = Button(
        #    self.window, font=menu_font, text="교재\n웹사이트\n오픈", padx=1, pady=1
        #)
        #self.open_web_button.place(x=250, y=175, width=125, height=125)

        # 성취도
        self.book_achievement = DoubleVar()
        self.achievement_bar = tk.Progressbar(
            self.book_frame, maximum=100, length=240, variable=self.book_achievement
        )
        self.achievement_bar.grid(row=3, column=1, sticky=S)
        self.achievement_bar.config(value=50)

        self.book_achievement_text = Message(self.book_frame, font=('배달의민족 주아', 8), justify=CENTER, text='성취도\n0%', width=40)
        self.book_achievement_text.grid(row=3, column=2, sticky=S)

        # 기타 인스턴스변수 생성
        #self.book_index = 0
        #self.present_book = {}
        #self.present_book_title = ""

        self.window.resizable(width=False, height=False)
        self.window.mainloop()
    
    def adjust_start_achievement(self, event):
        if int(self.achievement_start_value.get().replace('%', '')) >= int(self.achievement_end_value.get().replace('%', '')):
            self.achievement_start_value.set(str(int(self.achievement_end_value.get().replace('%', ''))-5)+'%')

    def adjust_end_achievement(self, event):
        if int(self.achievement_start_value.get().replace('%', '')) >= int(self.achievement_end_value.get().replace('%', '')):
            self.achievement_end_value.set(str(int(self.achievement_start_value.get().replace('%', ''))+5)+'%')




    # 분류기준에 따른 체크박스 생성
    def init_checkbox(self, standard=""):
        self.combobox1.delete(0, self.combobox1.size())
        if standard == "과목별 분류":
            self.values = ["국어", "수학", "영어", "사회", "역사", "과학", "기술.가정"]
            for i in range(0, 7):
                self.combobox1.insert(i, self.values[i])
            self.combobox1.place(width=80, height=115, x=80, y=0)
        elif standard == "성취도순 분류":
            self.values = ["0%~20%", "21%~40%", "41%~60%", "61%~80%", "81%~100%"]
            for i in range(0, 5):
                self.combobox1.insert(i, self.values[i])
            self.combobox1.place(width=80, height=115, x=80, y=0)

    def show_book_information(self, index_moving=0, sort_standard=""):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 찜한 책 모음 가져오기
        searching_result = {}                                   #수정
        chosen_book_keys = self.chosen_book_dict.keys()
        if sort_standard in ["국어", "수학", "영어", "사회", "역사", "과학", "기술.가정"]:
            for i in chosen_book_keys:
                if self.chosen_book_dict[i]["subject"] == sort_standard:
                    searching_result[i] = self.chosen_book_dict[i]
        elif sort_standard in ["0%~20%", "21%~40%", "41%~60%", "61%~80%", "81%~100%"]:
            for i in chosen_book_keys:
                if (
                    int(sort_standard.split("~")[0].replace("%", ""))
                    <= self.chosen_book_dict[i]["acheivement"]
                    <= int(sort_standard.split("~")[1].replace("%", ""))
                ):
                    searching_result[i] = self.chosen_book_dict[i]

        # 인덱스 조정
        if self.book_index == 0 and index_moving == (-1):
            self.book_index = len(searching_result) - 1
        elif self.book_index < len(searching_result) - 1:
            self.book_index += index_moving
        elif self.book_index >= len(searching_result) - 1:
            self.book_index = 0
        # 책제목 리스트
        title_list = list(searching_result.keys())      # 수정

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = searching_result[title_list[self.book_index]]
        self.present_book = book
        self.present_book_title = title_list[self.book_index]
        url = book["cover"]

        os.system("curl " + url + " > ignore_image\교재선택_image_file.jpg")

        # 이미지 크기 조정
        size_adjusting_image = Image.open("ignore_image\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (size_adjusting_image.size[0] * 2, size_adjusting_image.size[1] * 2), Image.ANTIALIAS
        )

        resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book_image.config(image=resized_image, text="")

        # 타이틀 수정
        book_title_text = title_list[self.book_index]
        self.book_title.config(text=book_title_text)

        # 정보 수정
        book_info_text = "가격: %s원" % book["priceStandard"]
        self.book_info.config(text=book_info_text)

        # 인덱스 수정
        searching_order_text = "%s / %s" % (len(searching_result), self.book_index + 1)
        self.searching_order.config(text=searching_order_text)

        self.open_web_button.config(command=lambda: webbrowser.open(book["link"]))

        self.window.mainloop()
