import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Post:

    def __init__(self,owner):
        self.owner = owner

    def like(self,user):
        if user.online:
            user.observer.like_post(self.owner.observer)

    def comment(self,user,comment_text):
        if user.online:
            user.observer.comment_post(self.owner.observer,comment_text)

class PostFactory:
    @staticmethod
    def CreatePost(type,owner,text,price,location):
        if type == "Text":
            return TextPost(owner=owner,text=text)
        elif type == "Image":
            return ImagePost(owner,text)
        elif type == "Sale":
            return SalePost(owner=owner,product=text,price=price,location=location)

class SalePost(Post):
    def __init__(self,owner,product,price,location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.sold_state = False


    def discount(self,quantity,user_password):
        permission = self.owner.authenticate(user_password)
        if permission and self.owner.online:
            self.price = self.price - self.price * (quantity / 100)
            self.owner.observable.update_discount_post(self.price)

    def sold(self,user_password):
        permission = self.owner.authenticate(user_password)
        if permission and self.owner.online:
            self.sold_state = True
            self.owner.observable.update_sold_post()

    def __str__(self):
        if(self.sold):
            return f"{self.owner.name} posted a product for sale:\nSold! {self.product}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.owner.name} posted a product for sale:\nfor sale! {self.product}, price: {self.price}, pickup from: {self.location}\n"

class ImagePost(Post):
    def __init__(self,owner,image_url):
        super().__init__(owner)
        self.image_url = image_url

    def display(self):
        if self.owner.online:
            pic = mpimg.imread(self.image_url)
            plt.imshow(pic)
            plt.show()
            print("Shows picture")
    def __str__(self):
        return f"{self.owner.name} posted a picture\n"


class TextPost(Post):
    def __init__(self,owner,text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        result = f"{self.owner.name} published a post:\n\"{self.text}\"\n"
        return result