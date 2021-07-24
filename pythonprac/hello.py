#%%
print('hello sparta');

# %%
a = 2
b = 3
b
print(a+b)
# %%
first_name = 'Sang Gi'
last_name = 'Travis'
print(first_name+last_name)
# %%
a_list = ['사과', '배', '감']

print(a_list)

# %%
a_list = ['사과', '배', '감']

print(a_list[1])
# %%
a_list = ['사과', '배', '감']
a_list.append('복숭아')
print(a_list)

# %%
def cal(n1,n2):
    return n1 + n2

result = cal(2,3)
print(result)
# %%
age = 25

if age > 20:
    print('Adult!')
else:
    print('Child!')

# %%
def is_adult(age):
    if age > 20:
        print('Adult!')
    else:
        print('Child!')
is_adult(30)
is_adult(15)
# %%
fruits = ['사과','배','배','감',
'수박','귤','딸기','사과','배','수박']

count = 0
for ff in fruits:
    if ff == '수박':
        count += 1

print(count)

# %%
people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] < 20:
        print(person)
# %%
import requests 

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gu_for = rjson['RealtimeCityAir']['row']
for gu in gu_for:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if (gu_mise > 50):
        print(gu_name, gu_mise)

# %%
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')


for tr in trs:
    a_tag = tr.select_one('td.title > div > a')

    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = tr.select_one('td.title > div > a').text
        star = tr.select_one('td.point').text
        doc = {
            'rank': rank,
            'title': title,
            'star': star
        }
        db.movies.insert_one(doc)
# %%
