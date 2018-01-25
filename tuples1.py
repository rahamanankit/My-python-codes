name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle :
    if line.startswith("From:") :
        continue
    elif line.startswith("From") :
        words = line.split()
        words = words[5]
        words = words[0:2]
        counts[words] = counts.get(words,0) + 1

for k,v in sorted(counts.items()) :
 print(k,v)
