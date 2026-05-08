# for와 문자열
hello = '안녕하세요!'
for h in hello:
    print(h)
    
print('-'*50)

# for와 리스트
li=['푸바오', 100, 3.141592, '아이바오', '러바오']
for i in li:
    print(i)


print('-'*50)

# for와 딕셔너리
menu = {'김밥':3000, '라면':5000, '떡볶이':4000}
for m in menu:
    print(m)    #딕셔너리는  key만 출력하고  value는 출력하지 않는다.

for m in menu:
    print(menu[m]) #value 출력


for dic in menu.items():
    print(dic)

for k, v in menu.items():
    print(f'key:{k}, value:{v}')

print('-'*50)

for i in range(100):
    print(i)           # 0~99 까지 출력,  print()문은 enter를 포함. 자동 줄바꿈이 됨.

print()
print('-'*50)

for i in range(1, 31):
    print(i, end=' ')  # 1~30 까지 옆으로 출력, 줄바꿈 없음.
   
print()
print('-'*50)

for i in range(1, 31,2):
    print(i, end=' ')   # 홀수만
   
print()
print('-'*50)

# 거꾸로 30->1(1씩 감소)
for i in range(30, 0, -1):
    print(i, end=' ')