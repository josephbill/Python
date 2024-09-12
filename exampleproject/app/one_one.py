from utils import get_session, create_table
from models import User,Profile,Post


create_table()
#start a session
session = get_session()

#create user to profile (one to one)
user1 = User(name="Joseph", email="j@j.com")
profile1 = Profile(bio='software dev.', user=user1)

# add to session 
session.add(user1)
session.add(profile1)
session.commit()

users= session.query(User).all()
for user in users:
    print(user)
    print(user.profile)  #accessing one to one 
    
session.close()