class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password