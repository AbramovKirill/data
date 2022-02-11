import pymongo
from itertools import count
import datetime

# client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
# mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.1.9
client = pymongo.MongoClient("mongodb+srv://12345:12345@cluster0.htukn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.uprav_comp#присв db нашу бд(uprav_comp)
#db = client["uprav_comp"]
coll = db.advertisment#присв coll нашу колекц(advertisment)




##(ПУНКТ1(НАЕВРН))заполн колекц мусором, создаем 10 значений
# for i in range(10):
# 	data = {
# 		"_id": i,
# 		"text": "ВІдключення води білвлвл",
# 		"status": True,
# 		"time": datetime.datetime.now()
# 	}
# 	coll.insert_one(data)
# 	print(f"{i}: данные записаны!")

#уваляем всё из колекции
# res = coll.delete_many({})
# print("deleted:", res.deleted_count)

##(ПУНКТ4)удаляем значение с _id:1
# coll.delete_one({"_id": 1})

# #(ПУНКТ3(недодел))вставляем значение значение с _id:1 и новыми данными
#coll.insert_one({"_id": 1, "text": "лампочка пропала", "status": True, "time": datetime.datetime.now()})

# #(ПУНКТ2)выводит всё знач из колекц
# for value in coll.find():
# for value in coll.find().limit(3):#вывод 3 знач
# for value in coll.find().sort("_id", 1):#1 сорт по увел, -1 по убыванию
# 	print(value)
# 	print("отработало")	

#выведет всю информацию об оголош у которого _id: 2
#query = {"_id": 2}
# for value in coll.find(query):
# 	print(value)
# 	print("отработало")

# #выведет информацию об всех оголош, но без значения "status", "time"
# query = {"status": True}
# for value in coll.find(query, {"_id": 1, "text": 1}):#показываем только _id и text всех оголош
# 	print(value)
# 	print("отработало")

# current = {"_id": 2}#значения котор нужно найти
# new_data = {"$set": {"_id": 15}}#знач котор нужно указать, мы на них замен, использ модификатор "$set"
# coll.update_one(current, new_data)#и заменяем













# найти и изменить оголош без удаления
# если сделать как раньше, оно будем переберать последовательно по _id допустим 10млн _id(это займет много времени)
# 
#1.выводим инфу про индексы у _id: 1 (индексы сложная хрень, надо вникнуть)
# (важная сноска): когда есть логин пароль всякие, пишет так  {'_id_': {'v': 2, 'key': [('_id', 1)]}, 'login_-1': {'v': 2, 'key': [('login', -1)]}}
# 						когда мы уже удаляем индекс, пишется так:   {'_id_': {'v': 2, 'key': [('_id', 1)]}}
#              у нас самого начала нету индекса, выводит это: {'_id_': {'v': 2, 'key': [('_id', 1)]}}

# print(coll.index_information())#команда вывода инфы
# # 2.удаляем индекс
# coll.drop_index("login_-1")
# print(coll.index_information())
# # 3. создаем новый уникальный индекс, он недолжен повторятся
# coll.create_index([("logins", pymongo.ASCENDING)])# вот такое вот гавно {'_id_': {'v': 2, 'key': [('_id', 1)]}, 'logins_1': {'v': 2, 'key': [('logins', 1)]}}
# print(coll.index_information())
# # 4. ищим и выводи
# print(coll.find_one({"_id": 9}))
# #5. типо так мы ищем элем.колек. за секунды а не минуты... 
#автор мудак, я не понял







# current = {"_id": 2}
# new_data = {"$pull": {"arrage": "hii!!"}}
# coll.update_many(current, new_data)#добавляем элемент в конец