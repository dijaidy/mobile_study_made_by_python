from tkinter import *
import sys
import os
import json


# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)


class Login_window:
    def __init__(self):

        # 창 설정
        self.window = Tk()
        self.window.title("Login 창")
        self.window.geometry("400x400")
        self.window.resizable(width=False, height=False)

        # 타이틀 설정
        self.login = Label(self.window, text="MOBILE STUDY\n로그인창", font=title_font)
        self.login.pack(side=TOP, anchor=N, fill=X, ipady=10)
        
        # 닉네임설정
        self.nickname_text = Label(self.window, text='닉네임', font=menu_font, fg='gray', padx=50)
        self.nickname_text.pack(side=TOP, anchor=NW)

        self.nickname = Entry(self.window, font=submenu_font)
        self.nickname.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)

        # 비밀번호 설정
        self.password_text = Label(self.window, text='비밀번호', font=menu_font, fg='gray', padx=50)
        self.password_text.pack(side=TOP, anchor=NW, pady=(25, 0))

        self.password = Entry(self.window, font=submenu_font)
        self.password.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)
        
        # 로그인
        self.login_button = Button(self.window, font=('배달의민족 주아', 17), text='로그인', anchor=CENTER, command=lambda:self.login(self.nickname.get(),self.password.get()))
        self.login_button.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(20, 0))

        # 회원가입
        self.sign_in_button = Button(self.window, text='회원가입', font=('배달의민족 주아', 10), fg='gray', overrelief=FLAT, relief=FLAT, command=self.go_into_sign_in)
        self.sign_in_button.pack(side=TOP, anchor=NE, pady=(3, 0), padx=50)

        
        self.window.mainloop()

    #회원가입 함수
    def go_into_sign_in(self):

        # 창 설정
        self.sign_in_window = Tk()
        self.sign_in_window.title("회원가입 창")
        self.sign_in_window.geometry("400x600")
        self.sign_in_window.resizable(width=False, height=False)

        # 타이틀 설정
        sign_in = Label(self.sign_in_window, text="MOBILE STUDY\n회원가입 창", font=title_font)
        sign_in.pack(side=TOP, anchor=N, fill=X, ipady=10)
        
        # 닉네임설정
        nickname_text = Label(self.sign_in_window, text='닉네임', font=menu_font, fg='gray', padx=50)
        nickname_text.pack(side=TOP, anchor=NW)

        nickname = Entry(self.sign_in_window, font=submenu_font)
        nickname.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)

        # 비밀번호 설정
        password_text = Label(self.sign_in_window, text='비밀번호', font=menu_font, fg='gray', padx=50)
        password_text.pack(side=TOP, anchor=NW, pady=(20, 0))

        password = Entry(self.sign_in_window, font=submenu_font)
        password.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)

        # 비밀번호 확인
        password_check_text = Label(self.sign_in_window, text='비밀번호 확인', font=menu_font, fg='gray', padx=50)
        password_check_text.pack(side=TOP, anchor=NW, pady=(20, 0))

        password_check = Entry(self.sign_in_window, font=submenu_font)
        password_check.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)

        # 프레임(내용: 소속학교, 학년, 반)
        frame = Frame(self.sign_in_window)
        frame.pack(side=TOP, fill=BOTH, pady=(20, 0), padx=20)

        # 소속학교
        school_text = Label(frame, text='소속학교', font=menu_font, fg='gray')
        school_text.grid(row=0, column=0, sticky=W)

        school = Entry(frame, font=submenu_font, width=12)
        school.grid(row=1, column=0, padx=(0, 10))
        
        # 학년
        grade_text = Label(frame, text='학년', font=menu_font, fg='gray')
        grade_text.grid(row=0, column=1, sticky=W)

        grade = Entry(frame, font=submenu_font, width=6)
        grade.grid(row=1, column=1, padx=(0, 10))

        # 반
        class_text = Label(frame, text='반', font=menu_font, fg='gray', padx=10 , anchor=W)
        class_text.grid(row=0, column=2, sticky=W)

        school_class = Entry(frame, font=submenu_font, width=6)
        school_class.grid(row=1, column=2)
        

        # 회원가입
        sign_in_button = Button(self.sign_in_window, font=('배달의민족 주아', 17), text='회원가입', anchor=CENTER, command=lambda:self.sign_in(nickname.get(), password.get(), password_check.get(), school.get(),\
            grade.get(), school_class.get()))
        sign_in_button.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(20, 0))

        

    # 회원가입 함수
    def sign_in(self, nickname, password, password_check, school, grade, school_class):
        # 비밀번호 확인
        if password == password_check:

            # 유저 회원가입 정보 입력
            with open(r'information\users_information_file.json', 'w', encoding='UTF-8') as out_file:
                temporary_dict = json.load(out_file)
                temporary_dict[nickname] = {
                    'password'  :   password,
                    'school'    :   school,
                    'grade'     :   grade,
                    'school_class': school_class
                }
            self.sign_in_window.destroy()
        else:
            print('비밀번호를 정확히 입력해주세요.')

    
    # 로그인 함수
    def login(self, nickname, password):
        with open(r'information\users_information_file.json', 'r', encoding='UTF-8') as in_file:
            if nickname in in_file:
                if in_file[nickname]['password'] == password:
                    print('로그인 성공')
                    self.window.destroy()
                else:
                    print('비밀번호가 틀립니다.')
            else:
                print('아이디가 존재하지 않습니다.')

    # 로그인 닉네임 출력
    def __str__(self):
        return self.nickname.get()



        


