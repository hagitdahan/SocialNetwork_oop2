class Observer:

    def __init__(self,name):
        self.notificatins = []
        self.name = name

    def push_notification(self,notification):
        self.notificatins.append(notification)

    def like_post(self,Observer):
        if self.name != Observer.name:
            Observer.push_notification(f"{self.name} liked your post")
            print(f"notification to {Observer.name}: {self.name} liked your post")

    def comment_post(self,Observer,comment):
        if self.name != Observer.name:
            Observer.push_notification(f"{self.name} commented on your post")
            print(f"notification to {Observer.name}: {self.name} commented on your post: {comment}")
    def __str__(self):
        result = f"{self.name}'s Notifications:"
        for notification in self.notificatins:
            result += "\n" + notification
        return result

class Observerble:

    def __init__(self,name):
        self.observers = []
        self.name = name

    def add_observer(self,Observer):
        if Observer not in self.observers:
            self.observers.append(Observer)
            print(f"{Observer.name} started following {self.name}")


    def remove_observer(self,Observer):
        if Observer in self.observers:
            self.observers.remove(Observer)
            print(f"{Observer.name} unfollowed {self.name}")

    def update_new_post(self,new_post):
        for observer in self.observers:
            observer.push_notification(f"{self.name} has a new post")
        print(new_post)
    def update_discount_post(self,price):
        print(f"Discount on {self.name} product! the new price is: {price}")
    def update_sold_post(self):
        print(f"{self.name}'s product is sold")

    def num_followers(self):
        return len(self.observers)