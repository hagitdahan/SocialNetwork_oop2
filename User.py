from Post import PostFactory
class ManageUsers():
    list = []
    @staticmethod
    def addUser(user):
        ManageUsers.list.append(user)
    @staticmethod
    def deleteUser(user):
        ManageUsers.list.remove(user)
    @staticmethod
    def notifyUser(user_intercated,type,comment=""):
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
                            print(f"notification to {post_owner.name}: {user_intercated.name} commented on your post: {comment}")
                    post.isChanged = False
    @staticmethod
    def saleUpdate(sale_post,new_price,user_password):
        for user in ManageUsers.list:
            for post in user.posts:
                if post == sale_post:
                    if user.password != user_password:
                        return
                    if(new_price == -1):
                        post.price = new_price
                        print(f"{user.name}'s product is sold")
                    else:
                        post.price = new_price
                        print(f"Discount on {user.name} product! the new price is: {new_price}")
                    return


class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.online = True
        self.followers = []
        self.posts = []
        self.isChanged = False
        ManageUsers.addUser(self)

    def follow(self,user):
        user.followers.append(self)
        print(f"{self.name} started following {user.name}")
    def unfollow(self,user):
        user.followers.remove(self)
        print(f"{self.name} unfollowed {user.name}")
    def publish_post(self,type,text,price="",location=""):
        new_post = PostFactory.CreatePost(self,type,text,price,location)
        self.posts.append(new_post)

        if(type=="Text"):
            print(f"{self.name} published a post:\n{new_post.text}\n")
        elif(type=="Image"):
            print(f"{self.name} posted a picture\n")
        elif(type=="Sale"):
            print(f"{self.name} posted a product for sale:\n For sale! {text}, price: {price}, pickup from: {location}\n")

        return new_post
    def print_notifications(self):
        pass
    def __str__(self):
        #print(f"{self.name}")
        pass




