#!/opt/local/bin/python
good_password=0
bad_password=0
short_password=0
total_checked=0

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

#print(lines)

for line in lines:

    total_checked += 1
    splitline = line.split(" ")

    #print("##############", splitline)

    if len(splitline) != 3:
        print("bad line - %s" % splitline)

    #can I split this directly into 2 variables (spot1, spot2)?
    spots  = splitline[0].split("-")
    spot1  = int(spots[0])
    spot2  = int(spots[1])
    characters = splitline[1].split(":")
    character = characters[0]
    password = splitline[2]

    #print("Spot1: %s, Spot2: %s, Character: %s, Password: %s" % (spot1, spot2, character, password))

    if (spot1 > len(password)) or (spot2 > len(password)):
        print("password %s SHORT (requesting spots %s and %s, looking for char %s password is %s long)" % (password, spot1, spot2, character, len(password)))
        short_password += 1    
    else:
#        print("Looking for %s" % character)
#        print("Password length = %s" % len(password))
#        print("Spot[%s] = %s" % (spot1, password[spot1-1]))
#        print("Spot[%s] = %s" % (spot2, password[spot2-1]))

        thisOneIsGood = False
        if ((password[spot1-1] == character) and (password[spot2-1] != character)) or ((password[spot2-1] == character) and (password[spot1-1] != character)):
            print("password %s ok (requesting spots %s and %s, looking for char %s password is %s long)" % (password, spot1, spot2, character, len(password)))
            good_password += 1
        else:
            print("password %s BAD (requesting spots %s and %s, looking for char %s password is %s long)" % (password, spot1, spot2, character, len(password)))
            bad_password += 1

        #if password[int(goodspots[0])-1] == character[0]:
        #    if password[int(goodspots[1])-1] == character[0]:
        #        print("password %s ok (requesting spots %s and %s, looking for char %s password is %s long)" % (password, goodspots[0], goodspots[1], character[0], len(password)))
        #        good_password += 1
        #else:
        #    print("password %s BAD (requesting spots %s and %s, looking for char %s password is %s long)" % (password, goodspots[0], goodspots[1], character[0], len(password)))
        #    bad_password += 1

print(" ")
print("##################### ")
print("Total good passwords: %s" % good_password)
print("Total bad passwords: %s" % bad_password)
print("Total short passwords: %s" % short_password)
print("Total checked: %s" % total_checked)
