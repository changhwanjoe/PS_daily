import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)

'''
{
    "id": "gildong123",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}
'''

import requests
# Important! 
# URL 을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET : www.movies.com/movies: : 영화를 전부 조회
# GET : www.movies.com/movies/id: : 아이디인 영화를 전부 조회
# PUT : www.movies.com/movies
# DELETE : www.movies.com/movies

# 세션 활성화
s = requests.Session()

# Example 1
r = s.get('https://github.com/events')

#수신 상태 체크
#r.raise_for_status() # 수신코드 400 에러가 발생하면 예외 발생하고 끔
print(r.text)


#예제2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입 (디테일하게)
jar.set('name','niceman',domain = 'httpbin.org',path='/cookies')

# 쿠키를 넣어서 요청
r=s.get('http://httpbin.org/cookies',cookies = jar)
#print(r.text)

#예제 3  Timeout을 넣어서 
r = s.get('https://github.com/',timeout=5)

#예제 4 
r=s.post('http://httpbin.org/post',data = {'id':'test44','pw':'111'},cookies=jar)

#예제 5
# 요청(Post)
paylod1={'id':'test44','pw':'111'}
payload2=(('id','test44'),('pw','111'))
r=s.post('http://httpbin.org/post',data=payload2)

#예제 6(Put)
r=s.put('http://httpbin.org/post',data=payload2)

#예제 6(delete)
r=s.delete('http://httpbin.org/delete',data={'id':1})
print(r.text)
print(r.headers)

# json 예제 ====
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)
#=========


# json 으로 바꾸기
import json
# 사전 자료형(dict) 데이터 선언
user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)
# ----------------------------- 