from Post import PostFactory

class User:
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        self.online = True
        self.followers = []
        self.posts = []
        self.notifications=[]

    def follow(self,user):
        user.followers.append(self)
        print(f"{self.name} started following {user.name}")
    def unfollow(self,user):
        user.followers.remove(self)
        print(f"{self.name} unfollowed {user.name}")
    def publish_post(self,type,text,price="",location=""):
        #add password to create post func
        pass
    def print_notifications(self):
        pass
    def __str__(self):
        #print(f"{self.name}")
        pass
    def authenticate(self,password):
        return password==self.__password



