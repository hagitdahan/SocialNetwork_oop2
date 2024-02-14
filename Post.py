import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Post:
    """
    this class represent a post and has an owner and has two mathods
    """
    def __init__(self,owner):
        self.owner = owner

    def like(self,user):
        """
        this method set like to this post by user.
        :param user: user who liked the post(user instance)
        :return:
        """
        if user.online:
            user.observer.like_post(self.owner.observer)

    def comment(self,user,comment_text):
        """
        this method set comment to this post by user.
        :param user:user who did the comment on this post (user instance)
        :param comment_text: the comment string
        :return:
        """
        if user.online:
            user.observer.comment_post(self.owner.observer,comment_text)

class PostFactory:
    """
    this class implement factory design pattern for post
    """
    @staticmethod
    def CreatePost(type,owner,text,price,location):
        """
        this method
        :param type: the type of post string
        :param owner: the owner of the post user instance
        :param text: URL/product/text content string
        :param price: the price of the product
        :param location: the location of the product
        :return: by the type of the post, call the right class to create the post
        """
        if type == "Text":
            return TextPost(owner=owner,text=text)
        elif type == "Image":
            return ImagePost(owner,text)
        elif type == "Sale":
            return SalePost(owner=owner,product=text,price=price,location=location)

class SalePost(Post):
    """
    this class inherit from Post and has product name, price, location
    and if the product sold or not
    """
    def __init__(self,owner,product,price,location):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.location = location
        self.sold_state = False


    def discount(self,quantity,user_password):
        """
        this method update the price of the product
        :param quantity: the percentage reduction of price
        :param user_password: the password string for permission to edit the post
        :return:
        """
        permission = self.owner.authenticate(user_password)
        if permission and self.owner.online:
            self.price = self.price - self.price * (quantity / 100)
            self.owner.observable.update_discount_post(self.price)

    def sold(self,user_password):
        """
        this method update that the product is sold
        :param user_password: the password string for permission to edit the post
        :return:
        """
        permission = self.owner.authenticate(user_password)
        if permission and self.owner.online:
            self.sold_state = True
            self.owner.observable.update_sold_post()

    def __str__(self):
        """
        :return: the string representation of the post
        """
        if(self.sold_state):
            return f"{self.owner.name} posted a product for sale:\nSold! {self.product}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.owner.name} posted a product for sale:\nFor sale! {self.product}, price: {self.price}, pickup from: {self.location}\n"

class ImagePost(Post):
    """
    this class inherit from Post and has image url
    """
    def __init__(self,owner,image_url):
        super().__init__(owner)
        self.image_url = image_url

    def display(self):
        """
        this method displays the image on the screen print to the screen
        :return:
        """
        if self.owner.online:
            pic = mpimg.imread(self.image_url)
            plt.imshow(pic)
            plt.show()
            print("Shows picture")
    def __str__(self):
        """
        :return: string representation of the post
        """
        return f"{self.owner.name} posted a picture\n"


class TextPost(Post):
    """
    this class inherit from Post and has text content
    """
    def __init__(self,owner,text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        """
        :return: the string representation of the post
        """
        result = f"{self.owner.name} published a post:\n\"{self.text}\"\n"
        return result