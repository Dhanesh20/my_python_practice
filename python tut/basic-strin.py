mystr ="today is the great day"
# print(len(mystr))
# # 22
# print(mystr[0:5])
# # Today
# print(mystr[0:22:2])
# # Tdyi h ra a
# print(mystr[-21:-2])
# # oday is the great d
# print(mystr[::-1])
# # yad taerg eht si yadoT
#print(mystr.isalnum())
# isalnum is func. is the boolean func.output will be true or false.This is func checks if the given string is numeric or not
#print(mystr.isalpha())
#isalpha is func. is the boolean func. output will be true or false.This is func checks if the given string is alpha or not
# print(mystr.endswith("day"))
# print(mystr.count('d'))
print(mystr.capitalize())
# this func. capitalize the first letter
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))
#F-strings
import math

me="Dhanesh"
a1=5
# a= "This is %s %s"%(me,a1)
# a="This is {0} {1}"
# b=a.format(me,a1)
# print(b)
a=f"This is {me} {a1} {math.cos(65)}"
print(a)