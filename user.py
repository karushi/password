class User:
    '''
    class that creat new instances of user
    '''
    create_user = []

    def __init__(self, first_name, second_name, password):

        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user object into user

        '''
        User.create_user.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved contact from user

        '''
        User.create_user.remove(self)

    @classmethod
    def find_by_name(cls, first_name, second_name, password):
        '''
        method that in a name and return a name that matches that name

        Args:
            name: first_name to search for
        Returns :
            User of person that matches the name.
        '''
        for detail in cls.create_user:
            if detail.first_name == first_name:
                return detail

    @classmethod
    def user_extist(cls, first_name, second_name, password):
        '''
        method that check if user exists

        Args:
            name: account_name to search if it exists
        Returns :
            Boolean: true or false depending if the account_name user_exists
        '''
        for user in cls.create_user:
            if user.first_name == first_name:
                return True
            return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the create user
        '''
        return cls.create_user
