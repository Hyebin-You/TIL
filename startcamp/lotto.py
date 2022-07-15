from multiprocessing import Semaphore
import requests
from random import sample

#1. lotto api로 부터 데이터 받아오기
#2. 지난주 당첨 번호 알아내기(1등만)
#3. ramdom module이 가지고 있는 sample이라는 함수를 사용하여
#  1부터 45중에 무작위 6개를 뽑는다.
#4. 그 번호가 당첨 번호와 일치하는지 확인한다.
#(5.) 천번 이상 새로운 로또 번호를 생성하여서
# 매번 당첨이 되었는지 확인해보는 로직 작성
# 
#(6.) 1등부터 2등을 포함한 (보너스 번호까지) 4등까지의
#각 당첨 횟수 출력하기

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'
response = requests.get(url).json()
No1 = response['drwtNo1']
No2 = response['drwtNo2']
No3 = response['drwtNo3']
No4 = response['drwtNo4']
No5 = response['drwtNo5']
No6 = response['drwtNo6']
Nobnus = response['bnusNo']
print('지난주 당첨 번호는'+' '+str(No1)+','+str(No2)+','+str(No3)+','+str(No4)+','+str(No5)+','+str(No6)+','+str(Nobnus))
Numb = [No1, No2, No3, No4, No5, No6, Nobnus]

def checkNum():
    sam = sample(range(1,45),6)
    a = 0
    b = 0
    for i in sam:
        for l in range(6):
            if i == Numb[l]:
                a = a + 1
        if i == Numb[6]:
            b = b + 1
    
    no1 = 0
    no2 = 0
    no3 = 0
    no4 = 0
    no5 = 0

    if a == 6:
        no1 = 1
    elif a == 5 and b == 1:
        no2 = 1
    elif a == 5 and b == 0:
        no3 = 1
    elif (a == 4 and b == 0) or (a == 3 and b == 1):
        no4 = 1
    elif (a == 3 and b == 0) or (a == 2 and b == 1):
        no5 = 1

    return [no1, no2, no3, no4, no5]

a = checkNum()
for i in range(5):
    if a[i] == 1:
        print(str(i)+'등에 당첨')

if a == [0,0,0,0,0]:
    print('당첨되지 못함')


def checktime1000():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    for i in range(1000):
        times = checkNum()
        if times[0] == 1:
            a = a + 1
        elif times[1] == 1:
            b = b + 1
        elif times[2] == 1:
            c = c + 1
        elif times[3] == 1:
            d = d + 1
        elif times[4] == 1:
            e = e + 1

    print('1등 당첨 횟수는 ' + str(a))
    print('2등 당첨 횟수는 ' + str(b))
    print('3등 당첨 횟수는 ' + str(c))
    print('4등 당첨 횟수는 ' + str(d))
    

checktime1000()