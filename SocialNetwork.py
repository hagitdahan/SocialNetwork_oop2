from User import User
## Social Network - Singleton V
## Factroy - Posts (Which type of post to create) V
## User - Observer

class SocialNetwork(object):

    __instance = None

    def __new__(cls,name):
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
            cls.__instance.__initialized = False
            print(f"The social network {name} was created!")
        return cls.__instance
    def __init__(self,name):
        if not SocialNetwork.__instance.__initialized:
            self.name = name
            SocialNetwork.__instance.__initialized = True

    def sign_up(self,username,password):
        #check if the username in the publisher bank of users
        #add user
        pass


    def log_out(self,username):
        #edit the status of the user to offline in publisher bank
        pass

    def log_in(self,username,password):
        # edit the status of the user to offline in publisher bank
        pass

    def __str__(self):
        result = f"{self.name} social network:"
        #print all the users in publisher
        pass
