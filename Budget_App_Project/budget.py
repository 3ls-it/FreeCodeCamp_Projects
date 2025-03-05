class Category:

    def __init__(self, category):
        self.name = category
        self.ledger = []
        self.balance = 0.00
    # End __init__() 


    def __str__(self):
        width = 30

        # Construct summary headline 
        header = []
        title = str(self.name)
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
        total = '\nTotal: ' + str(self.balance)

        return headline + entries + total
    # End __str__() 


    def get_balance(self):
        return self.balance
    # End get_balance() 


    def check_funds(self, amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        return False
    # End check_funds() 


    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': float(amount), 'description': description})
        self.balance += float(amount)
    # End deposit() 


    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': (amount * -1.00), 'description': description})
            self.balance -= amount
            return True
        return False
    # End withdraw() 


    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_cat.name}')
            other_cat.deposit(amount, f'Transfer from {self.name}')
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
            if entry['amount'] < 0:
                tot += entry['amount']
        spent.append(abs(tot))
    total_amount = sum(spent)

    percentages = []
    for amount in spent:
        percentages.append(int((amount/total_amount) * 10) * 10)

    # Do chart from percentages 
    chart = 'Percentage spent by category\n'
    for percent in range(100, -1, -10):
        chart += str(percent).rjust(3) + '|'
        for p in percentages:
            if p >= percent:
                chart += ' o ' 
            else:
                chart += '   ' 
        chart += ' \n'

    # Do line at bottom 
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # Find longest category name 
    max_height = 0
    for cat in categories:
        height = len(cat.name)
        if height > max_height:
            max_height = height

    # Put category names in columns  
    for i in range(max_height):
        chart += '     '
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + '  ' 
            else:
                chart += '   ' 
        if i < max_height - 1:
            chart += '\n'
    return chart
# End create_spend_chart() 
