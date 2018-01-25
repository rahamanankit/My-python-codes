a = input("Enter a word:")
b = a[::-1]
if a == b:
    print("The word is palindrome")
else:
    print("Not a palindrome")
print("Actual string:",a)
print("Reversed string:",b)
