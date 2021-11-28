from tkinter import *
from tkinter import ttk as tk
import sys
import os
import json
from PIL import Image, ImageTk
import webbrowser
import tkinter.ttk

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
    book_index = 0
    def __init__(self):
        # 찜한교재_manage_user_information 상속받기
        super(찜한교재목록_window, self).__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("찜한교재현황")
        self.window.geometry("400x790")
        self.window.resizable(width=False, height=False)

        # 현재 위치/책 전체 개수
        self.searching_order = Label(self.window, font=menu_font, text='')
        self.searching_order.place(x=120, y=125, width=170, height=30)



        # 검색어입력창
        self.search_entry = Entry(self.window, font=menu_font)
        self.search_entry.place(relx=0, relwidth=4 / 5, rely=0, height=50)

        # 교재 불러오기
        with open('information\chosen_book_file.json', 'r', encoding='UTF-8') as every_book_dict:
            book_dict = json.load(every_book_dict)

        # 검색하기 버튼
        self.search_button = Button(
            self.window, text="검색(필터)", font=('배달의민족 주아', 14), command=lambda: self.fill_book_frame(book_dict=book_dict,first = False)
        )
        self.search_button.place(relx=4 / 5, relwidth=1 / 5, rely=0, height=50)

        # 과목분류_텍스트
        self.subject_sort_text = Message(
            self.window,
            font=("배달의민족 주아", 12),
            justify=CENTER,
            anchor=CENTER,
            text="과목",
            width=200,
        )
        self.subject_sort_text.place(x=0, y=60, width=200, height=20)

        # 성취도분류_텍스트
        self.achievement_sort_text = Message(
            self.window, font=("배달의민족 주아", 12), justify=CENTER, anchor=CENTER, text="성취도"
        )
        self.achievement_sort_text.place(x=200, y=60, width=200, height=20)

        # 카테고리 가져오기
        self.subject_list = []  # 전 카테고리 딕셔너리
        with open("information\subject_list_file.json", "r", encoding="UTF-8") as in_file:
            self.subject_list = json.load(in_file)['subject']

        # 과목분류 콤보박스
        self.subject_list.insert(0, '전체')
        self.subject_sort_combobox = tkinter.ttk.Combobox(
            self.window, values=self.subject_list, state="readonly"
        )
        self.subject_sort_combobox.place(x=20, y=80, width=160, height=30)
        self.subject_sort_combobox.current(0)

        #성취도 시작 범위 텍스트
        achievement_start_range_text = Label(self.window, font=('배달의민족 주아', 10), justify=CENTER, anchor=CENTER, text='시작 범위')
        achievement_start_range_text.place(x=200, y=80, width=100, height=20)
        #성취도 끝 범위 텍스트
        achievement_end_range_text = Label(self.window, font=('배달의민족 주아', 10), justify=CENTER, anchor=CENTER, text='끝 범위')
        achievement_end_range_text.place(x=300, y=80, width=100, height=20)

        # 성취도분류 조정
        self.achievement_start_value = StringVar(self.window)
        self.achievement_end_value = StringVar(self.window)
        achievement_start_value_list = [str(i) + '%' for i in range(0, 101, 5)]
        achievement_end_value_list = [str(i) + '%' for i in range(0, 101, 5)]

        self.achievement_start_spinbox = Spinbox(self.window, values=achievement_start_value_list, textvariable=self.achievement_start_value)
        self.achievement_start_spinbox.place(x=220, y=100, width=80, height=20)
        self.achievement_end_spinbox= Spinbox(self.window, values=achievement_end_value_list, textvariable=self.achievement_end_value)
        self.achievement_end_spinbox.place(x=300, y=100, width=80, height=20)
        self.achievement_start_value.set('0%')
        self.achievement_end_value.set('100%')


        self.achievement_start_spinbox.bind('<Button-1>', self.adjust_start_achievement)
        self.achievement_end_spinbox.bind('<Button-1>', self.adjust_end_achievement)
        self.achievement_start_spinbox.bind('<ButtonRelease-1>', self.adjust_start_achievement)
        self.achievement_end_spinbox.bind('<ButtonRelease-1>', self.adjust_end_achievement)

        # 프레임 만들기
        self.frame_canvas = Frame(self.window, width=400, height=630)
        #self.frame_canvas.pack(side=TOP, pady=(140,0), fill='x')
        #self.frame_canvas.pack_propagate(False)
        self.frame_canvas.grid(row=0, column=0, pady=(160, 0), sticky='n')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)



        # 그 프레임안에 캔버스 그리기
        self.canvas = Canvas(self.frame_canvas, bg='yellow')
        self.canvas.grid(row=0, column=0, sticky='news')

        
                # 캔버스에 스크롤바 연결
        self.vsb = Scrollbar(self.frame_canvas, orient='vertical', command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        
        
        

        self.book_frame = Frame(self.canvas) # width=360
        self.canvas.create_window((0, 0), window=self.book_frame, anchor='nw')

        with open('information\chosen_book_file.json', 'r', encoding='UTF-8') as every_book_dict:
            self.fill_book_frame(json.load(every_book_dict))
        self.book_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
            

        


        # Update buttons frames idle tasks to let tkinter calculate buttons sizes

        # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
        first5columns_width = 380
        first5rows_height = 660

        # 루프
        self.window.mainloop()

        
    def filter_book(self):
        searching_word = self.search_entry.get()
        subject = self.subject_sort_combobox.get()
        achievement_range = (int(self.achievement_start_value.get().replace('%', '')), int(self.achievement_end_value.get().replace('%', '')))
        return searching_word, subject, achievement_range
            
    def adjust_start_achievement(self, event):
        if int(self.achievement_start_value.get().replace('%', '')) >= int(self.achievement_end_value.get().replace('%', '')):
            self.achievement_start_value.set(str(int(self.achievement_end_value.get().replace('%', ''))-5)+'%')

    def adjust_end_achievement(self, event):
        if int(self.achievement_start_value.get().replace('%', '')) >= int(self.achievement_end_value.get().replace('%', '')):
            self.achievement_end_value.set(str(int(self.achievement_start_value.get().replace('%', ''))+5)+'%')

    def fill_book_frame(self, book_dict, first = True):
        # 각 책마다 다른 인덱스(위젯 row 조정에 이용)
        if not first:   # 검색버튼 눌러서 책 리스트 내용입력할 때
            print('조건 검사')
            #프레임 재생성
            
            self.book_frame.destroy()
            self.book_frame = Frame(self.canvas) # width=360
            self.canvas.create_window((0, 0), window=self.book_frame, anchor='nw')
            # 조건 변수 저장
            searching_word, subject, achievement_range = self.filter_book()
            removing_list = []
            # 검색어 필터
            if searching_word == '':
                print('검색어 없음')
            else:
                for book_title in book_dict:
                    if  searching_word not in book_title:
                        removing_list.append(book_title)
                for book_title in removing_list:
                    del(book_dict[book_title])

            # 과목 필터
            if subject == '전체':
                print('전체 과목')
            else:

                for book_title in book_dict:
                    if book_dict[book_title]['subject'] != subject:
                        removing_list.append(book_title)

                for book_title in removing_list:
                    del(book_dict[book_title])
            
            #############성취도 관련 필터 ###################
        print(book_dict)
        self.searching_order.config(text = '교재 전체 개수: %s권'%str(len(book_dict)))
        book_index = -1
        first_book_boolean= False
        self.book_image_list = []
        for book_title in book_dict:
            book_index += 1
            # 교재 표지 사진 저장
            url = book_dict[book_title]["cover"]

            os.system("curl " + url + " > ignore_image\%s.jpg" % str(book_index))

            # 이미지 크기 조정
            size_adjusting_image = Image.open("ignore_image\%s.jpg" % str(book_index))
            image = size_adjusting_image.resize(
                (120,160), Image.ANTIALIAS
            )

            resized_image = ImageTk.PhotoImage(image, master=self.window)  # 새창에서 그림띄우면 마스터 정의 꼭!
            self.book_image_list.append(resized_image)

            # 교재 이미지
            Label(self.book_frame, borderwidth=2, relief="sunken", image=self.book_image_list[book_index], text="", width=120, height=160)\
                .grid(row= book_index * 3 + 1, column=0, rowspan=2)


            # 교재 타이틀
            if first_book_boolean:
                pady = (15, 0)
            else:   # 처음이면
                pady = (0, 0)
                first_book_boolean = True
            Message(self.book_frame, font=('배달의민족 주아', 14), text=book_title, anchor=N, justify=LEFT,width=375, background='skyblue')\
            .grid(row=book_index * 3 + 0, column=0, columnspan=3, sticky=W, pady=pady)


            # 교재 정보 내용
            book_info_text = book_dict[book_title]['description']
            if book_info_text == '':
                book_info_text = '교재 설명: \n위 교재는 교재 설명을 지원하지 않습니다.'
            else:
                book_info_text = '교재 설명: \n%s'%book_info_text                

            # 교재 정보
            self.book_info = Message(self.book_frame, font=('배달의민족 주아', 12), justify=LEFT, text=book_info_text, width=245)
            self.book_info.grid(row=book_index * 3 + 1, column=1, columnspan=2, sticky=NW, pady=5)
            #self.open_web_button = Button(
            #    self.window, font=menu_font, text="교재\n웹사이트\n오픈", padx=1, pady=1
            #)
            #self.open_web_button.place(x=250, y=175, width=125, height=125)

            # 성취도
            self.book_achievement = DoubleVar()
            self.achievement_bar = tk.Progressbar(
                self.book_frame, maximum=100, length=220, variable=self.book_achievement
            )
            self.achievement_bar.grid(row=book_index * 3 + 2, column=1, sticky=S)
            self.achievement_bar.config(value=50)

            self.book_achievement_text = Message(self.book_frame, font=('배달의민족 주아', 8), justify=CENTER, text='성취도\n0%', width=40)
            self.book_achievement_text.grid(row=book_index * 3 + 2, column=2, sticky=S)
            self.window.update()

            # 기타 인스턴스변수 생성
            #self.book_index = 0
            #self.present_book = {}
            #self.present_book_title = ""

        
   



        




