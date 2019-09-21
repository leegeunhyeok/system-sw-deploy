# 연습문제

# 아래 문자열의 길이를 구하시오.
# "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len('dk2jd923i1jdk2jd93jfd92jd918943jfd8923'))

# print 함수를 사용해서 아래와 같이 출력해보시오.
# apple;orange;banana;lemon
print('apple', 'orange', 'banana', 'lemon', sep=';')

# 화면에 * 기호 100개를 표시하시오.
print('*' * 100)

# 문자열 "30" 을 각각 정수형, 실수형, 문자형으로 변환해보시오.
var_1 = '30'
print(int(var_1), float(var_1), str(var_1))

# 다음 문자열 "Human" 에서 "man" 문자열만 추출해보시오.
var_2 = 'Human'
print(var_2[2:5])

# 다음 문자열을 거꾸로 출력해보시오. : "Strawberry"
var_3 = 'Strawberry'
print(var_3[::-1])

# 다음 문자열에서 '-'를 제거 후 출력하시오. : "010-7777-9999"
var_4 = '010-7777-9999'
print(var_4.replace('-', ''))

# 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하시오. : "http://daum.net"
var_5 = 'http://daum.net'
print(var_5.replace('http://', ''))

# 다음 문자열을 모두 대문자, 소문자로 각각 출력해보시오. : "Hello"
var_6 = 'Hello'
print(var_6.upper())
print(var_6.lower())

# 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하시오. : "abcdefghijklmn"
var_7 = 'abcdefghijklmn'
print(var_7[2:5])

# 다음 리스트에서 "Apple" 항목만 삭제하시오. : ["Banana", "Apple", "Orange"]
var_8 = ['Banana', 'Apple', 'Orange']
print(var_8.remove('Apple'))

# 다음 튜플을 리스트로 변환하시오. : (1,2,3,4)
var_9 = (1,2,3,4)
print(list(var_9))

# 다음 항목을 딕셔너리(dict)으로 선언해보시오.
# { 성인 - 100000 , 청소년 - 70000 , 아동 - 30000 }
var_10 = {
    '성인': 100000,
    '청소년': 70000,
    '아동': 30000
}
print(var_10)

# 위에서 선언한 dict 항목에 { 소아 - 0 } 항목을 추가해보시오.
var_10['소아'] = 0
print(var_10)

# 위에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보시오.
print(var_10.keys())

# 위에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보시오.
print(var_10.values())

# 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하시오.
q1 =  {'봄': '딸기', '여름': '토마토', '가을': '사과'}
print(q1['가을'])

# 아래 딕셔너리에서 '사과'가 포함되었는지 확인하시오.
q2 =  {'봄': '딸기', '여름': '토마토', '가을': '사과'}
print('사과' in q2.values())


# 다음 점수 구간에 맞게 학점을 출력하시오.
"""
81 ~ 100 : A학점
61 ~ 80 :  B학점
41 ~ 60 :  C학점
21 ~ 40 :  D학점
 0 ~ 20 :  F학점
"""
score = 89
if (score > 80 and score <= 100):
    print('A')
elif (score > 60 and score <= 80):
    print('B')
elif (score > 40 and score <= 60):
    print('C')
elif (score > 20 and score <= 40):
    print('D')
else:
    print('F')
    
# 다음 세 개의 숫자 중 가장 큰수를 출력하시오
# 12, 6, 18

# 주민등록번호에서 남자, 여자를 판별하시오.
# 임의의 주민등록번호 값을 가지고 구현
# 1,3 : 남자, 2,4 : 여자
person_number = '000509-3123456'
gender_code = person_number[7]
if (gender_code == '1' or gender_code == '3'):
    print('남자')
elif (gender_code == '2' or gender_code == '4'):
    print('여자')

# 다음 리스트 중에서 '정' 글자를 제외하고 출력하시오.
q = ['갑', '을', '병', '정']
for item in q:
    if item != '정':
        print(item)

# 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력하시오.
odd = [i for i in range(1, 101, 2)]
print(odd)

# 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하시오.
q4 = ['nice', 'study', 'python', 'anaconda', '!']
for item in q4:
    if len(item) >= 5:
        print(item)

# 아래 리스트 항목 중에서 소문자만 출력하시오.
q5 = ['A', 'b', 'c', 'D', 'e', 'F', 'G', 'h']
for item in q5:
    if item.islower():
        print(item)

# 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하시오.
q6 = ['A', 'b', 'c', 'D', 'e', 'F', 'G', 'h']
for item in q6:
    if item.isupper():
        print(item.lower())
    else:
        print(item.upper())
