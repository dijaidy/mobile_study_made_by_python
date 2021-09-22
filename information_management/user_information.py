# 데이터 파일로 저장이나 불러오는 활동 총괄
import json

class 찜한교재_manage_user_information:  # 교재등록 밑 관리
    def __init__(self):
        self.chosen_book_dict = {}
        self.chosen_book_dict = self.call_chosen_book_from_file()

    def plus_chosen_book_dict(self, book_title, book_dict, subject, book_type):  # 찜한 교재 목록에 추가
        book_dict["subject"] = subject
        book_dict["book_type"] = book_type
        self.chosen_book_dict[book_title] = book_dict

    def save_chosen_book_to_file(self):  # 교재정보를 파일에 저장
        with open("information\chosen_book_file.json", "w", encoding="UTF-8") as out_file:
            json.dump(self.chosen_book_dict, out_file, ensure_ascii=False)

    def call_chosen_book_from_file(self):  # 파일 불러오기
        with open("information\chosen_book_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)


class 과목_manage_user_information:  # 유저의 학습 과목 관리
    def __init__(self):
        self.subject_list = []
        self.subject_list = self.call_subject_list_from_file()

    def update_subject(self, subject_list):  # 찜한 교재 목록에 추가
        self.subject_list = subject_list

    def save_subject_list_to_file(self):  # 교재정보를 파일에 저장
        with open("information\subject_list_file.json", "w", encoding="UTF-8") as out_file:
            output_dict = {}
            output_dict["subject"] = self.subject_list
            json.dump(output_dict, out_file, ensure_ascii=False)

    def call_subject_list_from_file(self):  # 파일 불러오기
        with open("information\subject_list_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)["subject"]

class 공부계획_manage_user_information:                       #공부계획한 것들 저장
    def __init__(self):
        self.plan_list = []
        self.plan_list = self.call_plan_list_from_file()
    def call_plan_list_from_file(self):    #파일 불러오기
        with open("information\plan_list_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)["0"]