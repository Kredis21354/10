import pymongo

client = pymongo.MongoClient("mongodb+srv://retyp:12345@cluster0.iztqtnu.mongodb.net/?retryWrites=true&w=majority")

db = client["test"]

col = db["test"]

x = col.insert_one({"test":"My test data"})



#mongodb+srv://retyp:<password>@cluster0.iztqtnu.mongodb.net/?retryWrites=true&w=majority

