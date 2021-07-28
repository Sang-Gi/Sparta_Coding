# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#인서트 저장
doc = {'name':'bobby','age':25}
db.users.insert_one(doc)

# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#리스트 찾기
same_ages = list(db.users.find({'age':25},{'_id':False}))

for perseon in same_ages:
    print(perseon)
# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#조건 찾기
user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user['age'])

# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#업데이트
db.users.update_one({'name':'bobby'},{'$set':{'age':25}})


# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#삭제
db.users.delete_one({'name':'bobby'})

# %%
