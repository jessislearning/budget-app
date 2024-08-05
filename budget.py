class Category:
    def __init__(self):
        self.ledger=[]
        self.balance=0.0

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance+=amount

    def widthdraw(self, amount, description=""):        
        if amount > self.balance:
            self.ledger.append({'amount': amount*-1, 'description': description})
            self.balance+=amount
            return True
        elif amount <= self.balance:
            balance = self.balance
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self):
        pass

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        if amount <= self.balance:
            return True



def create_spend_chart(categories):
    pass
