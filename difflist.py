import sys

args = sys.argv

firstListFile = ""
secondListFile = ""

for x in args:
    if x == "-f":
        firstListFile = args[args.index("-f") + 1]
    
    if x == "-s":
        secondListFile = args[args.index("-s") + 1]

if not firstListFile.strip():
    print("Please define the first wordlist correctly!")
    sys.exit()

if not secondListFile.strip():
    print("Please define the second wordlist correctly!")
    sys.exit()

fll = list()
sll = list()

with open(firstListFile) as f:
  for line in f:
        if not line.strip():
            continue
        fll.append(line)

with open(secondListFile) as f:
  for line in f:
        if not line.strip():
            continue
        sll.append(line)

for i in fll:
    if i in sll:
        sll.remove(i)

print("Final List:")

for i in sll:
    print(i, end="")
