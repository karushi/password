class Details:
    '''
    class that creat new instances of details.
    '''
    create_details = []

    def __init__(self, account_name, account_password):

        self.account_name = account_name
        self.account_password = account_password

    def save_details(self):
        '''
        save_details method saves details object into details

        '''
        Details.create_details.append(self)

    def delete_details(self):
        '''
        delete_details method deletes a saved contact from details

        '''
        Details.create_details.remove(self)
