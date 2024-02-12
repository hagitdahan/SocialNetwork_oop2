class NotificationService:

    __followers = {}

    @staticmethod
    def add_follower(user_to_follow,user):
        if user_to_follow not in NotificationService.__followers:
            NotificationService.__followers[user_to_follow] = []
        # if NotificationService.__followers[user_to_follow] is list:
        NotificationService.__followers[user_to_follow].append(user)
        #
        print(f"{user.name} started following {user_to_follow.name}")

    @staticmethod
    def followers_count(user_to_follow):
        return len(NotificationService.__followers[user_to_follow])

    @staticmethod
    def remove_follower(user_to_follow,user):
        NotificationService.__followers[user_to_follow].remove(user)
        print(f"{user.name} stopped following {user_to_follow.name}")

    @staticmethod
    def notify_new_post(user_to_follow):
        for user in NotificationService.__followers[user_to_follow]:
            user.push_notification(f"{user_to_follow.name} add a new post")

    @staticmethod
    def notify_new_comment(user_to_follow,user,commnet):
        print(f"Notification for {user_to_follow.name}: {user.name} commented {commnet}")
        user_to_follow.push_notification(f"{user.name} commented your post")

    @staticmethod
    def notify_new_like(user_to_follow,user):
        print(f"Notification for {user_to_follow.name}: {user.name} liked your post")
        user_to_follow.push_notification(f"{user.name} liked your post")

    @staticmethod
    def notify_discount(owner,new_price):
        print(f"Discount on {owner.name} product! the new price is: {new_price}")

    @staticmethod
    def notify_sold(owner,product,price,location):
        print(f"Sold! Toyota prius 2012, price: 37800.0, pickup from: Haifa")