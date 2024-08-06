class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger=[]
        self.balance=0.0
    
    def __str__(self):
        self.title = self.category_name.center(30, "*") + "\n"
        line = ""
        for item in self.ledger:
            description = str(item["description"]).ljust(23)
            amount = str(format(int(item["amount"]),".2f")).rjust(7)
            line += description + amount + "\n"
        total = "Total: " + format(self.balance, ".2f")
        return self.title + line + total
    
    def deposit (self, amount, description=""):
        # writes the amount and description into the ledger and updates the current balance
        self.ledger.append({'amount': amount, 'description': description})
        self.balance+=amount

    def withdraw (self, amount, description=""):    
        # amount to withdraw must be less current balance
        # write amount and description of withdrawal, update balance
        if amount <= self.balance:
            self.ledger.append({'amount': -1*amount, 'description': description})
            self.balance+=-1*amount
            return True
        elif amount > self.balance:
            return False
    
    def get_balance(self):
        # returns the total for current category
        return self.balance
    
    def transfer(self, amount, transfer_cat):
        # withdraw from current category and deposit to another (transfer_cat)
        if amount <= self.balance:
            self.withdraw(amount, f"Transfer to {transfer_cat.category_name}")
            transfer_cat.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        if amount > self.balance:
            return False

def create_spend_chart(categories):
    # list of total amount spent per category
    spent_per_cat=[]
    for category in categories:
        category_total = 0
        for item in category.ledger:
            if item["amount"] < 0:
             category_total += item["amount"]
             print(item["amount"], category.category_name)
        spent_per_cat.append(category_total)

    # sum of total spending
    total_spent = round(sum(spent_per_cat), 2)
    percentages = [int(round(x/total_spent*100, -1)) for x in spent_per_cat]
    return percentages
