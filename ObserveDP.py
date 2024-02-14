#implimanting observer design pattern
class Observer:
    """
    This class represents Observer and has notifications and name
    """
    def __init__(self,name):
        self.notificatins = []
        self.name = name



    def push_notification(self,notification):
        """
         insert notification to notifications array
        :param notification: string of notification
        :return:
        """
        self.notificatins.append(notification)

    def like_post(self,Observer):
        """
        send notification to the observer about changes in his post and print it to screen
        :param Observer: observer instance
        :return:
        """
        if self.name != Observer.name:
            Observer.push_notification(f"{self.name} liked your post")
            print(f"notification to {Observer.name}: {self.name} liked your post")

    def comment_post(self,Observer,comment):
        """
        send notification to the observer about changes in his post and print it to screen
        :param Observer: observer instance, comment: comment content
        :return:
        """
        if self.name != Observer.name:
            Observer.push_notification(f"{self.name} commented on your post")
            print(f"notification to {Observer.name}: {self.name} commented on your post: {comment}")
    def __str__(self):
        """
        :return: notifications Observer string
        """
        result = f"{self.name}'s notifications:"
        for notification in self.notificatins:
            result += "\n" + notification
        return result

class Observerble:
    """
    This class represents Observerble and observers array and name
    """
    def __init__(self,name):
        self.observers = []
        self.name = name

    def add_observer(self,Observer):
        """
        if not exist add observer to observers array
        :param Observer: Observer instance
        :return:
        """
        if Observer not in self.observers:
            self.observers.append(Observer)
            print(f"{Observer.name} started following {self.name}")


    def remove_observer(self,Observer):
        """
        if exist remove observer from observers
        :param Observer: Observer instance
        :return:
        """
        if Observer in self.observers:
            self.observers.remove(Observer)
            print(f"{Observer.name} unfollowed {self.name}")

    def update_new_post(self,new_post):
        """
        send notification to observers
        :param new_post: Post instance
        :return:
        """
        for observer in self.observers:
            observer.push_notification(f"{self.name} has a new post")
        print(new_post)

    def update_discount_post(self,price):
        """
        print the update on the screen
        :param price: the new price of the product
        :return:
        """
        print(f"Discount on {self.name} product! the new price is: {price}")

    def update_sold_post(self):
        """
        print that the product is sold
        :return:
        """
        print(f"{self.name}'s product is sold")

    def num_followers(self):
        """
        :return: number of observers
        """
        return len(self.observers)