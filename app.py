import sys
from dbhelper import DBhelper
class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()
    def menu(self):
        user_input = input("""
              1. Enter 1 to register
              2. Enter 2 to login 
              3. Anything else to leave
              """)
        if user_input == "1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(1000)

    def login_menu(self):
        input("""
        1. Enter 1 to see profile:
        2. Enter 2 to edit profile:
        3. Enter 3 to delete profile:
        4. Enter 4 to logout:
        """)

    def register(self):
        name= input("enter name")
        email=input("enter email")
        password=input("enter password")
        
        response= self.db.register(name,email,password)

        if response:
            print("successfull")
        else:
            print("failed")
    
    def login(self):
        email=input("Enter email:")
        password=input("Enter password:")

        data= self.db.search(email,password)
        if len(data)==0:
            print("incorrect email/password")
            self.login()
        else:
            print("hello,",data[0][1])
            self.login_menu()
obj= Flipkart()


        