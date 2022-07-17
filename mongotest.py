import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://imransah:imran123@cluster0.z0jr8ht.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    'name': 'imran sah',
    'email': 'imransah1623@gmail.com',
    'surname': 'Sah'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
