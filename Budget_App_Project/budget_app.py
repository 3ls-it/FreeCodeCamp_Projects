
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []


    def __str__(self):
        # Construct summary headline 
        header = []
        title = str(self.category)
        title_len = len(title)
        width = 30

        star_num = (width - title_len) // 2
        header.append('*' * star_num)
        header.append(title)
        header.append('*' * star_num)
        headline  = ''.join(header)

        # Headline is 29 in length when title_len is odd  
        if len(headline) < width:
            headline += '*'

        # do entries 
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


    def _total(self):
        tot = 0
        for entry in self.ledger:
            tot += entry['amount']
        return tot


    def check_balance(self):
        return self._total()


    def check_funds(self, amount):
        balance = self.check_balance()
        if amount > balance:
            return False
        return True


    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        return False


    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_cat.category}')
            other_cat.deposit(amount, f'Transfer from {self.category}')
            return True
        return False


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
#print(test)

#print("")
#print('Deposit $500')
test.deposit(500, 'Test deposit')
#print('Balance: ', test.check_balance())
#print('Withdraw $50')
"""
if test.withdraw(50, 'Test withdrawal'):
    print('Balance: ', test.check_balance())
print('Withdraw $800')
if test.withdraw(800, 'Test withdrawal'):
    print('Balance: ', test.check_balance())
else:
    print('Insufficient funds')
"""

#print("")
test2 = Category('Test 2')
test2.deposit(2000, 'For transfer')
#print(test2)
#print("")
#print('Balance: ', test2.check_balance())
#print('Transfer $1000 to Test')
test2.transfer(1000, test)
#print('Balance: ', test2.check_balance())

#print("")
#print(test)

category_list = [food, clothing, test, test2]


def create_spend_chart(categories):
    for cat in categories:
        print(cat)

create_spend_chart(category_list)
