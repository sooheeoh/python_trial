import re

p = re.compile("ca.e")
# . (ca.e): 하나의 문자 > care, cafe, case | caffe (X)
# ^ (^de): 문자열의 시작 > desk, destination | fade (X)
# $ (se$): 문자열의 끝 > case, base | face (X)

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않았습니다")

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인, 뒤에 뭐가 있어도 상관없음
print_match(m)
# print(m.group()) # case가 위의 정규식과 매칭이 되어서 그 내용을 출력한다는 의미, 매치되지 않으면 에러 발생
