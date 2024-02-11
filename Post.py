import User

class Post:

    def __init__(self,owner,password):
        self.owner = owner
        self.__password=password

    def like(self,user):
        #edit the post in publisher
        pass

    def comment(self,user,comment_text):
        # edit the post in publisher
        pass

class PostFactory:
    @staticmethod
    def CreatePost(password,type,owner,text,price,location):
        if type == "Text":
            return TextPost(owner=owner,password=password,text=text)
        elif type == "Image":
            return ImagePost(owner=owner,password=password,text=text)
        elif type == "Sale":
            return SalePost(owner=owner,password=password,product=text,price=price,location=location)

class SalePost(Post):
    def __init__(self,owner,password,product,price,location):
        super().__init__(owner,password)
        self.product = product
        self.price = price
        self.location = location
        self.sold = False


    def discount(self,quantity,user_password):
        #edit post in publisher
        pass

    def sold(self,user_password):
        # edit post in publisher
        pass

    def __str__(self):
        if(self.sold):
            return f"{self.owner.name} posted a product for sale:\nSold! {self.product}, price: {self.price}, location: {self.location}"
        else:
            return f"{self.owner.name} posted a product for sale:\n{self.product}, price: {self.price}, location: {self.location}"

class ImagePost(Post):
    def __init__(self,owner,password,image_url):
        super().__init__(owner,password)
        self.image_url = image_url

    def display(self):
        pass
    def __str__(self):
        pass

class TextPost(Post):
    def __init__(self,owner,password,text):
        super().__init__(owner,password)
        self.text = text

    def __str__(self):
        pass