from tkinter import *

# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)


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
    def __init__(self):
        # 창 설정
        window = Tk()
        window.title("교재선택")
        window.geometry("400x800")


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


start_window()
