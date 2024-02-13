import ObserveDP
from ObserveDP import Observer
from Post import PostFactory
from NotificationService import NotificationService


class User:
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        self.observer = ObserveDP.Observer(self.name)
        self.observable = ObserveDP.Observerble(self.name)
        self.online = True
        self.posts_count = 0

    def follow(self,user):
        self.observable.add_follower(user.observer)

    def unfollow(self,user):
        self.observable.remove_follower(user.observer)

    def publish_post(self,type,text,price="",location=""):
        new_post = PostFactory.CreatePost(type,self,text,price,location)
        self.posts_count += 1
        self.observable.update_new_post(new_post)
        return new_post

    def print_notifications(self):
        print(self.observer)

    def __str__(self):
        return (f"User name: {self.name} Number of posts: {self.posts_count},"
                f" Number of followers: {NotificationService.followers_count(self)}")

    def authenticate(self,password):
        return password==self.__password



