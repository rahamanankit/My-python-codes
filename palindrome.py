s1 = input('Enter a string:')
s2 = s1[::-1]
if s1 == s2:
    print('String is palindrome')
else:
    print('String is not palindrome')
print('Actual string is:',s1,'Reversed string is:',s2)
