import os
import garth
from getpass import getpass

class GarminAuth:
    def __init__(self, email: str = None, password: str = None, tokenstore: str = None):
        self.email = email
        self.password = password
        self.tokenstore = "~/.garth"
        self.authenticated = False

    def login(self):
        try:
            garth.resume("~/.garth")
        except:
            if not self.email or not self.password:
                raise ValueError("Email and password required for 1st time login!")
        
        self.authenticated = True
        print('we are here, this is garth')
        print(dir(garth))
        print(garth)
        return garth

