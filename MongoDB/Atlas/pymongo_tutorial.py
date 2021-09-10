from pymongo import MongoClient
from env.env import CONNECTION

cluster = MongoClient(CONNECTION)
db = cluster['test']
collection = db['test']

# post = {'_id': 0, 'name': 'Tim', 'score': 5}
# post = {'name': 'Tim', 'score': 5}

# collection.insert_one(post)

post1 = {'_id': 2, 'name': 'Joe'}
post2 = {'_id': 3, 'name': 'Bill'}

# collection.insert_many([post1, post2])

# results = collection.find({'name': 'Bill'})
# results = collection.find({})

# for result in results:
#     # print(result['_id'])
#     print(result)

# results = collection.delete_one({'_id': 0})
# results = collection.delete_many({})        # delete everything

# results = collection.update_one({'_id': 2}, {'$set': {'name': 'Tim'}})
# results = collection.update_one({'_id': 2}, {'$set': {'score': 5}})
# results = collection.update_one({'_id': 2}, {'$inc': {'score': 5}})

post_count = collection.count_documents({})
print(post_count)