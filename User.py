from ObserveDP import *
from Post import PostFactory


class User:
    """
    this class represent the user data, has name, password, online status and number of posts
    the user function in the network as:
    Observer - follow other users
    Observerble  - being followed by other users
    """
    def __init__(self,name,password):
        self.name = name
        self.__password = password
        self.observer = Observer(self.name)
        self.observable = Observerble(self.name)
        self.online = True
        self.posts_count = 0

    def follow(self,user):
        """
        this method set follow to user.
        :param user: user to follow (user instance)
        :return:
        """
        if self.online:
            user.observable.add_observer(self.observer)

    def unfollow(self,user):
        """
        this method set unfollow to user.
        :param user: user to unfollow (user instance)
        :return:
        """
        if self.online:
            user.observable.remove_observer(self.observer)

    def publish_post(self,type,text,price="",location=""):
        """
        this method publish a new post by user and sends update
        :param type: type of post
        :param text: URL/product/text content string
        :param price: default is empty string, else price of the product
        :param location: default is empty string, else location of the product
        :return: if online return new post
        """
        if self.online:
            new_post = PostFactory.CreatePost(type,self,text,price,location)
            self.posts_count += 1
            self.observable.update_new_post(new_post)
            return new_post

    def print_notifications(self):
        """
        this method print the notifications of the user
        :return:
        """
        print(self.observer)

    def __str__(self):
        """
        :return: the string representation of the user
        """
        return (f"User name: {self.name}, Number of posts: {self.posts_count},"
                f" Number of followers: {self.observable.num_followers()}")

    def authenticate(self,password):
        """
        this method check if password is the user's password.
        :param password: password string
        :return: true if password is correct, false otherwise
        """
        return password==self.__password



