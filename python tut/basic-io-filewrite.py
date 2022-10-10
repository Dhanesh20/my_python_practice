#file writing
# f=open("dk1.txt","w")           #This will create new file or if the file already created than it will remove the old content and write the new one
# f.write("Today is the rainy day")
# f.close()
# f=open("dk1.txt","a")            #This "a"will append the content every we executing this program
# f.write("Today is the rainy day")
# f.close()
# f=open("dk1.txt","a")
# a=f.write("Today is the rainy day")     #tells me how many character is in the text file
# print(a)
# f.close()


#Handle read and write
# f=open("dk1.txt","r+")
# print(f.read())
# f.write("\nThank you")

#Tell and Seek commands
# f = open("dk1.txt")
# print(f.tell())             #"Tell command " tells the at which point character in
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()
# f = open("dk1.txt")
# print(f.tell())
# print(f.readline())
# print(f.seek(45))               #Seek command reset the pointer
# print(f.readline())
# print(f.tell())
# f.close()


#Using With block
# with open("dk.txt") as f:
#     a=f.read(5)
#     print(a)



# f = open("dk.txt","rt")
# print(f.readlines())
# print(f.readline())
#f.close()