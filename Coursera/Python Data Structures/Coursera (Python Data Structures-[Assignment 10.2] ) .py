name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
word = list()
count = dict()
for line in fh:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        pos = line.find(':')
        hour = line[pos-2:pos]
        word.append(hour)
for key in word:
    count[key]=count.get(key,0)+1
for k,v in sorted(count.items()):
    print(k,v)