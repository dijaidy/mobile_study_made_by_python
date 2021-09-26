from tkinter import *
from tkinter import ttk as tk
import sys
import os
import json
from PIL import Image, ImageTk
import webbrowser

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
        #찜한교재_manage_user_information 상속받기
        super().__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("찜한교재현황")
        self.window.geometry("400x800")

        #책 전체개수/현재 위치
        self.searching_order = Label(self.window, font=menu_font, text="  /  ")
        self.searching_order.place(x=250, y=30, width=125, height=50)
        
        #이전 교재 보여주기 버튼
        self.prior_button = Button(self.window, text = "이전 교재로 가기", font = menu_font, command = lambda: self.show_book_information(index_moving = -1, sort_standard = self.combobox1.get(self.combobox1.curselection()[0], self.combobox1.curselection()[0])[0]))
        self.prior_button.place(relx = 0, y = 750, height = 50, width = 200)

        #다음 교재 보여주기 버튼
        self.next_button = Button(self.window, text = "다음 교재로 가기", font = menu_font, command = lambda: self.show_book_information(index_moving = 1, sort_standard = self.combobox1.get(self.combobox1.curselection()[0], self.combobox1.curselection()[0])[0]))
        self.next_button.place(relx = 1/2, y = 750, height = 50, width = 200)

        #큰 분류기준선택버튼만들기
        self.sort_by_acheivement = Button(self.window, text = "성취도순 분류", font = ("배달의민족 주아", 11), command = lambda: self.init_checkbox(standard = "성취도순 분류"))
        self.sort_by_subject = Button(self.window, text = "과목별 분류", font = ("배달의민족 주아", 11), command = lambda: self.init_checkbox(standard = "과목별 분류"))
        self.sort_by_acheivement.place(x = 0, y = 0, height = 20, width = 80)
        self.sort_by_subject.place(x = 0, y = 20, height = 20, width = 80)

        #작은 분류체크박스만들기
        self.combobox1 = Listbox(self.window, selectmode = "extended", height = 0, width = 0)

        #최종확인버튼만들기
        self.showing_button = Button(self.window, text = "선택 완료", font = ("배달의민족 주아", 12), command = lambda: self.show_book_information(sort_standard = self.combobox1.get(self.combobox1.curselection()[0], self.combobox1.curselection()[0])[0]))
        self.showing_button.place(x = 300, y = 5)

        # 교재 이미지
        self.book_image = Label(self.window, borderwidth = 2, relief = "sunken", text = "자료 없음")
        self.book_image.place(x = 25, y = 120, height = 250, width = 200)

        # 교재 타이틀
        self.book_title = Message(self.window, font = title_font)
        self.book_title.place(x = 0, y = 350, height = 200, width = 400)

        # 교재 정보
        self.book_info = Label(self.window, font = menu_font, justify = LEFT, padx = 1, pady = 1)
        self.book_info.place(x = 25, y = 550, height = 150, width = 400 - 50)
        self.open_web_button = Button(
            self.window, font = menu_font, text = "교재\n웹사이트\n오픈", padx = 1, pady = 1
        )
        self.open_web_button.place(x = 250, y = 75, width = 125, height = 125)

        #성취도
        self.book_acheivement = DoubleVar()
        self.acheivement_bar = tk.Progressbar(self.window, maximum = 100, length = 175, variable = self.book_acheivement)
        self.acheivement_bar.place(x = 225, y = 230)

        #기타 인스턴스변수 생성
        self.book_index = 0
        self.present_book = {}
        self.present_book_title = ""

    #분류기준에 따른 체크박스 생성
    def init_checkbox(self, standard = ""):
        self.combobox1.delete(0, self.combobox1.size())
        if (standard == "과목별 분류"):
            self.values = ["국어", "수학", "영어", "사회", "역사", "과학", "기술.가정"]
            for i in range(0, 7):
                self.combobox1.insert(i, self.values[i])
            self.combobox1.place(width = 80, height = 115, x = 80, y = 0)
        elif (standard == "성취도순 분류"):
            self.values = ["0%~20%", "21%~40%", "41%~60%", "61%~80%", "81%~100%"]
            for i in range(0, 5):
                self.combobox1.insert(i, self.values[i])
            self.combobox1.place(width = 80, height = 115, x = 80, y = 0)
            

    def show_book_information(self, index_moving = 0, sort_standard = ""):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 찜한 책 모음 가져오기
        searching_result = {}
        chosen_book_keys = self.chosen_book_dict.keys()
        if sort_standard in ["국어", "수학", "영어", "사회", "역사", "과학", "기술.가정"]:
            for i in chosen_book_keys:
                if self.chosen_book_dict[i]["subject"] == sort_standard:
                    searching_result[i] = self.chosen_book_dict[i]
        elif sort_standard in ["0%~20%", "21%~40%", "41%~60%", "61%~80%", "81%~100%"]:
            for i in chosen_book_keys:
                if int(sort_standard.split('~')[0].replace("%", "")) <= self.chosen_book_dict[i]["acheivement"] <= int(sort_standard.split('~')[1].replace("%", "")):
                    searching_result[i] = self.chosen_book_dict[i]

        # 인덱스 조정
        if self.book_index == 0 and index_moving == (-1):
            self.book_index = len(searching_result)-1
        elif self.book_index < len(searching_result)-1:
            self.book_index += index_moving
        elif self.book_index >= len(searching_result)-1:
            self.book_index = 0
        # 책제목 리스트
        title_list = list(searching_result.keys())

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = searching_result[title_list[self.book_index]]
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

        # 정보 수정
        book_info_text = "가격: %s원" % book["priceStandard"]
        self.book_info.config(text = book_info_text)

        #인덱스 수정
        searching_order_text = "%s / %s" % (len(searching_result), self.book_index+1)
        self.searching_order.config(text=searching_order_text)

        self.open_web_button.config(command = lambda: webbrowser.open(book["link"]))

        self.window.mainloop()
