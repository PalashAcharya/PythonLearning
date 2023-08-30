class Category:
    def __init__(self,cat):
        self.category = cat
        self.total = 0
        self.ledger = []
        self.withdrawn_amount = 0

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
            self.withdrawn_amount = amount
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
        
    def spending_percentage(self):
        og_amount = self.total + self.withdrawn_amount
        percent = (self.withdrawn_amount/og_amount)*100
        return round(percent/10)*10

    def __repr__(self):
        title_string = self.category.center(30,"*")
        ledger_string = str(self.ledger[0]["description"]).ljust(23)+str(self.ledger[0]["amount"]).rjust(7)
        for i in range(1,len(self.ledger)):
            ledger_string = ledger_string+"\n"+str(self.ledger[i]["description"])[0:23].ljust(23)+str(self.ledger[i]["amount"]).rjust(7)
        total_string = "Total:"+str(self.total)
        final_string = title_string+"\n"+ledger_string+"\n"+total_string
        return final_string
    

def create_spend_chart(categories):
    try:
        len(categories)<=4
    except:
        raise ValueError("chart only takes 4 category list")
    y_axis = "Percentage spent by Category"
    spent_percent = []
    footer = ""
    height = max(len(category.category) for category in categories)
    for i in categories:
        spent_percent.append(i.spending_percentage())
    for i in reversed(range(0,110,10)):
        i = str(i).rjust(3)
        y_axis = y_axis+"\n"+str(i)+"|"
        for j in spent_percent:
            if j >=int(i):
                y_axis+= " o  "
            else:
                y_axis+="    "
    for i in range(height):
        footer +="     "
        for j in categories:
            if(i<len(j.category)):
                footer+= j.category[i]+"   "
            else:
                footer+="    "
        footer += "\n"
    x_axis = "    "+"- - - - - - - -"
    chart_string = y_axis+"\n"+x_axis+"\n"+footer.rstrip()
    return chart_string   

obj = Category("Food")
obj2 = Category("Clothes")
obj3 = Category("Movies")
obj4  = Category("games")
obj3.deposit(1000,"Initial deposit")
obj.deposit(1000,"Initial deposit")
obj.withdraw(15,"Groceries")
obj.withdraw(2,"snacks")
obj.transfer(230,obj2)
obj.deposit(1000,"second deposit")
obj.transfer(1000,obj2)
obj2.transfer(500,obj4)
l1 = [obj2,obj,obj3,obj4]
print(create_spend_chart(l1))