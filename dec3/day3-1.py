#!/opt/local/bin/python
from __future__ import print_function

with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

#print(lines)

miss = 0
hit = 0
fuckup = 0
#print(lines[1][1])
#print(len(lines[1]))
#print(len(lines[2]))
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
            print(line[char], end=''),



my_x = 0
my_y = 0

for i in range(0,height):

    print("####loc: ",my_y,my_x,len(line))
    if my_x > len(line):
        print("whatthefuck")
    #print(my_x,my_y)
    #print(lines[my_y])
    printspot(lines[my_y],my_x)
    ThereATree = checktree(my_x,lines[my_y])
    if ThereATree:
        hit += 1
    else:
        miss += 1
    my_y += 1
    my_x += 3
    print(" ")
    print("pm loc: ",my_y,my_x,len(line))
    #for this test data, line length is 32, array is 0-31
    #ex1: my_x was 27, moved 3 right, now 30 - OK
    #ex2: my_x was 29, moved 3 right, now 32 - LOOP around to 0
    #ex3: my_x was 28, moved 3 right, now 31 - OK
    #ex4: my_x was 31, moved 3 right, now 34 - LOOP around to 2
    if my_x > len(line)-1:
        #print("tooooo wide, looping")
        my_x = my_x - len(line)
        looped += 1

print("Trees:   %s" % hit)
print("Misses:  %s" % miss)
print("Loops:   %s" % looped)
