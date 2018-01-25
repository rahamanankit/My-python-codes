fname = input("Enter file name: ")
fh = open(fname)
lst = list()
x = list()
for line in fh:
 line = line.rstrip()
 x = line.split()
 for i in x:
  if i not in lst:
    lst.append(i)
    lst.sort()
print(lst)
