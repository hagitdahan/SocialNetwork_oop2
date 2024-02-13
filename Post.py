from NotificationService import NotificationService
class Post:

    def __init__(self,owner):
        self.owner = owner

    def like(self,user):
        user.observer.like_post(self.owner.observer)

    def comment(self,user,comment_text):
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
        if permission:
            self.price = self.price - self.price * (quantity / 100)
            NotificationService.notify_discount(self.owner,self.price)

    def sold(self,user_password):
        permission = self.owner.authenticate(user_password)
        if permission:
            self.sold_state = True
            NotificationService.notify_sold(self.owner,self.product,self.price,self.location)

    def __str__(self):
        if(self.sold):
            return f"{self.owner.name} posted a product for sale:\nSold! {self.product}, price: {self.price}, location: {self.location}"
        else:
            return f"{self.owner.name} posted a product for sale:\n{self.product}, price: {self.price}, location: {self.location}"

class ImagePost(Post):
    def __init__(self,owner,image_url):
        super().__init__(owner)
        self.image_url = image_url

    def display(self):
        pass
    def __str__(self):
        pass

class TextPost(Post):
    def __init__(self,owner,text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        result = f"{self.name} published a post:\n{self.text}"
        return result