from tkinter import *

window = Tk()

window.title("MOBILE_STUDY")
window.geometry("400x800")

# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)


class start_scene:
    def __init__(self):
        # 타이틀 설정
        title = Label(window, text="MOBILE\nSTUDY", font=title_font)
        title.place(relx=0, relwidth=1, rely=0, height=150)

        # 버튼 설정
        menu_내교재찜하기 = Button(window, text="내 교재 찜하기", font=("배달의민족 주아", 10))
        menu_내교재찜하기.place(y=150, height=50, relx=0, relwidth=1 / 5)
        내교재찜하기_submenu = ["교재선택", "찜한교재현황"]
        menu_공부계획 = Button(window, text="공부 계획", font=menu_font)
        menu_공부계획.place(y=150, height=50, relx=1 / 5, relwidth=1 / 5)
        공부계획_submenu = ["공부계획"]
        menu_공부방 = Button(window, text="공부방", font=menu_font)
        menu_공부방.place(y=150, height=50, relx=2 / 5, relwidth=1 / 5)
        공부방_submenu = ["오늘의 공부", "학교수업복습"]
        menu_커뮤니티 = Button(window, text="커뮤니티", font=menu_font)
        menu_커뮤니티.place(y=150, height=50, relx=3 / 5, relwidth=1 / 5)
        커뮤니티_submenu = ["스터디 그룹", "학교정보"]
        menu_현재성과 = Button(window, text="현재성과", font=menu_font)
        menu_현재성과.place(y=150, height=50, relx=4 / 5, relwidth=1 / 5)
        현재성과_submenu = ["나의 성취도", "랭킹"]

        window.resizable(width=False, height=False)
        window.mainloop()

    def show_내교재찜하기_submenu():
        pass


start_scene()
