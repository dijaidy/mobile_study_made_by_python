# api를 이용하여 정보를 가져오는 것을 담당
import urllib.request
import json
import xmltodict
from datetime import datetime, timedelta

# 검색어에 따라 결과 출력
class API_loading:
    def __init__(self):
        self.subject_id_dict = {
            '1' :   {
                "과학": "CLSS0000068529",
                "국어": "CLSS0000068510",
                "기술·가정": "CLSS0000068694",
                "도덕": "CLSS0000068623",
                "미술": "CLSS0000068739",
                "사회": "CLSS0000068583",
                "수학": "CLSS0000068558",
                "영어": "CLSS0000068757",
                "음악": "CLSS0000068725",
                "체육": "CLSS0000068637"
            },
            '2' :   {
                "과학": "CLSS0000077433",
                "국어": "CLSS0000079323",
                "기술가정 ": "CLSS0000079523",
                "미술 ": "CLSS0000079996",
                "사회": "CLSS0000077950",
                "수학": "CLSS0000077664",
                "역사": "CLSS0000058812",
                "영어": "CLSS0000081204"
            },
            '3' :   {
                "과학": "CLSS0000059357",
                "국어": "CLSS0000058989",
                "국어 6": "CLSS0000059091",
                "수학": "CLSS0000059184",
                "역사": "CLSS0000059293",
                "영어": "CLSS0000059439"
            }
            
        }

    def return_subject_id(self):
        return self.subject_id_dict

    def load_aladin_book(self, keyword, CID):  # 검색하고 싶은 책을 입력받아 검색결과 리턴
        need_list = {"link", "priceStandard", "cover", "description"}
        input_word = keyword
        input_choice = 0
        query = "&query=" + urllib.parse.quote(input_word)
        url = (
            "http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001%s&MaxResults=20&CategoryId=%s&output=JS&Version=20131101"
            % (query, CID)
        )

        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            respose_body = response.read()
            decode_data = respose_body.decode("utf-8")
            json_data = json.loads(decode_data)
            searched_list = json_data["item"]

            searching_result = {}  # 최종적으로 띄워줄 정보
            for book in searched_list:
                book_dict = {}  # 하나의 책에 대한 정보모음
                for index in need_list:
                    book_dict[index] = book[index]
                searching_result[book["title"]] = book_dict

            return searching_result

    def choose():
        pass

    def load_edunet_information(self, subject_id):  # subject_id를 이용해 각 과목별 학습 컨텐츠 리턴
        need_list = {"kywrd", "url", "thum_img_full_path"}
        subject_ID = subject_id

        url_edunet = (
            "http://down.edunet4u.net/KEDNCM/OPENAPI/SUBCONT/nedu_sub_cont_UNIT_LEARNING_CLSS0000057446_%s.xml"
            % subject_ID
        )
        request = urllib.request.Request(url_edunet)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        # 정상적으로 받아 왔으면
        if rescode == 200:
            response_body = response.read()
            decoded_data = response_body.decode("utf-8")

            # xml파일을 json으로 변환
            xml_parse = xmltodict.parse(decoded_data)  # string인 xml 파싱
            xml_dict = json.loads(json.dumps(xml_parse))

            # 여러 컨텐츠 모음
            searched_list = xml_dict["root"]["contents"]["row"]

            # 필요한 컨텐츠만 추출
            searching_result = {}  # 최종적으로 띄워줄 정보
            for learning_content in searched_list:
                Learning_content_dict = {}  # 하나의 컨텐츠에 대한 정보모음

                for index in need_list:
                    Learning_content_dict[index] = learning_content[index]
                searching_result[learning_content["title"]] = Learning_content_dict
            print(searching_result)
            return searching_result  # 결과를 출력한다

        # 받아오는데 실패하면
        else:
            print("에듀넷 api 입력 오류")
            return 0

    def return_school_code(self, school):  # 학교 이름 입력 시 학교 코드 리턴
        input_file = "information\학교_코드_dict.json"

        school_name = school

        with open(input_file, "r", encoding="utf-8") as in_file:
            json_data = json.load(in_file)
            school_code_list = json_data[school_name]

        return school_code_list

    def load_school_timetable(self, school, grade, school_class):  # 학교, 학년, 반 입력 시 시간표 반환(바뀐 시간표까지 적용)
        school_code_list = self.return_school_code(school)
        today = datetime.today()
        weekday = today.weekday()
        from_day = today - timedelta(days=weekday)
        from_ymd = from_day.strftime("%Y%m%d")
        to_day = today + timedelta(days=4 - weekday)
        to_ymd = to_day.strftime("%Y%m%d")
        
        class_nm = school_class
        input_list = [from_ymd, to_ymd, grade, class_nm]
        school_code_list.extend(input_list)
        print(school_code_list)
        url_neis_api = (
            "https://open.neis.go.kr/hub/misTimetable?KEY=c14de8bbaf5d4856abb43baeb6383d30&Type=json&plndex=1&pSize=100&ATPT_OFCDC_SC_CODE=%s&SD_SCHUL_CODE=%s&TI_FROM_YMD=%s&TI_TO_YMD=%s&GRADE=%s&CLASS_NM=%s"
            % tuple(school_code_list)
        )

        request = urllib.request.Request(url_neis_api)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if rescode == 200:
            respose_body = response.read()
            decode_data = respose_body.decode("utf-8")
            json_data = json.loads(decode_data)

            timetable = {}
            weekday_list = ["월", "화", "수", "목", "금"]
            json_data = json_data["misTimetable"][1]["row"]

            # 요일 계산을 위한 변수
            prior_ymd = 0
            weekday_index = -1

            for lesson in json_data:
                this_ymd = lesson["ALL_TI_YMD"]
                if this_ymd != prior_ymd:
                    prior_ymd = this_ymd
                    weekday_index += 1
                    timetable[weekday_list[weekday_index]] = {}
                timetable[weekday_list[weekday_index]][lesson["PERIO"]] = lesson["ITRT_CNTNT"]

            print(timetable)

            return timetable, from_day, to_day