
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
    # End __init__() 


    def __str__(self):
        width = 30

        # Construct summary headline 
        header = []
        title = str(self.category)
        title_len = len(title)
        star_num = (width - title_len) // 2
        header.append('*' * star_num)
        header.append(title)
        header.append('*' * star_num)
        headline  = ''.join(header)

        # Headline is 29 in length when title_len is odd  
        # so fix it. 
        if len(headline) < width:
            headline += '*'

        # Do entries 
        entries = ''
        for entry in self.ledger:
            descr = entry['description'][:23]
            amnt = entry['amount']
            entries += '\n'+''.join([descr,
                                     f'{amnt:.2f}'.rjust(width-len(descr))
                                    ])

        # Get total  
        total = '\nTotal: ' + str(self._total())

        return '\n' + headline + entries + total
    # End __str__() 


    def _total(self):
        tot = 0
        for entry in self.ledger:
            tot += entry['amount']
        return tot
    # End _total() 


    def check_balance(self):
        return self._total()
    # End check_balance() 


    def check_funds(self, amount):
        balance = self.check_balance()
        if amount > balance:
            return False
        return True
    # End check_funds() 


    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    # End deposit() 


    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        return False
    # End withdraw() 


    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_cat.category}')
            other_cat.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
    # End transfer() 
# End class Category 


def create_spend_chart(categories):
    #  Calculate total & get percentages list  
    spent = []
    for cat in categories:
        tot = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                tot += entry["amount"]
        spent.append(abs(tot))
    total_amount = sum(spent)

    percentages = []
    for amount in spent:
        percentages.append(int((amount/total_amount) * 10) * 10)

    # Do chart from percentages 
    chart = "Percentage spent by category\n"
    for percent in range(100, -1, -10):
        chart += str(percent).rjust(3) + "|"
        for p in percentages:
            if p >= percent:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Do line 
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find longest category name 
    max_height = 0
    for cat in categories:
        height = len(cat.category)
        if height > max_height:
            max_height = height

    # Put category names in columns  
    for i in range(max_height):
        chart += "     "
        for cat in categories:
            if i < len(cat.category):
                chart += cat.category[i] + "  "
            else:
                chart += "   "
        if i < max_height - 1:
            chart += "\n"

    print(chart)
# End create_spend_chart() 


# Some tests 
# FreeCodeCamp examples 
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
#print(food)
#print(clothing)

# My own tests
test = Category('Test')
test.deposit(500, 'Test deposit')

test2 = Category('Test 2')
test2.deposit(2000, 'For transfer')
test2.transfer(1000, test)

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
food.withdraw(50.75, "restaurant")

clothing.deposit(500, "initial deposit")
clothing.withdraw(100, "jeans")

auto.deposit(1000, "initial deposit")
auto.withdraw(200, "car repair")

category_list = [food, clothing, auto]
create_spend_chart(category_list)

print(food)
print(clothing)
print(auto)
#print(test)
#print(test2)
