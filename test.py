subject_string_category = """CLSS0000068529 : 중학 1학년 공통 과학 1
CLSS0000068510 : 중학 1학년 공통 국어
CLSS0000068694 : 중학 1학년 공통 기술·가정 ⓛ
CLSS0000068623 : 중학 1학년 공통 도덕 ⓛ
CLSS0000068739 : 중학 1학년 공통 미술 ⓛ
CLSS0000068583 : 중학 1학년 공통 사회 ⓛ
CLSS0000068558 : 중학 1학년 공통 수학 1
CLSS0000068757 : 중학 1학년 공통 영어 1
CLSS0000068725 : 중학 1학년 공통 음악 ⓛ
CLSS0000068637 : 중학 1학년 공통 체육 ⓛ/②
CLSS0000077433 : 중학 2학년 공통 과학
CLSS0000079323 : 중학 2학년 공통 국어
CLSS0000079523 : 중학 2학년 공통 기술가정 ②
CLSS0000079996 : 중학 2학년 공통 미술 ②
CLSS0000077950 : 중학 2학년 공통 사회
CLSS0000077664 : 중학 2학년 공통 수학
CLSS0000058812 : 중학 2학년 공통 역사 ①
CLSS0000081204 : 중학 2학년 공통 영어
CLSS0000059357 : 중학 3학년 공통 과학 ③
CLSS0000058989 : 중학 3학년 공통 국어 ⑤
CLSS0000059091 : 중학 3학년 공통 국어 ⑥
CLSS0000059184 : 중학 3학년 공통 수학 ③
CLSS0000059293 : 중학 3학년 공통 역사 ②
CLSS0000059439 : 중학 3학년 공통 영어 ③
"""

subject_list = subject_string_category.split("\n")

subject_id_dict = {}
for i in range(0, len(subject_list) - 1):
    id_subject = subject_list[i]
    id_subject = id_subject.split(" : ")
    print(id_subject)
    subject_id_dict[id_subject[1]] = id_subject[0]

print(subject_id_dict)
