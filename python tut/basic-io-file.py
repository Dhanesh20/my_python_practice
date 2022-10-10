"flie io basics"
"""
"r"- open file for reading -default
"w"- open file for writing
"x"- create file if not exists
"a"- add more content to a file
"t"- text mode- default
"b"- binary mode
"+"- read and write
"""
# open("dk.txt") #nothing will show in output therefore
# f = open("dk.txt")  #proper syntax to open and read the file
# content = f.read()
# print(content)
# f = open("dk.txt","rt")  #using default mode which are only "r"and"t
# content = f.read()
# print(content)
# f = open("dk.txt","rt")  #using the characters f.read(5) only read first five character you can change the number
# content = f.read(5)       #for this output will be "Today"
# print(content)
f = open("dk.txt","rt")
# content = f.read()
# for line in f:      #Today is the great day
#                      # I will make myself happy
#                       # You are chosen
#     print(line,end="")
print(f.readlines()) #output  ['Today is the great day\n', 'I will make myself happy\n', 'You are chosen']
f.close()  #every we open must close at  the end