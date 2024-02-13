class Observer:

    def __init__(self,name):
        self.notificatins = []
        self.name = name

    def push_notification(self,notification):
        self.notificatins.append(notification)

    def like_post(self,Observer):
        Observer.push_notification(f"{self.name} liked your post")
        ## Add loud print

    def comment_post(self,Observer,comment):
        Observer.push_notification(f"{self.name} commented on your post")
        ## Add loud print
    def __str__(self):
        result = f"{self.name} Notifications:"
        for notification in self.notificatins:
            result += "\n" + notification


class Observerble:

    def __init__(self,name):
        self.observers = []
        self.name = name

    def add_observer(self,Observer):
        # what happned if twice?
        self.observers.append(Observer)
        print(f"{Observer.name} started following {self.name}")

    def remove_observer(self,Observer):
        self.observers.remove(Observer)
        print(f"{Observer.name} stopped following {self.name}")

    def update_new_post(self,new_post):
        for observer in self.observers:
            observer.push_notification(f"{self.name} has a new post")
        print(new_post)

    def update_discount_post(self,post):
        pass

    def update_sold_post(self,post):
        pass

