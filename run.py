#!/usr/bin/env python3.5
from password import Details
from details import Details

    def create_details(account_name, account_password):
        '''
        function to create details
        '''
        new_details = Details(account_name, account_password)
        return new_details

    def save_details(details):
        '''
        Function to save details
        '''
        details.save_details()

    def del_details(details):
        '''
        Function to delete Details
        '''
        details.delete_details()

    def find_details(name):
        '''
        Function that finds  details by name and return the details
        '''
        return Details.find_by_name(name)

    def check_existing_details(name):
        '''
        Function that check if details with that name and return boolean
        '''
        return Details. details_exist(number)

     def main():
        print ("welcome to your details whats is your name")
        user_name = input()

        print ("Hello{user_name} what would you like to do?")

        print('\n')

        while True:
            print ("use these short codes: cd - create a new details, dd -display details, fd - find details")

            short_code = input().lower()
            if short_code == 'cd':
                   print ("New_Details")
                   print("-"*70)

                   print ("account_name")
                   account_name = input()

                   print ("account_password")
                   account_password = input()

                   save_details(create_details(account_name, account_password)) # creat and save new details

                   print ('\n')
                   print ("New_Details{account_name}{account_password}created")

                   print ('\n')

        elif short_code == 'dd':

            if display_details():
                   print ("here is a list of all my details")
                   print('\n')
                   for details in display_details():
                    print("{account_name}{account_password}")

                    print('\n')
                else:

                    print('\n')
                    print("Enter the name you want to seach for")

                     search_name = input()
                            if check_existing_details(search_name):
                                    search_details= find_deataisl(search_name)
                                    print(f"{search_details.account_name} {search_account_password}")
                                    print('-' * 60)

                                    print(account_name.......{search_deatails.account_passwor}")
                                    print(f"account_name.......{search_details.name}")
                            else:
                                    print("That details does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
