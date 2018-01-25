name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for lines in handle :
    if lines.startswith("From "):
        lines = lines.split()
        lines = lines[1]
        count[lines]=count.get(lines,0) + 1

bigCount = None
bigWord = None
for word,sender in count.items():
    if bigCount == None or sender > bigCount :
     bigWord = word
     bigCount = sender
print(bigWord,bigCount)
 
