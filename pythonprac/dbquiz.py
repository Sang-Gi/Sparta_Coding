# %%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#Quiz1
movies = db.movies.find_one({'title':'매트릭스'},{'_id':False})
target_star = movies['star'] 
#Quiz2
same_star = list(db.movies.find({'star':target_star},{'_id':False}))
for target in same_star:
    print(target['title'])
#Quiz3
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
# %%
