"""
Utilities file

Author: Diego Arango - @darango91
"""


def get_colombia_current_trm():
    """
    Returns the current day TRM
    TODO: find (or create) an API for the present day trm in colombia, for now a fixed value
    :return: float, the day trm
    """
    return 3525.25


class SwitchAction:
    """
    Action switcher
    """
    mongo = None
    account = None

    def switch(self, action, **kwargs):
        return getattr(self, str(action))(**kwargs)

    def validate_account(self, **params):
        return self.account.is_valid

    def get_account_balance(self, **params):
        return self.account.get_balance()

    def withdraw_in_dollars(self, **params):
        dollars = params.get("money").get("value")

        self.account.withdraw(dollars, dollar=True)

        self.mongo.db.accounts.update_one(
            {"user_id": self.account.user_id},
            {"$set": {"balance": self.account.get_balance()}}
        )
        return self.account.balance

    def withdraw_in_pesos(self, **params):
        pesos = params.get("money").get("value")

        self.account.withdraw(pesos)

        self.mongo.db.accounts.update_one(
            {"user_id": self.account.user_id},
            {"$set": {"balance": self.account.get_balance()}}
        )
        return self.account.balance

    def deposit_money(self, **params):
        pesos = params.get("money").get("value")

        self.account.deposit(pesos)

        self.mongo.db.accounts.update_one(
            {"user_id": self.account.user_id},
            {"$set": {"balance": self.account.get_balance()}}
        )
        return self.account.balance


class Validator:
    """
    Custom validator
    """
    account = None

    def validate(self, operator, field_id, value):
        return getattr(self, str(operator))(field_id, value)

    def eq(self, field_id, value):
        """
        Operator - equal
        """
        return self.account.__getattribute__(field_id) == value

    def gt(self, field_id, value):
        """
        Operator - greater than
        """
        return self.account.__getattribute__(field_id) > value

    def gte(self, field_id, value):
        """
        Operator - Greater than or equal
        """
        return self.account.__getattribute__(field_id) >= value

    def lt(self, field_id, value):
        """
        Operator - Lower than
        """
        return self.account.__getattribute__(field_id) < value

    def lte(self, field_id, value):
        """
        Operator - Lower than or equal
        """
        return self.account.__getattribute__(field_id) <= value
