"""
Account model file

Author: Diego Arango - @darango91
"""

from src.utils import get_colombia_current_trm


class Account:
    """
    Account class
    """
    user_id = None
    pin = None
    balance = None
    is_valid = False

    def __init__(self, args):
        self.user_id = args.get("user_id")
        self.pin = args.get("pin")
        self.balance = args.get("balance")
        self.is_valid = True

    def validate_account(self, user_id, pin):
        """
        Validate the account against given user_id and pin
        :param user_id: string, identifier for the user
        :param pin: int, a four digits pin
        :return: True or False if the data is valid
        """
        return self.user_id == user_id and self.pin == pin

    def get_balance(self):
        """
        Get the account balance
        :return: balance, float value containing the account current balance
        """
        return self.balance

    def deposit(self, amount, dollars=False):
        """
        Deposit money in the account
        :param amount: int, the money to be deposited in the account
        :param dollars: boolean tells if this transaction is in dollars
        :return: the new account balance
        """
        if dollars:
            amount = amount*get_colombia_current_trm()

        self.balance += amount
        return self.balance

    def withdraw(self, amount, dollar=False):
        """
        Withdraw money from the account
        :param amount:
        :param dollar: boolean tells if this transaction is in dollars
        :return: the new account balance
        """
        if dollar:
            amount = amount*get_colombia_current_trm()
        self.balance -= amount

        return self.balance
