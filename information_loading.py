import urllib.request
import json
import xmltodict

# ttbsmartapple031950001 TTBkey
# 요청url주소 = http://www.aladin.co.kr/ttb/api/ItemList.aspx
# http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001&Query=쎈&QueryType=쎈&MaxResults=10&CategoryId=76841&output=XML&Version=20131101

# 검색어에 따라 결과 출력
def load_aladin_book(grade): 
    input_word = input("검색어 입력> ")
    input_choice = input("선택사항 입력(학년, 과목):")
    query = "&query=" + urllib.parse.quote(input_word)
    url = (
       "http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001%s&MaxResults=10&CategoryId=76000&output=JS&Version=20131101"
    % query
    )

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        respose_body = response.read()
        decode_data = respose_body.decode("utf-8")
        print(decode_data)
        return decode_data



subject_id_dict = {
    "중학 1학년 공통 과학 1": "CLSS0000068529",
    "중학 1학년 공통 국어": "CLSS0000068510",
    "중학 1학년 공통 기술·가정 ⓛ": "CLSS0000068694",
    "중학 1학년 공통 도덕 ⓛ": "CLSS0000068623",
    "중학 1학년 공통 미술 ⓛ": "CLSS0000068739",
    "중학 1학년 공통 사회 ⓛ": "CLSS0000068583",
    "중학 1학년 공통 수학 1": "CLSS0000068558",
    "중학 1학년 공통 영어 1": "CLSS0000068757",
    "중학 1학년 공통 음악 ⓛ": "CLSS0000068725",
    "중학 1학년 공통 체육 ⓛ/②": "CLSS0000068637",
    "중학 2학년 공통 과학": "CLSS0000077433",
    "중학 2학년 공통 국어": "CLSS0000079323",
    "중학 2학년 공통 기술가정 ②": "CLSS0000079523",
    "중학 2학년 공통 미술 ②": "CLSS0000079996",
    "중학 2학년 공통 사회": "CLSS0000077950",
    "중학 2학년 공통 수학": "CLSS0000077664",
    "중학 2학년 공통 역사 ①": "CLSS0000058812",
    "중학 2학년 공통 영어": "CLSS0000081204",
    "중학 3학년 공통 과학 ③": "CLSS0000059357",
    "중학 3학년 공통 국어 ⑤": "CLSS0000058989",
    "중학 3학년 공통 국어 ⑥": "CLSS0000059091",
    "중학 3학년 공통 수학 ③": "CLSS0000059184",
    "중학 3학년 공통 역사 ②": "CLSS0000059293",
    "중학 3학년 공통 영어 ③": "CLSS0000059439",
}



def load_edunet_imformation(grade): #grade정수형
    input_word = input('과목을 입력해주세요')
    subject_ID = subject_id_dict[input_word]
   
    url_edunet = "http://down.edunet4u.net/KEDNCM/OPENAPI/SUBCONT/nedu_sub_cont_UNIT_LEARNING_CLSS0000057446_%s.xml" % subject_ID
    request = urllib.request.Request(url_edunet)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        decoded_data = response_body.decode("utf-8")
        xml_parse = xmltodict.parse(decoded_data)  # string인 xml 파싱
        xml_dict = json.loads(json.dumps(xml_parse))
        print(xml_dict)  # 결과를 출력한다


# class Book:
#    def __init__(self, title):
#        pass
load_edunet_imformation(3)