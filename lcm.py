n1 = int(input('Enter the first no.'))
n2 = int(input('Enter the second no.'))
x = n1
y = n2
while n1!=n2 :
 if n1>n2 :
  n1=n1-n2
 else:
  n2=n2-n1
print('LCM is:',(x * y)/n1)
