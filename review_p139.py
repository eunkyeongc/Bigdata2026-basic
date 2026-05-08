#학교, 학과, 이름, 연락처를 입력받아 변수에 저장하여 출력하세요.
#변수명: 학교(univ), 학과(dept), 이름(ㅜ믇), 연락처(phone)
univ = '한국대학교'
dept = '경제학과'
name = '홍길동'
phone = '010-1234-5678'

print('학교: ', univ)
print('학과: ', dept)
print('이름: ', name)
print('연락처: ', phone)
print(f'{name} 학생은 {univ} {dept}에 재학 중이며, 연락처는 {phone}입니다.')

#이름과 출생연도를 입력받아 한국 나이를 출력하는 프로그램을 작성하세요.
name = input('이름 입력: ')
birth = input('출생년도 입력: ')

print('2023년 시점, 홍길동님의 한국 나이는 20살입니다.')


#월을 입력받아 계절을 출력하는 프로그램을 작성하시오.
month = int(input('월 입력: '))
if 3 <= month and month <=5 :
    print(f'{month}월은 봄입니다.')
elif 6 <= month and month <= 8 :
    print(f'{month}월은 여름입니다.')
elif 9 <= month and month <= 11 :
    print(f'{month}월은 가을입니다.')
else :
    print(f'{month}월은 겨울입니다.')

