text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
pos = text.find('0')
tval = text[pos:length]
val = float(tval)
print(val)
