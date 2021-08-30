from config import db

# test for database access

#db.users.insert_one({"name": "Jesse", "email": "jessr@hotmail.com"})
#db.users.insert_one({"name": "Je", "email": "jer@hotmail.com"})
#db.users.insert_one({"name": "Jes", "email": "jesr@hotmail.com"})

cursor = db.users.find({"name": "Staff"})
for user in cursor:
    print(user)


