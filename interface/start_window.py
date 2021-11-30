from tkinter import *
import urllib.request
import sys
import os
import time
import json




sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from information_management.api_loading import API_loading

from 내교재_찜하기.교재선택_window import 교재선택_window
from 내교재_찜하기.찜한교재목록_window import 찜한교재목록_window
from 공부계획.공부계획_window import 공부계획_window
from 공부방.오늘의공부_window import 오늘의공부_window
from 공부방.학교수업복습_window import 학교수업복습_window
from 커뮤니티.스터디그룹_window import 스터디그룹_window
from 커뮤니티.유저정보_window import 학교정보_window
from 나의성과.학습통계_window import 학습통계_window
from 나의성과.랭킹_window import 랭킹_window

from login_window import Login_window


# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)


class start_window:
    def __init__(self):
        # 로그인 창
        login = Login_window()



        # 창 설정
        self.window = Tk()
        self.window.title("MOBILE STUDY")
        self.window.geometry("400x800")
        
        self.window.resizable(width=False, height=False)

        # 닉네임
        self.nickname = str(login)
        if self.nickname == '':
            self.window.destroy()
            return

        # 타이틀 설정
        self.title = Label(self.window, text="MOBILE\nSTUDY", font=title_font)
        self.title.place(relx=0, relwidth=1, rely=0, height=170)

        # 닉네임 표시
        self.nickname_label = Label(self.window, text='%s님 환영합니다' % self.nickname, font=('배달의민족 주아', 15), fg='blue')
        self.nickname_label.pack(side=TOP, anchor=E, padx=10, pady=5)

        # 파일 불러오기
        # 찜한 교재 목록
        with open(r'information\users_information_file.json', 'r', encoding='UTF-8') as in_file:
            with open(r'information\chosen_book_file.json', 'w', encoding='UTF-8') as out_file:
                self.users_information = json.load(in_file)
                if self.users_information == None:
                    self.users_information = {}
                file_content = self.users_information[self.nickname]["chosen_book_file"]
                json.dump(file_content, out_file, ensure_ascii=False)

        # 계획표
        with open(r'information\plan_list_file.json', 'w', encoding='UTF-8') as out_file:
            file_content = self.users_information[self.nickname]['plan_list_file']
            json.dump(file_content, out_file, ensure_ascii=False)

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
            self.window, text="커뮤니티", font=menu_font, fg="grey", command=self.show_커뮤니티_submenu
        )
        self.menu_커뮤니티.place(y=150, height=50, relx=3 / 5, relwidth=1 / 5)

        self.menu_현재성과 = Button(
            self.window, text="나의 성과", font=menu_font, fg='grey', command=self.show_현재성과_submenu
        )
        self.menu_현재성과.place(y=150, height=50, relx=4 / 5, relwidth=1 / 5)

        # sub_menu 기본설정
        self.sub_menu_1 = Button(
            self.window, text="교재선택 >", font=submenu_font, command=self.show_교재선택_window
        )
        self.sub_menu_2 = Button(
            self.window, text="찜한교재목록 >", font=submenu_font, command=self.show_찜한교재목록_window
        )
        self.sub_menu_1.place(y=400, height=50, relx=0, relwidth=2 / 5)
        self.sub_menu_2.place(y=470, height=50, relx=0, relwidth=2 / 5)

        self.log_out_button = Button(self.window, text='로그 아웃', font=submenu_font, command=self.log_out)
        self.log_out_button.place(x=260, y=710, width=100, height=50)

        self.window.mainloop()

        # 파일 저장하기
        with open(r'information\users_information_file.json', 'w', encoding='UTF-8') as out_file:
            with open(r'information\chosen_book_file.json', 'r', encoding='UTF-8') as in_file1:
                with open(r'information\plan_list_file.json', 'r', encoding='UTF-8') as in_file2:
                    self.users_information[self.nickname]['chosen_book_file'] = json.load(in_file1)
                    self.users_information[self.nickname]['plan_list_file'] = json.load(in_file2)
                    json.dump(self.users_information, out_file, ensure_ascii=False)






    # sub_menu_띄우는 함수 + sub_menu 해당 윈도우 띄우는 함수
    def show_내교재찜하기_submenu(self):
        self.sub_menu_1["text"] = "교재선택 >"
        self.sub_menu_2["text"] = "찜한교재목록 >"
        self.sub_menu_1["command"] = self.show_교재선택_window
        self.sub_menu_2["command"] = self.show_찜한교재목록_window
        self.sub_menu_1["fg"] = "black"
        self.sub_menu_2["fg"] = "black"

    def show_교재선택_window(self):
        교재선택_window()

    def show_찜한교재목록_window(self):
        찜한교재목록_window()

    def show_공부계획_submenu(self):
        self.sub_menu_1["text"] = "공부계획 >"
        self.sub_menu_2["text"] = ""
        self.sub_menu_1["command"] = self.show_공부계획_window
        self.sub_menu_2["command"] = ""
        self.sub_menu_1["fg"] = "black"
        self.sub_menu_2["fg"] = "black"

    def show_공부계획_window(self):
        공부계획_window()

    def show_공부방_submenu(self):
        self.sub_menu_1["text"] = "오늘의 공부 >"
        self.sub_menu_2["text"] = "학교 수업 복습 >"
        self.sub_menu_1["command"] = self.show_오늘의공부_window
        self.sub_menu_2["command"] = self.show_학교수업복습_window
        self.sub_menu_1["fg"] = "black"
        self.sub_menu_2["fg"] = "black"

    def show_오늘의공부_window(self):
        오늘의공부_window()

    def show_학교수업복습_window(self):
        학교수업복습_window(self.nickname)

    def show_커뮤니티_submenu(self):
        self.sub_menu_1["text"] = "스터디 그룹 >"
        self.sub_menu_2["text"] = "유저 정보 >"
        self.sub_menu_1["command"] = self.show_스터디그룹_window
        self.sub_menu_2["command"] = self.show_학교정보_window
        self.sub_menu_1["fg"] = "grey"
        self.sub_menu_2["fg"] = "grey"

    def show_스터디그룹_window(self):
        스터디그룹_window()

    def show_학교정보_window(self):
        학교정보_window()

    def show_현재성과_submenu(self):
        self.sub_menu_1["text"] = "학습 통계 >"
        self.sub_menu_2["text"] = "랭킹 >"
        self.sub_menu_1["command"] = self.show_학습통계_window
        self.sub_menu_2["command"] = self.show_랭킹_window
        self.sub_menu_1["fg"] = "grey"
        self.sub_menu_2["fg"] = "grey"

    def show_학습통계_window(self):
        학습통계_window()

    def show_랭킹_window(self):
        랭킹_window()
    
    def log_out(self):
        self.window.destroy()
        start_window()


# sub_menu 윈도우 모두 모듈화시킴

if __name__ == "__main__":
    start_window()
else:
    print("임포트 되어 사용 됨:", __name__)
