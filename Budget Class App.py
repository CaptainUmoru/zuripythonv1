class leanBudget:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self):
        return "This is a deposit method."

    def check_balance(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass



category = leanBudget("Unto God", 50000)
category_1 = leanBudget("Clothes", 5000)
category_2 = leanBudget("Internet", 30,000)
category_3 = leanBudget("Transportation", 15000)
category_4 = leanBudget("Food", 25000)

print(category.deposit())
