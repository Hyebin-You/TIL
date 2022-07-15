import requests

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=999'
response = requests.get(url).json()

print(response)