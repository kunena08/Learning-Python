import re

#   x = re.compile(r'REGEX') -> creates a re object
#   mo = x.search("STRING") -> creates an object
# after searching the STRING for matched REGEX
#   mo.group() -> returns the matched STRING

"""

    Import the regex module with import re.

    Create a Regex object with the re.compile() function. (Remember to use a raw string.)

    Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

    Call the Match object’s group() method to return a string of the actual matched text.


"""

# REGEX test @: https://www.regexpal.com/

# examples
# 0: grouping regex with () and escaping \( when
#there's a need for matching actual '('.
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My phone number is (123) 555-6622.")
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.groups())

print('\n')
# 1: matching multiple groups with the Pipe '|' (means OR)
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())
mo2 = heroRegex.search("Tina Fey and Batman.")
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batmobile lost a wheel.")
print(mo.group())
print(mo.group(1))

print('\n')
# 2: optional matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search("The Adventures of Batman!")
print(mo1.group())
mo2 = batRegex.search("The Adventures of Batwoman!")
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search("My number is 415-555-4242")
print(mo1.group())
mo2 = phoneRegex.search("My number is 555-4242")
print(mo2.group())

print('\n')
# 3:
