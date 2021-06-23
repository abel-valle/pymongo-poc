from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

# collection.insert_one({"name": "keyboard", "price": 300})

'''
product_one = {"name": "mouse"}
product_two = {"name": "monitor"}

collection.insert_many([product_one, product_two])
'''

results = collection.find()
# print(results)
for r in results:
    print(r['name'])

print('----------')
results = collection.find({"price": 300})
for r in results:
    print(r)

print('----------')
result = collection.find_one({"price": 300})
print(result)

# collection.delete_many({"price": 300})
collection.delete_one({"name": "monitor"})

# Delete all documents.
# collection.delete_many({})

# Uncomment to create the document.
# collection.insert_one({"name": "laptop"})

# collection.update_one({"name": "laptop"}, {"$set": {"name": "keyboard", "price": 450}})
collection.update_one({"name": "keyboard"}, {"$inc": {"price": 25}})

products_num = collection.count_documents({})

print('----------')
print(products_num)
