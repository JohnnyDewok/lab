class Account:
    def __init__(self, name):
        '''
        :param name: 001-John
        Enter a three-digit number followed with a "-" and the account holder's first name
        every account starts at zero.
        '''

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        '''
        :param amount: Enter a POSITIVE number to be added to the account selected
        :return: True or False depending on entered values.
                If a negative deposit (i.e. -5), the sequence will not accept it and return FALSE
        '''

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        '''
        :param amount: Enter a POSITIVE number to be added to the account selected
        :return: True or False depending on entered values.
                If a negative deposit (i.e. -5), the sequence will not accept it and return FALSE
        '''

        if amount > 0 and amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    def __str__(self):
        return f'name = {self.__account_name}, account balance = {self.__account_name}'