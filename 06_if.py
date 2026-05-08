# 회원이며 '어서오세요'라는 인사말 출력
member = input('회원입니까??(y/n)')
if member == 'y' :
    print('반갑습니다!')
else:
    print('회원가입을 해 주세요.')

#-------------------------------------------------------------
# 회원이며 '어서오세요'라는 인사말 출력
member = input('회원입니까??(y/n)')
if member == 'y' :
    print('반갑습니다!')
elif member == 'n':
    print('회원가입을 하세요.')
else:
    print('y와 n중에 입력하세요.')
    
# 입장료 정가: 2만원, 6세 미만: 무료, 6세이상 60세 미만: 정가, 60세 이상: 정가 50%
age = int(input('나이를 입력하세요: '))
price = 20000
if age < 6:
    print('6세 미만은 무료입니다.')
elif age < 60:
    print(f'입장료는 {price}원입니다.')
else :
    print(f'경로우대 입장료는 {int(price*0.5)}원입니다.')