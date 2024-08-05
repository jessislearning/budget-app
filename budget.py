class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger=[]
        self.balance=0.0
        
    def deposit (self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance+=amount

    def withdraw (self, amount, description=""):        
        if amount <= self.balance:
            self.ledger.append({'amount': -1*amount, 'description': description})
            self.balance+=amount
            return True
        elif amount > self.balance:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, transfer_cat):
        self.withdraw(amount, f"Transfer to {transfer_cat.category_name}")
        transfer_cat.deposit(amount, f"Transfer from {self.category_name}")

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        if amount > self.balance:
            return False


def create_spend_chart(categories):
    pass
