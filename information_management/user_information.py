# 데이터 파일로 저장이나 불러오는 활동 총괄
import json


class 찜한교재_manage_user_information:  # 교재등록 밑 관리
    def __init__(self):
        self.chosen_book = {}
        self.chosen_book = self.call_chosen_book_from_file()

    def plus_chosen_book_dict(self, book_title, book_dict):  # 찜한 교재 목록에 추가
        self.chosen_book[book_title] = book_dict

    def save_chosen_book_to_file(self):  # 교재정보를 파일에 저장
        with open("information\chosen_book_file.json", "w", encoding="UTF-8") as out_file:
            json.dump(self.chosen_book, out_file, ensure_ascii=False)

    def call_chosen_book_from_file(self):  # 파일 불러오기
        with open("information\chosen_book_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)