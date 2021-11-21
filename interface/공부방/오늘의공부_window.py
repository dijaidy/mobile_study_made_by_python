from tkinter import *
import sys
import os

sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.user_information import 공부계획_manage_user_information
from PIL import Image, ImageTk


class 오늘의공부_window(공부계획_manage_user_information):
    def __init__(self):
        super(오늘의공부_window, self).__init__()
        # 창 설정
        self.window = Tk()
        self.window.title("오늘의공부")
        self.window.geometry("400x800")
        self.window.resizable(False, False)

        self.studied_time={"hour" : 0, "minute": 0, "second" : 0} #총 공부시간
        self.show_you_late=Label(self.window, width=400, height=700, fill="")    #늦었으면 노랑, 제대로 끝냈으면 초록, 아직 하기 전이면 파랑
        self.show_you_late.place(x=0, y=100)
        self.show_studied_time=Label(self.window, text="총 공부시간:"+str(self.studied_time["hour"])+":"+str(self.studied_time["minute"])+":"+str(self.studied_time["second"]))  #총 공부시간 보여주기
        self.book_index=0
        self.show_book_information()

    def show_book_information(self, index_moving=0):  # 알라딘api에서 가져온 책 정보를 이용해 띄워줌
        # 찜한 책 모음 가져오기
        searching_result = self.plan_list_for_month[self.return_present_time().tm_yday]

        # 인덱스 조정
        if self.book_index == 0 and index_moving == (-1):
            self.book_index = len(searching_result) - 1
        elif self.book_index < len(searching_result) - 1:
            self.book_index += index_moving
        elif self.book_index >= len(searching_result) - 1:
            self.book_index = 0
        # 책제목 리스트
        title_list = list(searching_result.keys())

        # curl 요청
        # curl "이미지 주소" > "저장 될 이미지 파일 이름"
        book = searching_result[title_list[self.book_index]]
        self.present_book = book
        self.present_book_title = title_list[self.book_index]
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
        book_title_text = title_list[self.book_index]
        self.book_title.config(text=book_title_text)

        # 인덱스 수정
        searching_order_text = "%s / %s" % (len(searching_result), self.book_index + 1)
        self.searching_order.config(text=searching_order_text)

        self.window.mainloop()