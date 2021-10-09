class Category:
  def __init__(self, category):
    self.balance = 0
    self.category = category
    self.ledger = []
    self.spent = 0

  def deposit(self, amount, des=''):
    self.ledger.append({"amount": amount, "description": des})
    self.balance += amount
  
  def withdraw(self, amount, des=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": des})
      self.spent += amount
      self.balance -= amount
      return True
    return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

  def get_balance(self):
    return self.balance
  
  def transfer(self, amount, othercat):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {othercat.category}")
      self.spent -= amount
      othercat.deposit(amount, f"Transfer from {self.category}")
      return True
    return False
    
  def __str__(self):
    statement = ''
    statement += self.category.center(30, "*") + '\n'
    
    for i in self.ledger:
      monie = i['amount']
      fixlength = len(str(f'{monie:.2f}')) + 1

      if len(i["description"]) + fixlength >= 30:
        statement += i["description"][0:(30 - fixlength)]
      else:
        statement += i["description"].ljust(30 - fixlength)

      statement += " " + str(f'{monie:.2f}') + '\n'

    statement += f"Total: {self.balance}"
    return statement

def create_spend_chart(categories):
  spentchart = []
  tnames = []
  sum = 0
  finalchart = ""

  for cat in categories:
    spentchart.append(cat.spent)
    sum += cat.spent
    tnames.append(cat.category)

  percentage = []
  for money in spentchart:
    percentage.append(round(money/sum * 100))

  finalchart += "Percentage spent by category" + '\n'

  def barchart(loopindex, pindex):
    if loopindex <= pindex:
      return 'o' + ' ' + ' '
    return ' ' * 3

  for i in range(10,-1,-1):
    finalchart += str(i*10).rjust(3) + '|' + ' '
    
    for y in range(len(percentage)):
      finalchart += barchart(i*10,percentage[y])

    finalchart += '\n'
  
  finalchart += ' ' * 4 + '-' * 3 * len(percentage) + '-' + '\n'
  
  maximum = len(max(tnames, key=len))

  def namechart(namelist, turnindex, letterindex):
    wordlength = len(namelist[turnindex])
    if letterindex <= (wordlength - 1):
      return namelist[turnindex][letterindex] + ' ' + ' '
    return ' ' * 3

  for i in range(maximum):
    finalchart += ' ' * 5

    for y in range(len(tnames)):
      finalchart += namechart(tnames, y, i)
    
    finalchart += '\n'

  return(finalchart[:-1])