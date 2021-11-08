# 바꾼거
# 타이틀 설정


# 교재선택_window
import json
from tkinter import *
import tkinter
from types import CellType
from typing import List
import urllib.request
import sys
import os
from PIL import Image, ImageTk
import webbrowser

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.api_loading import API_loading
from information_management.user_information import 찜한교재_manage_user_information
from information_management.user_information import 과목_manage_user_information

# 폰트 설정
title_font = ("배달의민족 주아", 23)
submenu_font = ("배달의민족 주아", 17)
menu_font = ("배달의민족 주아", 15)

api_loading_source = API_loading()
찜한교재 = 찜한교재_manage_user_information()
과목 = 과목_manage_user_information()


# sub_menu 윈도우
class 교재선택_window(Tk):
    # 현재 띄워주는 책의 정보
    book_index = 0
    present_book_title = ""
    present_book = {}

    # 가져온 책들의 결과
    searching_result = {}
    searching_book_title_list = []
    book_count = 0

    def __init__(self):
        # 프레임
        self._frame = None

        # 창 설정
        self.window = Tk()
        self.window.title("교재 선택")
        self.window.geometry("400x800")

        # 검색어입력창
        self.search_entry = Entry(self.window, font=("배달의민족 주아", 15))
        self.search_entry.place(relx=0, relwidth=4 / 5, rely=0, height=50)

        # 검색하기 버튼
        self.search_button = Button(
            self.window, text="검색하기", font=menu_font, command=lambda: self.show_book_information(0)
        )
        self.search_button.place(relx=4 / 5, relwidth=1 / 5, rely=0, height=50)

        # 메인카테고리 텍스트
        self.main_category_text = Message(
            self.window,
            font=("배달의민족 주아", 12),
            justify=CENTER,
            anchor=CENTER,
            text="학년-참고서 종류",
            width=200,
        )
        self.main_category_text.place(x=0, y=60, width=200, height=20)

        # 서브카테고리 텍스트
        self.sub_category_text = Message(
            self.window, font=("배달의민족 주아", 12), justify=CENTER, anchor=CENTER, text="과목"
        )
        self.sub_category_text.place(x=200, y=60, width=200, height=20)

        # 카테고리 가져오기
        self.category_dict = {}  # 전 카테고리 딕셔너리
        with open("information\교재_카테고리_dict.json", "r", encoding="UTF-8") as in_file:
            self.category_dict = json.load(in_file)

        # 메인 카테고리 콤보박스
        self.main_category_keys = list(self.category_dict.keys())
        self.main_category_keys.insert(0, "전체")
        self.main_category_combobox = tkinter.ttk.Combobox(
            self.window, values=self.main_category_keys, state="readonly"
        )
        self.main_category_combobox.place(x=20, y=80, width=160, height=30)
        self.main_category_combobox.current(0)

        # 서브 카테고리 콤보박스
        self.sub_category_combobox = tkinter.ttk.Combobox(
            self.window, height=15, state="readonly", values=["전체"]
        )
        self.sub_category_combobox.place(x=220, y=80, width=160, height=30)
        self.sub_category_combobox.current(0)

        self.search_button.place(relx=4 / 5, relwidth=1 / 5, rely=0, height=50)

        # 검색 순서/전체 검색결과 텍스트
        self.searching_order = Label(self.window, font=menu_font, text="  /  ")
        self.searching_order.place(x=250, y=75, width=125, height=50)

        # 다음 검색결과 보기 버튼
        self.next_button = Button(
            self,
            text="다음 검색결과 보기",
            font=menu_font,
            command=lambda: self.show_next_book(),
        )
        self.next_button.place(relx=1 / 2, relwidth=1 / 2, y=800 - 50, height=50)

        # 이전 검색결과 보기 버튼
        self.prior_button = Button(
            self,
            text="이전 검색결과 보기",
            font=menu_font,
            command=lambda: self.show_prior_book(),
        )
        self.prior_button.place(relx=0, relwidth=1 / 2, y=800 - 50, height=50)

        # 내 교재 찜하기 버튼
        self.choose_my_textbook = Button(
            self, text="내 교재 찜하기", font=menu_font, command=self.choose_my_book
        )
        self.choose_my_textbook.place(relx=0, relwidth=1, y=800 - 100, height=50)

        # 교재 이미지

        # 메인 카테고리 설정시 동작하는 함수(서브카테고리 리스트 변경)
        def set_main_category(event):
            grade_type = self.main_category_combobox.get()
            subject = self.category_dict[grade_type]["item"]
            subject = list(subject.keys())
            subject.insert(0, "전체")
            self.sub_category_combobox["values"] = subject
            self.sub_category_combobox.current(0)

        self.main_category_combobox.bind("<<ComboboxSelected>>", set_main_category)

    def bring_keyword_and_CID(self):  # 검색어 입력창에서 받은 입력어 반환
        # 키워드 가져오기
        keyword = self.search_entry.get()
        # 카테고리 키 설정
        selected_main_category = self.main_category_combobox.get()
        selected_sub_category = self.sub_category_combobox.get()
        if selected_main_category == "전체":
            CID = 76000
        elif selected_sub_category == "전체":
            CID = self.category_dict[selected_main_category]["CID"]
        else:
            CID = self.category_dict[selected_main_category]["item"][selected_sub_category]
        return (keyword, CID)

        self.searching_order = Label(self, font=menu_font, text="  /  ")
        self.searching_order.place(x=250, y=125, width=125, height=50)

        self.book_image = Label(self, borderwidth=3, relief="ridge")
        self.book_image.place(x=25, y=125, height=188, width=150)

        # 이미지 크기 조정
        size_adjusting_image = Image.open("image_sources\교재미선택_이미지.png")
        image = size_adjusting_image.resize((200, 250), Image.ANTIALIAS)

        resized_image = ImageTk.PhotoImage(image, master=self)  # 새창에서 그림띄우면 마스터 정의 꼭!
        self.교재미선택_image = resized_image
        self.book_image.config(image=resized_image)

        # 교재 타이틀
        self.book_title = Message(
            self,
            font=("배달의민족 주아", 17),
            anchor=N,
            justify=CENTER,
            aspect=300,
        )
        self.book_title.place(x=0, y=330, height=250, width=400)

        # 교재 정보

        self.book_description = Message(
            self, font=("배달의민족 주아", 12), justify=LEFT, padx=10, anchor=NW, aspect=400
        )
        self.book_description.place(x=0, y=450, height=150, width=400)

        # 교재 출처
        self.book_link = Message(self, font=("배달의민족 주아", 15), justify=LEFT, anchor=NW, aspect=400)
        self.book_link.place(x=0, y=600, width=400, height=100)

        # 교재 웹사이트 오픈
        self.open_web_button = Button(self, font=menu_font, text="교재\n웹사이트\n오픈", padx=1, pady=1)
        self.open_web_button.place(x=250, y=175, width=125, height=125)

        # 링크

        # 학교수업복습에 사용할 거
        # for subject, id in api_loading_source.return_subject_id().items():
        #    print("Key:%s\tValue:%s" % (subject, id))

        # 루프

    def bring_keyword(self):  # 검색어 입력창에서 받은 입력어 반환
        keyword = self.search_entry.get()
        return keyword

    def show_book_information(self, index_moving=0):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 검색 결과 책 모음 가져오고, 저장하기
        searching_result = api_loading_source.load_aladin_book(self.bring_keyword())
        교재선택_window.searching_result = searching_result
        교재선택_window.searching_book_title_list = list(교재선택_window.searching_result.keys())
        교재선택_window.book_index = 0
        교재선택_window.book_count = len(교재선택_window.searching_result)

        # 책제목 리스트
        first_book_title = 교재선택_window.searching_book_title_list[0]

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = 교재선택_window.searching_result[first_book_title]
        교재선택_window.present_book_title = first_book_title
        교재선택_window.present_book = book
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
        self.book_title.config(text="제목: \n%s" % first_book_title)

        # 정보 수정
        book_link_text = book["link"]
        self.book_link.config(text="이미지 출처: \n%s" % book_link_text)

        if book["description"] != "":
            book_description_text = book["description"]
            self.book_description.config(text="교재 설명: \n%s" % book_description_text)
        else:
            self.book_description.config(text="교재 설명: \n해당 사이트에서 교재정보를 제공하지 않습니다.")

        # 링크 수정
        def open_web():
            webbrowser.open(book["link"])

        self.open_web_button.config(command=open_web)

        # 검색 순서 수정
        searching_order_text = "%s / %s" % (교재선택_window.book_index + 1, 교재선택_window.book_count)
        self.searching_order.config(text=searching_order_text)

        self.mainloop()

    # 이전 검색결과
    def show_prior_book(self):
        index_moving = -1

        if 교재선택_window.book_count == 0:
            return

        # 인덱스 조정
        교재선택_window.book_index += index_moving
        if 교재선택_window.book_index < 0:
            교재선택_window.book_index += 교재선택_window.book_count
        elif 교재선택_window.book_index >= 교재선택_window.book_count:
            교재선택_window.book_index -= 교재선택_window.book_count

            # 책제목 리스트
        book_title = 교재선택_window.searching_book_title_list[교재선택_window.book_index]

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = 교재선택_window.searching_result[book_title]
        교재선택_window.present_book_title = book_title
        교재선택_window.present_book = book
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
        self.book_title.config(text="제목: \n%s" % book_title)

        # 정보 수정
        book_link_text = book["link"]
        self.book_link.config(text="이미지 출처: \n%s" % book_link_text)

        book_description_text = book["description"]
        self.book_description.config(text="교재 설명: \n%s" % book_description_text)

        # 링크 수정
        def open_web():
            webbrowser.open(book["link"])

        self.open_web_button.config(command=open_web)

        # 검색 순서 수정
        searching_order_text = "%s / %s" % (교재선택_window.book_index + 1, 교재선택_window.book_count)
        self.searching_order.config(text=searching_order_text)

        self.window.mainloop()

    # 다음 검색결과
    def show_next_book(self):
        index_moving = 1

        # 인덱스 조정
        교재선택_window.book_index += index_moving
        if 교재선택_window.book_index < 0:
            교재선택_window.book_index += 교재선택_window.book_count
        elif 교재선택_window.book_index >= 교재선택_window.book_count:
            교재선택_window.book_index -= 교재선택_window.book_count

        if 교재선택_window.book_count == 0:
            return

            # 책제목 리스트
        book_title = 교재선택_window.searching_book_title_list[교재선택_window.book_index]

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = 교재선택_window.searching_result[book_title]
        교재선택_window.present_book_title = book_title
        교재선택_window.present_book = book
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
        self.book_title.config(text="제목: \n%s" % book_title)

        # 정보 수정
        book_link_text = book["link"]
        self.book_link.config(text="이미지 출처: \n%s" % book_link_text)

        book_description_text = book["description"]
        self.book_description.config(text="교재 설명: \n%s" % book_description_text)

        # 링크 수정
        def open_web():
            webbrowser.open(book["link"])

        self.open_web_button.config(command=open_web)

        # 검색 순서 수정
        searching_order_text = "%s / %s" % (교재선택_window.book_index + 1, 교재선택_window.book_count)
        self.searching_order.config(text=searching_order_text)

        self.window.mainloop()

    # 내교재 찜하기 버튼
    def choose_my_book(self):

        choose_option(교재선택_window.present_book_title, 교재선택_window.present_book)


class choose_option:
    subject_list = []
    subject_list = 과목.call_subject_list_from_file()
    present_book_title = ""
    present_book = ""

    def __init__(self, present_book_title, present_book):
        self.window = Tk()
        self.window.title("교재 선택 옵션")
        self.window.geometry("400x250")

        choose_option.present_book_title = present_book_title
        choose_option.present_book = present_book

        # 제목
        self.title = Label(self.window, text="교재 찜하기 옵션", font=submenu_font, justify=CENTER)
        self.title.place(x=5, y=10, width=390, height=40)

        # 과목
        self.subject = Label(self.window, text="과목", font=menu_font)
        self.subject.place(x=20, y=50, width=50, height=50)

        # 과목 리스트
        self.subject_listbox = Listbox(
            self.window, selectmode="single", height=0, exportselection=False
        )
        for i in range(0, len(choose_option.subject_list)):
            self.subject_listbox.insert(i, choose_option.subject_list[i])
        self.subject_listbox.place(x=100, y=50, width=100, height=100)

        # 과목 추가 버튼
        self.subject_add_button = Button(
            self.window,
            text="과목 추가",
            font=("배달의민족 주아", 12),
            justify=CENTER,
            command=lambda: self.add_subject(self.subject_to_add.get()),
        )
        self.subject_add_button.place(x=20, y=160, width=70, height=50)

        # 추가할 과목 이름
        self.subject_to_add = Entry(self.window, font=("배달의민족 주아", 12))
        self.subject_to_add.place(x=110, y=160, width=80, height=50)

        # 교재 종류(텍스트)
        self.book_type = Label(self.window, text="교재 종류", font=menu_font)
        self.book_type.place(x=200, y=50, width=100, height=50)

        # 교재 종류(입력)
        self.book_type_listbox = Listbox(
            self.window, selectmode="single", height=0, exportselection=False
        )
        i = 0
        for book_type in ["예습교재", "시험교재", "기타교재"]:
            self.book_type_listbox.insert(i, book_type)
            i += 1

        self.book_type_listbox.place(x=290, y=50, width=100, height=100)

        # 기타 교재 예시
        self.etc_book_type_example = Label(
            self.window, text="기타교재의 예시: 코딩 교재 등 \n교과목 외에 배우는 것", font=("배달의민족 주아", 10)
        )
        self.etc_book_type_example.place(x=210, y=150, width=200, height=50)

        # 확인 버튼
        self.confirm_button = Button(
            self.window,
            text="확인",
            font=("배달의민족 주아", 12),
            justify=CENTER,
            command=lambda: self.apply_option(
                self.subject_listbox.curselection(),
                self.book_type_listbox.curselection(),
            ),
        )

        self.confirm_button.place(x=330, y=200, width=70, height=50)

        self.cancel_button = Button(
            self.window,
            text="취소",
            font=("배달의민족 주아", 12),
            justify=CENTER,
            command=self.cancel_option_window,
        )
        self.cancel_button.place(x=260, y=200, width=70, height=50)

    def add_subject(self, subject):
        self.subject_listbox.insert(len(choose_option.subject_list), subject)
        choose_option.subject_list.append(subject)
        과목.update_subject(choose_option.subject_list)
        과목.save_subject_list_to_file()

    def apply_option(self, subject, book_type):
        if type(subject) == tuple and type(book_type) == tuple:
            subject = self.subject_listbox.get(subject)
            book_type = self.book_type_listbox.get(book_type)

        # 교재 정보 저장
        찜한교재.plus_chosen_book_dict(
            choose_option.present_book_title, choose_option.present_book, subject, book_type
        )
        찜한교재.save_chosen_book_to_file()
        self.window.destroy()

    def cancel_option_window(self):
        self.background = Label(self.window, relief=RIDGE, borderwidth=3)
        self.background.place(x=100, y=75, width=200, height=125)

        # 정말 취소 하시겠습니까?
        self.warning_widget_title = Label(
            self.window, text="정말 취소 하시겠습니까?", justify=CENTER, font=("배달의민족 주아", 10)
        )
        self.warning_widget_title.place(x=120, y=80, width=160, height=20)

        # 확인버튼

        self.sub_confirm_button = Button(
            self.window,
            text="확인",
            font=("배달의민족 주아", 12),
            justify=CENTER,
            command=lambda: self.window.destroy(),
        )
        self.sub_confirm_button.place(x=125, y=125, width=70, height=50)

        # 취소
        self.sub_cancel_button = Button(
            self.window,
            text="취소",
            font=("배달의민족 주아", 12),
            justify=CENTER,
            command=self.close_warning_widget,
        )
        self.sub_cancel_button.place(x=205, y=125, width=70, height=50)

    def close_warning_widget(self):
        self.warning_widget_title.place_forget()
        self.sub_cancel_button.place_forget()
        self.sub_confirm_button.place_forget()
        self.background.place_forget()


# 테스트
