from utils import get_session,create_table
from models.user import User
from models.post import Post 

create_table()
session = get_session()

#create a user 
user1 = User(name="Joseph", email="j@j.com")
post1 = Post(title="First post", content="jfjsdksjd", user=user1 )
post2 = Post(title="Second post", content="jfjsdksjd", user=user1 )

session.add(user1)
session.add_all([post1,post2])
session.commit()

users = session.query(User).all()
for user in users:
    print(user)
    for post in user.posts:
        print(f' {post}')
  
#reverse  
posts = session.query(Post).all()
for post in posts:
    print(post)
    print(f' user- {post.user}')
    
session.close()