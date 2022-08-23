import sys
xx= sys.stdin.readline().strip()
'''
1. 처음 마이너스부터 다음 마이너스가 오기 전까지 + 는 모두 더해줘야 최소값이 나온다.
2. 따라서, -를 기준으로 시작괄호를 열고, 다음 -가 나온다면 그때 괄호를 닫아주자.
'''
equation=[]
num=''
cnt_start=0

for x in xx:
    if  x not in ['+','-']:
        if x=='0' and num=='':
            continue
        num=num+x
    else:
        if num=='': equation.append('0')
        else: equation.append(num)
        num=''
        if x=='-' and cnt_start==1: 
            equation.append(')'+x+'(')
        elif x=='-' and cnt_start==0: 
            equation.append(x+'(')
            cnt_start=1
        else: 
            equation.append(x)

if num=='': equation.append('0')
else: equation.append(num)
if cnt_start==1: 
    equation.append(')')
answer=eval(''.join(x for x in equation))
    
print(answer)
