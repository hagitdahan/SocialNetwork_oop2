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
        # Check name and Password
        new_user = User(username,password)
        return new_user

    def log_out(self,username):
        for user in User.users:
            if user.username == username:
                user.online = False
                print(f"{username} disconnected")

    def log_in(self,username,password):
        for user in User.users:
            if user.username == username and user.password == password:
                user.online = True
                print(f"{username} connected")

    def __str__(self):
        result = f"{self.name} social network:"
        for user in User.users:
            result += f"\nUser name: {user.username}, Number of posts: {len(user.posts)}, Number of followers: {len(user.followers)}"
        return result