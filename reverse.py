n = int(input('Enter a no:'))
r = 0
while n>0:
 t = n % 10
 r = (r * 10) + t
 n = n // 10
print(r)
