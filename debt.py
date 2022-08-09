debt = int(input('借金>'))
interest_rate = float(input('年利率(%)>'))
amount = int(input('返済額>'))
total = 0
month = 0
while debt > amount:
    month += 1
    debt = debt*(1 + interest_rate/12/100) - amount
    print(str(month)+'月:返済額',amount,'円','残り',int(debt),sep='')
    total += amount
month += 1
debt = debt*(1 + interest_rate/12/100)
total += amount
print(str(month)+'月: 返済額',int(debt),'円　これで完済。　返金総額: ',int(total),'円',sep='')