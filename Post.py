import User

class Post:

    def __init__(self,owner):
        self.isChanged = False
        self.owner = owner
        # self.likes = []
        # self.comments = []

    def like(self,user):
        self.isChanged = True
        # self.likes.append(user)
        User.ManageUsers.notifyUser(user,"Like")

    def comment(self,user,comment_text):
        self.isChanged = True
        # self.comments.append(user)
        User.ManageUsers.notifyUser(user,"Comment",comment_text)

class PostFactory:
    @staticmethod
    def CreatePost(type,owner,text,price,location):
        if type == "Text":
            return TextPost(owner=owner,text=text)
        elif type == "Image":
            return ImagePost(owner=owner,text=text)
        elif type == "Sale":
            return SalePost(owner=owner,product=text,price=price,location=location)

class SalePost(Post):
    def __init__(self,owner,product,price,location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.sold = False


    def discount(self,quantity,user_password):
        new_price = self.price - (self.price*(quantity/100))
        User.ManageUsers.saleUpdate(self,new_price,user_password)

    def sold(self,user_password):
        self.sold = True
        User.ManageUsers.saleUpdate(self, -1, user_password)
        pass

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
        pass