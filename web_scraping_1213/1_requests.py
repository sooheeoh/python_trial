import requests
# res = requests.get("http://naver.com")
res = requests.get("http://gofundme.com")
res.raise_for_status() # 문제가 생겼을 때는 오류를 내뱉고 바로 종료하도록 함
# print("응답코드 : ", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok: # ok로 끝나는 거 - 응답코드와 동일
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code,"]")

print(len(res.text))
print(res.text)

with open("mygofundme.html", "w", encoding="utf-8") as f:
    f.write(res.text)