from User import User

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
            self.users=[]
            SocialNetwork.__instance.__initialized = True

    def contains(self,username):
        for user in self.users:
            if username == user.name:
                return user
        return None

    def sign_up(self,username,password):
        if(self.contains(username)==None and len(password)>=4 and len(password)<=8):
            new_user = User(username,password)
            self.users.append(new_user)
            return new_user


    def log_out(self,username):
        #edit the status of the user to offline in publisher bank
        tmp_user=self.contains(username)
        if tmp_user is not None:
            tmp_user.online=False
            print(f"{username} disconnected")

    def log_in(self,username,password):
        # edit the status of the user to offline in publisher bank
        tmp_user=self.contains(username)
        if tmp_user is not None and tmp_user.authenticate(password):
            tmp_user.online=True
            print(f"{username} connected")


    def __str__(self):
        result = f"{self.name} social network:"
        for user in self.users:
            result += "\n" + user.__str__()
        return result
