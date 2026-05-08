# 빈 딕셔너리 생성
a = {}      #{}로 딕셔너리 확인
print(a)

b = dict()  # 형변환
print(b)

# 딕셔너리 초기화
#  <형식>
#    {key1:value1, key2:value2, .....}  #key는 중복될수 없음. value는 중복가능

menu = {'김밥':3000, '라면':5000}

print(menu['김밥'])
print(menu['라면'])

# 새로운 쌍 추가
menu['떡볶이'] = 4000
print(menu)

# 값 수정
menu['김밥']=3500
print(menu)

# 쌍(키와 값) 삭제
del(menu['라면'])
print(menu)

# set(세트) 자료형  --> 순서가 없다! 중복이 안된다.!
a = {30, 10, 30, 20, 30,10}
print(a)   # {10, 20, 30}

b = set()  #  빈 세트
print(b)

c = {40, 20}
print(c)

# 교집합
print('교집합 :', a & c)

# 합집합
print(a | b)  # | --> shift + \

# 차집합
print(a - c)
print(c - a)
