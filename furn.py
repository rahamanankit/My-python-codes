furniture = ['Sofa Set','Dining Table','T.V. Stand','Cupboard']
cost = [20000,8500,4599,13920]
f = input('Enter the name of the furniture you want to order:')
q = int(input('Enter the no. of items you want to purchase:'))
if f in furniture and q > 0:
    index = furniture.index(f)
    c = cost[index]
    amount = c*q
    print('The total cost is =',amount)
else:
    print('Invalid data entered')
    amount = 0
    print('The total cost is =',amount)
    