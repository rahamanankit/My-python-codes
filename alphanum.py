s = input('Enter a word:')
lst = list()
if s.isalnum() == True:
    for i in s:
        lst.append(i)
    print(lst)
else:
    print('The given string is not alphanumeric')