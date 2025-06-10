import garth

class GarminAuth:

    def __init__(self, email: str = None, password: str = None):
        self.email = email
        self.password = password
        self.authenticated = False
        self.client = None

    def login(self):
        garth.login(self.email, self.password)

        self.authenticated = True
        self.client = garth
        return self.client

    def connectapi(self, url, **kwargs):
        if not self.authenticated:
            self.login()
        return self.client.connectapi(url, **kwargs)