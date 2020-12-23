from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})


# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))

#print(all_users[0])     #0번째 결과값을 보기
#print(all_users[0]['name'])

# for user in all_users:
#     print(user)

# MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':40}))

# for user in same_ages:
#     print(user)

user = db.users.find_one({'name': '덤블도어'})
print(user)

# 그 중 특정 키 값을 빼고 보기
user = db.users.find_one({'name': '덤블도어'}, {'_id': False})
print(user)

# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 119}})

user = db.users.find_one({'name' : '덤블도어'})
print(user)

db.users.delete_one({'name': '론'})
Rons =list(db.users.find({'name':'론'}))
print(Rons)


# Create(생성)
user1 = {'name': '론', 'age': 40}
user2 = {'name': '해리', 'age': 40}
db.users.insert_one(user1)
db.users.insert_one(user2)

# Read(조회) - 한 개 값만
user = db.users.find_one({'name': '론'})

# Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age': 40}, {'_id': False}))

# Update(업데이트) - 여러 값
db.people.update_many({'age': 40}, { '$set': {'age': 70}})

# Update(업데이트) - 하나 값
db.users.update_one({'name': '론'}, {'$set': {'age': 116}})

# Delete(삭제)
db.users.delete_one({'name': '론'})