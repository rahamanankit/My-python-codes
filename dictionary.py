stud = {'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}
s = 0
for k,v in stud.items():
    s += v
    print('The name of the student is:',k,'and marks is',v)
avg = s/5
print('The class average of this course is:',avg)
lst = sorted(stud.values(),reverse=True)
print("The top two scores are:",lst[0],lst[1])