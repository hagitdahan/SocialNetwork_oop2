from Post import PostFactory
from NotificationService import NotificationService


class User:
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        self.online = True
        self.posts_count = 0
        self.__notifications = []

    def follow(self,user):
        NotificationService.add_follower(user,self)

    def unfollow(self,user):
        NotificationService.remove_follower(user, self)

    def publish_post(self,type,text,price="",location=""):
        new_post = PostFactory.CreatePost(type,self,text,price,location)
        self.posts_count += 1
        NotificationService.notify_new_post(self)
        return new_post

    def print_notifications(self):
        print(f"{self.name} Notifications: ")
        for string in self.__notifications:
            print(string)

    def push_notification(self,string):
        self.__notifications.append(string)

    def __str__(self):
        return (f"User name: {self.name} Number of posts: {self.posts_count},"
                f" Number of followers: {NotificationService.followers_count(self)}")

    def authenticate(self,password):
        return password==self.__password



