# 교재선택_window
from tkinter import *
import urllib.request
import sys
import os
from PIL import ImageTk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from information_management import api_loading
from start_window import title_font, menu_font, submenu_font, api_loading_source


# sub_menu 윈도우
class 교재선택_window:
    image_index = 0

    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("교재선택")
        self.window.geometry("400x800")

        self.book_title_key = 0  # 책정보 딕션너리의 key를 keys()함수로 리스트로 만든 것에 쓰이는 인덱스값

        # 검색어입력창
        self.search_entry = Entry(self.window, font=menu_font)
        self.search_entry.place(relx=0, relwidth=4 / 5, rely=0, height=50)

        # 검색하기 버튼
        self.search_button = Button(
            self.window, text="검색하기", font=menu_font, command=lambda: self.show_book_information(0)
        )
        self.search_button.place(relx=4 / 5, relwidth=1 / 5, rely=0, height=50)

        # 다음 검색결과 보기 버튼
        self.next_button = Button(
            self.window,
            text="다음 검색결과 보기",
            font=menu_font,
            command=lambda: self.show_book_information(1),
        )
        self.next_button.place(relx=1 / 2, relwidth=1 / 2, y=800 - 50, height=50)

        # 이전 검색결과 보기 버튼
        self.prior_button = Button(
            self.window,
            text="이전 검색결과 보기",
            font=menu_font,
            command=lambda: self.show_book_information(-1),
        )
        self.prior_button.place(relx=0, relwidth=1 / 2, y=800 - 50, height=50)

        # 내 교재 찜하기 버튼
        self.choose_my_textbook = Button(self.window, text="내 교재 찜하기", font=menu_font)
        self.choose_my_textbook.place(relx=0, relwidth=1, y=800 - 100, height=50)

        #

        # 교재 이미지
        self.book = Label(self.window)
        self.book.place(relx=0, y=50, height=(800 - 50) - 100, relwidth=1)

        # 학교수업복습에 사용할 거
        # for subject, id in api_loading_source.return_subject_id().items():
        #    print("Key:%s\tValue:%s" % (subject, id))

        # 루프
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def bring_keyword(self):  # 검색어 입력창에서 받은 입력어 반환
        keyword = self.search_entry.get()
        return keyword

    def show_book_information(self, index_moving=0):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 검색 결과 책 모음 가져오기
        searching_result = api_loading_source.load_aladin_book(self.bring_keyword())

        # 인덱스 조정
        교재선택_window.image_index += index_moving
        if 교재선택_window.image_index < -1 * len(searching_result):
            교재선택_window.image_index + len(searching_result)
        elif 교재선택_window.image_index >= len(searching_result):
            교재선택_window.image_index - len(searching_result)

        # 책제목 리스트
        title_list = list(searching_result.keys())

        #

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        url = searching_result[title_list[교재선택_window.image_index]]["cover"]

        os.system("curl " + url + " > image_sources\교재선택_image_file.jpg")

        image = ImageTk.PhotoImage(
            file="image_sources\교재선택_image_file.jpg", master=self.window
        )  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book.config(image=image)
        self.window.mainloop()
