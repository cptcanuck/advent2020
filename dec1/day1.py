#!/opt/local/bin/python

with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

#print(lines)

for line in lines:
    number = int(line)
    for otherline in lines:
        othernumber = int(otherline)
        for anotherline in lines:
            anothernumber = int(anotherline)
            answer = number + othernumber + anothernumber
            if answer == 2020:
                print("numbers: ",number, othernumber,anothernumber)
                print("answer: ",number * othernumber * anothernumber)
