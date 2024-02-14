from User import User

class SocialNetwork(object):
    """
    this class implement Singletone design pattern for having only one instance
    from this class, this class has a name and array of users
    """

    __instance = None

    def __new__(cls,name):
        """
        this method implement the Singletone by checking if there is an instance of
        this class in the static data member, if there is return it, if not create
        new one by __init__ method, save it and return it
        :param name: name of the Social Network
        """
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
            cls.__instance.__initialized = False
            print(f"The social network {name} was created!")
        return cls.__instance
    def __init__(self,name):
        """
        if the __instance is not intialized, initialize it, else do nothing
        :param name:
        """
        if not SocialNetwork.__instance.__initialized:
            self.name = name
            self.users=[]
            SocialNetwork.__instance.__initialized = True

    def contains(self,username):
        """
        this method checks id there is a user with the username string.
        :param username: username string
        :return: if there is return user (user instance) else return None
        """
        for user in self.users:
            if username == user.name:
                return user
        return None

    def sign_up(self,username,password):
        """
        this method checks if the username and password is legal, then create a new user and
        add it to the users
        :param username: username string
        :param password: password string
        :return: if OK, the new user (user instance) else, None
        """
        if(self.contains(username)==None and len(password)>=4 and len(password)<=8):
            new_user = User(username,password)
            self.users.append(new_user)
            return new_user


    def log_out(self,username):
        """
        this method set the status of user to offline, and prints to the screen
        :param username: username string
        :return:
        """
        tmp_user=self.contains(username)
        if tmp_user is not None:
            tmp_user.online=False
            print(f"{username} disconnected")

    def log_in(self,username,password):
        """
        this method check permission to log in and
        set the status of user to online, and prints to the screen
        :param username: username string
        :param password: password string
        :return:
        """
        tmp_user=self.contains(username)
        if tmp_user is not None and tmp_user.authenticate(password):
            tmp_user.online=True
            print(f"{username} connected")


    def __str__(self):
        """
        :return: the string representation of the SocialNetwork's Users
        """
        result = f"{self.name} social network:\n"
        for user in self.users:
            result += user.__str__() + "\n"
        return result
