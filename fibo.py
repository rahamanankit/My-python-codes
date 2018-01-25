a = -1
b = 1
lst = list()
n= (int)(input("Enter the range:"))
for i in range(1,n):
 c=a+b
 a=b
 b=c
 lst.append(c)
print(lst)

