# Use the file name mbox-short.txt as the file name
import re
fname = input("Enter file name: ")
fh = open(fname)
numlist = list()
for line in fh:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        for item in stuff:
            s = s + int(item)
print(s)