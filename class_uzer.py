class User:
    """System user"""

    def __init__(self, is_burnd: False, name: str, email:str, age:str, sex:str = "man" ):
        print("User created")
        self.is_burnd = is_burnd    
        self.name = name
        self.email = email
        self.age = age
        self.sex = sex

    def get_age(self):
        return self.age
    
    def set_age(self):
        self.age = 25
        return self.age
    
    def burnUser(self):
        self.is_burnd = True
        return self.is_burnd
    


userMasha = User()
print(userMasha)

userMasha.name = "Masha"
userMasha.email = "masha@mail.tpru"
userMasha.age = 10
userMasha.sex = "woman"

mashaAge = userMasha.get_age()

print(userMasha.name, mashaAge, userMasha.sex)

#mashaAge = userMasha.set_age()
User.set_age(userMasha)

print(userMasha.name, userMasha.age, userMasha.sex)
