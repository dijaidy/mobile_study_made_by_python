from tkinter import *
import urllib.request
import sys
import os
from PIL import ImageTk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from information_management import api_loading


# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)

api_loading_source = api_loading.API_loading()


class start_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("MOBILE STUDY")
        self.window.geometry("400x800")

        # 타이틀 설정
        self.title = Label(self.window, text="MOBILE\nSTUDY", font=title_font)
        self.title.place(relx=0, relwidth=1, rely=0, height=150)

        # 메뉴 버튼 설정
        self.menu_내교재찜하기 = Button(
            self.window,
            text="내 교재 찜하기",
            font=("배달의민족 주아", 10),
            command=self.show_내교재찜하기_submenu,
        )
        self.menu_내교재찜하기.place(y=150, height=50, relx=0, relwidth=1 / 5)

        self.menu_공부계획 = Button(
            self.window, text="공부 계획", font=menu_font, command=self.show_공부계획_submenu
        )
        self.menu_공부계획.place(y=150, height=50, relx=1 / 5, relwidth=1 / 5)

        self.menu_공부방 = Button(
            self.window, text="공부방", font=menu_font, command=self.show_공부방_submenu
        )
        self.menu_공부방.place(y=150, height=50, relx=2 / 5, relwidth=1 / 5)

        self.menu_커뮤니티 = Button(
            self.window, text="커뮤니티", font=menu_font, command=self.show_커뮤니티_submenu
        )
        self.menu_커뮤니티.place(y=150, height=50, relx=3 / 5, relwidth=1 / 5)

        self.menu_현재성과 = Button(
            self.window, text="현재성과", font=menu_font, command=self.show_현재성과_submenu
        )
        self.menu_현재성과.place(y=150, height=50, relx=4 / 5, relwidth=1 / 5)

        # sub_menu 기본설정
        self.sub_menu_1 = Button(
            self.window, text="교재선택 >", font=submenu_font, command=self.show_교재선택_window
        )
        self.sub_menu_2 = Button(
            self.window, text="찜한교재현황 >", font=submenu_font, command=self.show_교재선택_window
        )
        self.sub_menu_1.place(y=400, height=50, relx=0, relwidth=2 / 5)
        self.sub_menu_2.place(y=470, height=50, relx=0, relwidth=2 / 5)

        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    # sub_menu_띄우는 함수 + sub_menu 해당 윈도우 띄우는 함수
    def show_내교재찜하기_submenu(self):
        self.sub_menu_1["text"] = "교재선택 >"
        self.sub_menu_2["text"] = "찜한교재현황 >"
        self.sub_menu_1["command"] = self.show_교재선택_window
        self.sub_menu_2["command"] = self.show_찜한교재현황_window

    def show_교재선택_window(self):
        교재선택_window()

    def show_찜한교재현황_window(self):
        찜한교재현황_window()

    def show_공부계획_submenu(self):
        self.sub_menu_1["text"] = "공부계획 >"
        self.sub_menu_2["text"] = ""
        self.sub_menu_1["command"] = self.show_공부계획_window
        self.sub_menu_2["command"] = ""

    def show_공부계획_window(self):
        공부계획_window()

    def show_공부방_submenu(self):
        self.sub_menu_1["text"] = "오늘의 공부 >"
        self.sub_menu_2["text"] = "학교 수업 복습 >"
        self.sub_menu_1["command"] = self.show_오늘의공부_window
        self.sub_menu_2["command"] = self.show_학교수업복습_window

    def show_오늘의공부_window(self):
        오늘의공부_window()

    def show_학교수업복습_window(self):
        학교수업복습_window()

    def show_커뮤니티_submenu(self):
        self.sub_menu_1["text"] = "스터디 그룹 >"
        self.sub_menu_2["text"] = "학교정보 >"
        self.sub_menu_1["command"] = self.show_스터디그룹_window
        self.sub_menu_2["command"] = self.show_학교정보_window

    def show_스터디그룹_window(self):
        스터디그룹_window()

    def show_학교정보_window(self):
        학교정보_window()

    def show_현재성과_submenu(self):
        self.sub_menu_1["text"] = "나의 성취도 >"
        self.sub_menu_2["text"] = "랭킹 >"
        self.sub_menu_1["command"] = self.show_나의성취도_window
        self.sub_menu_2["command"] = self.show_랭킹_window

    def show_나의성취도_window(self):
        나의성취도_window()

    def show_랭킹_window(self):
        랭킹_window()


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

        os.system("curl " + url + " > sources\교재선택_image_file.jpg")

        image = ImageTk.PhotoImage(
            file="sources\교재선택_image_file.jpg", master=self.window
        )  # 새창에서 그림띄우면 마스터 정의 꼭!

        self.book.config(image=image)
        self.window.mainloop()


class 찜한교재현황_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("찜한교재현황")
        self.window.geometry("400x800")


class 공부계획_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("공부계획")
        self.window.geometry("400x800")


class 오늘의공부_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("오늘의공부")
        self.window.geometry("400x800")


class 학교수업복습_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("학교수업복습")
        self.window.geometry("400x800")


class 스터디그룹_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("스터디그룹")
        self.window.geometry("400x800")


class 학교정보_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("학교정보")
        self.window.geometry("400x800")


class 나의성취도_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("나의성취도")
        self.window.geometry("400x800")


class 랭킹_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("랭킹")
        self.window.geometry("400x800")


if __name__ == "__main__":
    start_window()
else:
    print("임포트 되어 사용 됨:", __name__)
