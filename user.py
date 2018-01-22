class User:
    '''
    class that creat new instances of user
    '''
    create_user = []

    def __init__(self, first_name, second_name, password):

        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    # def save_details(self):
    #     '''
    #     save_details method saves details object into details
    #
    #     '''
    #     Details.create_details.append(self)
    #
    # def delete_details(self):
    #     '''
    #     delete_details method deletes a saved contact from details
    #
    #     '''
    #     Details.create_details.remove(self)
    #
    # @classmethod
    # def find_by_name(cls, account_name):
    #     '''
    #     method that in a name and return a name that matches that name
    #
    #     Args:
    #         name: account_name to search for
    #     Returns :
    #         Contact of person that matches the name.
    #     '''
    #     for detail in cls.create_details:
    #         if detail.account_name == account_name:
    #             return detail
    #
    # @classmethod
    # def details_extist(cls, account_name):
    #     '''
    #     method that check if details exists
    #
    #     Args:
    #         name: account_name to search if it exists
    #     Returns :
    #         Boolean: true or false depending if the account_name details_exists
    #     '''
    #     for details in cls.create_details:
    #         if details.account_name == account_name:
    #             return True
    #         return False
    #
    # @classmethod
    # def display_details(cls):
    #     '''
    #     method that returns the create details
    #     '''
    #     return cls.create_details
