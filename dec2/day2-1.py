#!/opt/local/bin/python
good_password=0

with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

#print(lines)

for line in lines:

    splitline = line.split(" ")

#    print(splitline)

    if len(splitline) != 3:
        print("bad line - %s" % splitline)

    #can I split this directly into 2 variables (from, to)?
    range = splitline[0].split("-")
    character = splitline[1].split(":")
    password = splitline[2]

    #print("Range: %s to %s  character: %s  password: %s" % (range[0], range[1],character[0],password))

    found_count = 0
    #count characters in password
    for i,letter in enumerate(password):
        if letter == character[0]:
            found_count += 1
    
    #print("Password %s contains %s occurances of %s" % (password, found_count, character[0]))


#    print("DEBUG: found_count: %s   range[0]: %s" % (found_count, range[0]))
# this was annoying had to type the range component because the check was failing on >= but working for <=
#    if found_count >= int(range[0]):
#        print("meets lower bound of %s" % range[0])
#
##    if found_count <= int(range[1]):
#        print("meets uppper bound of %s" % range[1])

    if (found_count >= int(range[0])) and (found_count <= int(range[1])):
#       print "password meets rule"
       good_password += 1


print("Total good passwords: %s" % good_password)
