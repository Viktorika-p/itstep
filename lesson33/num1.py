from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test']

persons = db.persons


persons.update_one({"firstName": "John"}, 
{"lastName": "West"}, {"email": "john@gmail.com"},
{"phone": "02134867651"}, {"wallet": "{"eur":20,"usd": 30, "uah": "2000"}},
{"address": {"building":"1007", "city":"NewYork"}}, {"Conpany":"Coca-cola"})

print(singers.find())
