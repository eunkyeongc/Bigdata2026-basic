#학교, 학과, 이름, 연락처를 입력받아 변수에 저장하여 출력하세요.
#변수명: 학교(univ), 학과(dept), 이름(ㅜ믇), 연락처(phone)
# 나의 풀이 : 자료를 입력받아라고 했는데 처음부터 변수명에 넣어서 출력함.
# univ = '한국대학교'
# dept = '경제학과'
# name = '홍길동'
# phone = '010-1234-5678'

# print('학교: ', univ)
# print('학과: ', dept)
# print('이름: ', name)
# print('연락처: ', phone)
# print(f'{name} 학생은 {univ} {dept}에 재학 중이며, 연락처는 {phone}입니다.')

# 선생님 풀이
univ = input('학교 : ')
dept = input('학과 : ')
name = input('이름 : ')
phone =input('연락처 : ')
print(f'{name} 학생은 {univ} {dept}에 재학 중이며, 연락처는 {phone}입니다.')
print('-' * 50)

#이름과 출생연도를 입력받아 한국 나이를 출력하는 프로그램을 작성하세요.
#나의 풀이:  출생년도를 입력받아 나이 계산을 안함.
# name = input('이름 입력: ')
# birth = input('출생년도 입력: ')

# print('2023년 시점, 홍길동님의 한국 나이는 20살입니다.')

# 선생님 풀이
name = input('이름 입력: ')
birth = int(input('출생년도 입력: '))
age = 2023-birth+1

print(f'2023년 시점, {name}님의 한국 나이는 {age}살입니다.')
print('-' * 50)

#월을 입력받아 계절을 출력하는 프로그램을 작성하시오.
#나의 풀이:  비교연산자 활용가능
month = int(input('월 입력: '))
if 3 <= month and month <=5 :
    print(f'{month}월은 봄입니다.')
elif 6 <= month and month <= 8 :
    print(f'{month}월은 여름입니다.')
elif 9 <= month and month <= 11 :
    print(f'{month}월은 가을입니다.')
else :
    print(f'{month}월은 겨울입니다.')

# 선생님 풀이
month = int(input('월 입력: '))
if 3 <= month <=5 :
    print(f'{month}월은 봄')
elif 6 <= month <= 8 :
    print(f'{month}월은 여름')
elif 9 <= month <= 11 :
    print(f'{month}월은 가을')
else :
    print(f'{month}월은 겨울')

