#!/opt/local/bin/python
from __future__ import print_function

with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

#print(lines)

miss = 0
hit = 0
fuckup = 0
print(len(lines))
looped = 0

height = len(lines)

def checktree(x,line):

    isatree=False
    if line[x] == ".":
        #print("Not a tree")
        isatree = False
    elif line[x] == "#":
        #print("Tree")
        isatree = True
    else:
        print("aliens")
        isatree = False
    return(isatree)

def printspot(line,lookingfor):

    for char in range(0,len(line)):
        if char == lookingfor:
            print('\033[1m\033[91m%s\033[0m' % line[char], end='')
        else:
            print(line[char], end='')




tests = {
    '1': { 'x': 1, 'y': 1 },
    '2': { 'x': 3, 'y': 1 },
    '3': { 'x': 5, 'y': 1 },
    '4': { 'x': 7, 'y': 1 },
    '5': { 'x': 1, 'y': 2 }
}

running_score = 1

for test in tests:
    print("Running test {} - x_step = {}, y_step = {}".format(test,tests[test]['x'],tests[test]['y']))
    my_x = 0
    my_y = 0
    thistest_hit = 0
    thistest_miss = 0
    
    for i in range(0,height):
        line = lines[i]
        if my_x > len(line):
            print("whatthefuck")
        printspot(lines[my_y],my_x)
        ThereATree = checktree(my_x,lines[my_y])
        if ThereATree:
            hit += 1
            thistest_hit +=1
        else:
            miss += 1
            thistest_miss +=1
        my_y += tests[test]['y']
        my_x += tests[test]['x']
        if my_x > len(line)-1:
            #print("tooooo wide, looping")
            my_x = my_x - len(line)
            looped += 1
        if my_y > height:
            print("ya went too far laddy, back up")
            break

        print('i = {}, y = {}, x = {}'.format(i,my_y, my_x))

    print("Trees:   %s" % thistest_hit)
    print("Misses:  %s" % thistest_miss)
    running_score = running_score * thistest_hit
    print("Running score:  %s" % running_score)



print("Trees:   %s" % hit)
print("Misses:  %s" % miss)
print("Loops:   %s" % looped)
print("Total score: %s" % running_score)
