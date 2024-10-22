import binascii

class Ecrypt:
    def __init__(self, password):
        try:
            if password is not None:
                self.__password = password
                self.__encrypted_password = None 
            else:
                return # Password is None / Empty
        except ValueError as e:
            return e # Error when the input is not a password

    def __encryption_first_letter(self, password_length):

        password_length = password_length

        first_letter = self.__password[0]
        letter_hex = binascii.hexlify(first_letter.encode('utf-8').decode('utf-8'))

        return (password_length * letter_hex) / 10
    
    def __encryption_odd_letter(self):
        

    def do(self):
        
        password_length = len(self.__password)

        encrypted_first_letter = self.__encryption_first_letter(password_length)



        

        
    