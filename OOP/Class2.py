class User:
    def __init__(self,email,password):
        self.userEmail = email
        self.userPassword = password

    def logout(self):
        print("Logout")
#You can now create an object out of your class
firstUser = User("temwa@gmail.com","12345")
secondUser = User("King@gmail.com","king123")
thirdUser = User("james@gmail.com","james123")

print(secondUser.userEmail)
thirdUser.logout()