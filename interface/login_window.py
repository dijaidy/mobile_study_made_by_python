from tkinter import *
import sys
import os
import json


# 폰트 설정
title_font = ("배달의민족 주아", 30)
menu_font = ("배달의민족 주아", 15)
submenu_font = ("배달의민족 주아", 17)


class Login_window:

    nickname = ''
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
        self.login_button = Button(self.window, font=('배달의민족 주아', 17), text='로그인', anchor=CENTER, command=lambda:self.log_in(self.nickname.get(),self.password.get()))
        self.login_button.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(20, 0))

        # 회원가입
        self.sign_in_button = Button(self.window, text='회원가입', font=('배달의민족 주아', 10), fg='gray', overrelief=FLAT, relief=FLAT, command=self.go_into_sign_in)
        self.sign_in_button.pack(side=TOP, anchor=NE, pady=(3, 0), padx=50)

        # 공지 텍스트
        self.inform_text1 = Label(self.window, font=('배달의민족', 10), anchor=CENTER, fg='red')
        self.inform_text1.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(5, 0))

        
        self.window.mainloop()

    #회원가입 함수
    def go_into_sign_in(self):

        # 창 설정
        self.sign_in_window = Tk()
        self.sign_in_window.title("회원가입 창")
        self.sign_in_window.geometry("400x500")
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

        self.password_check = Entry(self.sign_in_window, font=submenu_font)
        self.password_check.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50)

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
        sign_in_button = Button(self.sign_in_window, font=('배달의민족 주아', 17), text='회원가입', anchor=CENTER, command=lambda:self.sign_in(nickname.get(), password.get(), self.password_check.get(), school.get(),\
            grade.get(), school_class.get()))
        sign_in_button.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(20, 0))
        
        # 공지 텍스트
        self.inform_text2 = Label(self.sign_in_window, font=('배달의민족', 10), anchor=CENTER, fg='red')
        self.inform_text2.pack(side=TOP, anchor=CENTER, fill=BOTH, padx=50, pady=(5, 0))

        

    # 회원가입 함수
    def sign_in(self, nickname, password, password_check, school, grade, school_class):
        if nickname != '' and password != '' and password_check != '' and school !='' and grade != '' and school_class != '':
            # 비밀번호 확인
            if password == password_check:
                # 유저 회원가입 정보 입력
                with open(r'information\users_information_file.json', 'r', encoding='UTF-8') as in_file:                
                        temporary_dict = json.load(in_file)
                        if nickname in temporary_dict:
                            self.inform_text2.config(text='이미 존재하는 유저입니다.')

                        else:
                            temporary_dict[nickname] = {
                                'password'  :   password,
                                'school'    :   school,
                                'grade'     :   grade,
                                'school_class': school_class,
                                'chosen_book_file': {},
                                'plan_list_file'  : {}
                            }

                            with open(r'information\users_information_file.json', 'w', encoding='UTF-8') as out_file:
                                    json.dump(temporary_dict, out_file, ensure_ascii=False)
                                    self.sign_in_window.destroy()
            else:
                self.inform_text2.config(text='비밀번호 확인을 정확히 입력해주세요.')
                self.set_text_input(self.password_check, '')
        
        else:
            self.inform_text2.config(text='빈칸이 있습니다.')
            

    
    # 로그인 함수
    def log_in(self, nickname, password):
        if nickname != '' and password != '':
            with open(r'information\users_information_file.json', 'r', encoding='UTF-8') as in_file:
                dict = json.load(in_file)
                if nickname in dict:
                    if dict[nickname]['password'] == password:
                        Login_window.nickname = self.nickname.get()
                        self.window.destroy()
                    else:
                        self.inform_text1.config(text='비밀번호가 틀립니다.')
                        self.set_text_input(self.password, '')
                else:
                    self.inform_text1.config(text='닉네임이 존재하지 않습니다.')
                    self.set_text_input(self.nickname, '')
                    self.set_text_input(self.password, '')
        else:
            self.inform_text1.config(text='빈칸이 있습니다.')



    # 엔트리의 입력값 없애는 함수
    def set_text_input(self, entry, text):
        entry.delete(0,"end")
        entry.insert(0, text)

    # 로그인 닉네임 출력
    def __str__(self):
        return Login_window.nickname



        


