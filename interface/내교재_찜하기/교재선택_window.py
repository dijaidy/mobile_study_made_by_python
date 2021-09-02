# 교재선택_window
from tkinter import *
import urllib.request
import sys
import os
from PIL import Image, ImageTk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.api_loading import API_loading

# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)

api_loading_source = API_loading()


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

        # 교재 이미지
        self.book_image = Label(self.window)
        self.book_image.place(x=25, y=75, height=250, width=200)

        # 교재 타이틀
        self.book_title = Label(self.window, font=submenu_font)
        self.book_title.place(x=250)

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

        # 이미지 크기 조정
        size_adjusting_image = Image.open("image_sources\교재선택_image_file.jpg")
        image = size_adjusting_image.resize(
            (size_adjusting_image.size[0] * 2, size_adjusting_image.size[1] * 2), Image.ANTIALIAS
        )

        resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book.config(image=resized_image)
        self.window.mainloop()
