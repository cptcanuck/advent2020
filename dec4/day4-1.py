#!/opt/local/bin/python

data = []
test = {}
i = 0
with open('input.txt') as f:
    for line in f:
        print(line),
        if line == "\n":
            #print("Empty line")
            i += 1
            test[i] = data
            data = []
        else:
            data.append(line.split(' '))

good_data = {}
for thing in test:
    for item in test[thing]:
        good_data[thing].append('item')

print("Data #####")
print test

print good_data


