from database import Database
from user import User 

db = Database('blog.db')
# creating the table users 
User.create_table(db)

# save a user 
user1 = User(db,"Alice Mbugua", "alice.mbugua@moringaschool.com")
user1.save()

# fetch a user using id 
fetched_user = User.get_by_id(db,2)
if fetched_user:
    print(f'User id: {fetched_user.user_id}, Name: {fetched_user.name}, Email {fetched_user.email}')
    
users = User.get_all(db)
for user in users:
    print(f'User id: {user.user_id}, Name: {user.name}, Email {user.email}')


# delete a user 
# fetched_user.delete()

db.close()