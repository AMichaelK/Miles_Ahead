import garth
from getpass import getpass

class GarminAuth:
    def __init__(self, email: str = None, password: str = None, tokenstore: str = None):
        self.email = email
        self.password = password
        self.tokenstore = "~/.garth"
        self.authenticated = False
        self.client = None

    def login(self):
        try:
            garth.resume("~/.garth")
        except:
            if not self.email or not self.password:
                raise ValueError("Email and password required for 1st time login!")
            garth.login(self.email, self.password)
            garth.dump(self.tokenstore)

        self.authenticated = True
        self.client = garth
        return self.client
    
    def connectapi(self, url):
        if not self.authenticated:
            self.login()
        return self.client.connectapi(url)

