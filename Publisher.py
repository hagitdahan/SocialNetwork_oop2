class Publisher:
    list = []

    @staticmethod
    def addUser(user):
        ManageUsers.list.append(user)

    @staticmethod
    def deleteUser(user):
        ManageUsers.list.remove(user)

    @staticmethod
    def notifyUser(user_intercated, type, comment=""):
        post_owner = None
        for user in ManageUsers.list:
            for post in user.posts:
                if post.isChanged:
                    post_owner = user
                    if post_owner == user_intercated:
                        post.isChanged = False
                        continue

                    match type:
                        case "Like":
                            print(f"notification to {post_owner.name}: {user_intercated.name} like your post")
                        case "Comment":
                            print(
                                f"notification to {post_owner.name}: {user_intercated.name} commented on your post: {comment}")
                    post.isChanged = False

    @staticmethod
    def saleUpdate(sale_post, new_price, user_password):
        for user in ManageUsers.list:
            for post in user.posts:
                if post == sale_post:
                    if user.password != user_password:
                        return
                    if (new_price == -1):
                        post.price = new_price
                        print(f"{user.name}'s product is sold")
                    else:
                        post.price = new_price
                        print(f"Discount on {user.name} product! the new price is: {new_price}")
                    return

