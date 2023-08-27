class Category:
    def __init__(self,cat):
        self.category = cat
        self.total = 0
        self.ledger = []

    def deposit(self,amount,des=""):
        self.total = self.total + amount
        self.ledger.append({"amount":amount, "description":des})

    def check_funds(self,amount):
        if(self.total>amount):
            return True
        else:
            return False

    def withdraw(self,amount,des=""):
        if(self.check_funds(amount)==True):
            self.total = self.total-amount
            self.ledger.append({"amount":-amount,"description":des})
            return True
        else:
            return False
        
    def get_balance(self):
        return self.total
    
    def transfer(self,amount,cat):
        if(self.check_funds(amount)==True):
            self.withdraw(amount,f"Transfer to {cat.category}")
            cat.deposit(amount,f"Transfer from {self.category}")
            return True
        else:
            return True
    def __repr__(self):
        title_string = self.category.center(30,"*")
        ledger_string = str(self.ledger[0]["description"]).ljust(23)+str(self.ledger[0]["amount"]).rjust(7)
        for i in range(1,len(self.ledger)):
            ledger_string = ledger_string+"\n"+str(self.ledger[i]["description"]).ljust(23)+str(self.ledger[i]["amount"]).rjust(7)
        total_string = "Total:"+str(self.total)
        final_string = title_string+"\n"+ledger_string+"\n"+total_string
        return final_string
    
obj = Category("Food")
obj2 = Category("Clothes")
obj.deposit(1000,"Initial deposit")
obj.withdraw(15,"Groceries")
obj.withdraw(2,"snacks")
obj.transfer(230,obj2)
print(obj)