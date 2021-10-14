# 데이터 파일로 저장이나 불러오는 활동 총괄
import json
import time

class 찜한교재_manage_user_information:  # 교재등록 밑 관리
    def __init__(self):
        self.chosen_book_dict = {}
        self.chosen_book_dict = self.call_chosen_book_from_file()

    def plus_chosen_book_dict(self, book_title, book_dict, subject, book_type):  # 찜한 교재 목록에 추가
        book_dict["subject"] = subject  #교재의 과목
        book_dict["book_type"] = book_type  #교재의 종류(ex:예습교재, 시험교재)
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

    def update_subject(self, subject_list):  # 과목추가
        self.subject_list = subject_list

    def save_subject_list_to_file(self):  # 과목을 파일로 저장
        with open("information\subject_list_file.json", "w", encoding="UTF-8") as out_file:
            output_dict = {}
            output_dict["subject"] = self.subject_list
            json.dump(output_dict, out_file, ensure_ascii=False)

    def call_subject_list_from_file(self):  # 파일 불러오기
        with open("information\subject_list_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)["subject"]

class 공부계획_manage_user_information:                       #공부계획한 것들 저장
    def __init__(self):
        self.Korean_time = time.localtime(time.time())
        self.today = {"today" : {"month" : self.Korean_time.tm_mon, "day" : self.Korean_time.tm_mday}}
        self.plan_list_for_month = {}
        self.plan_list_for_month = self.call_plan_list_from_file()   #총 한 달의 기간 동안의 계획을 실행까지 며칠 남았냐에 따라 저장할 것임
        self.plan_list = {}
        self.plan_list = self.plan_list_for_month[self.today]
    def plus_plan_list(self, book_dict, start_time, end_time, day):
        #start_time은 시작시간, end_time은 끝나는 시간, day는 실행날짜
        self.plan_list = {"book" : book_dict, "start_time" : start_time, "end_time" : end_time}
        self.plan_list_for_month[day] = self.plan_list

    def save_plan_list_to_file(self):   #파일로 저장
        with open("information\plan_list_file.json", "w", encoding = "UTF-8") as out_file:
            json.dump(self.plan_list_for_month, out_file, ensure_ascii=False)

    def call_plan_list_from_file(self):    #파일 불러오기
        with open("information\plan_list_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)

    def return_present_time(self):  #현재 시각, 분을 튜플형태로 반환
        self.Korean_time = time.localtime(time.time())
        return (self.Korean_time.tm_hour, self.Korean_time.tm_min)

class users_information_manage:
    def __init__(self):
        self.users_information = {}
        self.users_information = self.call_users_information_from_file()

    def save_users_information_to_file(self, nickname, school, grade, classroom):   #입력받은 유저정보를 파일로 저장
        self.users_information = {"nickname" : nickname, "school" : school, "grade" : grade, "classroom" : classroom}
        with open("information\users_information_file.json", "w", encoding = "UTF-8") as out_file:
            json.dump(self.users_information, out_file, ensure_ascii=False)

    def call_users_information_from_file(self):    #파일 불러오기
        with open("information\plan_list_file.json", "r", encoding="UTF-8") as out_file:
            return json.load(out_file)

    