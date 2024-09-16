from models.models import User, Product, create_db, SessionLocal
import sys

#menu 
def menu():
    print("\n=== CLI Menu ===")
    print("1. Add User")
    print("2. Add Product")
    print("3. View Users")
    print("4. View Products")
    print("5. Update User")
    print("6. Delete User")
    print("0. Exit")
    
# Add a new user
def add_user():
    # validating , appropriate error message 
    session = SessionLocal()
    name = input("Enter user name: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    print(f"User '{name}' added.")
    
# glossary of methods 

def main():
    create_db() # ensuring the db is created
    # create the loop 
    while True:
        menu()
        choice = input("choose an option: ")
        if choice == "1":
            add_user()
        elif choice == "0":
            print("goodbye!")
            sys.exit()
        else:
            print("option not valid")
            
            
if __name__ == "__main__":
    main()