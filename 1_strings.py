#  October 25 2015
#  strings support operations that assume a positional ordering among items
import math

firstName = "Zach Timothy Aaron"
# firstName = firstName.replace(" ","") # object.replace(); replace target string or remove spaces
length = len(firstName) # len() - length of firstname variable
print(firstName, length)
print("First [index]" + firstName[0])
# for letter in range(0,len(firstName)):
#     print(firstName[letter])

print("LAST [index] of firstName: " + firstName[-2])
print("SLICING STRING: firstName[0:4] " + firstName[0:4])
print("SLICING STRING: firstName[6:10] " + firstName[5:12])
print("SLICING STRING: firstName[14:19] " + firstName[13:18])
print("SLICING STRING: firstName[:-8] " + firstName[4:-5])
print("-----------------------------------------------------")
print((firstName[0:4] + "\n") * 3 )
print("-----------------------LISTS-------------------------")

profession = 'programmer'

lookString = profession.find('p') #find the offset of a string
# replace first parameter with the second parameter
# we are not changing the original string but creating new string because
# string are immutable(not changeable)

lookString = profession.replace('p','PPP')
print(lookString)

line = "zach-timothy-aaron"
nameString = line.split('-')
print(len(nameString)) #length of nameString lists
print(nameString) #lists of nameString
for name in range(0,len(nameString)):
    print(nameString[name].upper())

greetings = "{0} {1}".format("Hello","Python") #formatting strings
print(greetings)

numbers = "{:,.2f}".format(296639.45)
print(numbers)
PI = "%.2f" % (math.pi) # rounding off digits 2 decimal places

print(PI)

import re
fewTexts = "http://horizons.com"

output = re.match("(.*)://(.*).(com)",fewTexts)

print(output.group(3))
fewTexts = fewTexts.replace(output.group(2),'nox') # change the horizons to nox, (I cracked it SO!)
print(fewTexts)

directory = 'usr/home:ztimaron~kiosk:=fork'
directoryOutput = re.split('[/:~=-]',directory)
print(directoryOutput)

# print("SLICING STRING: firstName[0:4] " + firstName[0:4])
