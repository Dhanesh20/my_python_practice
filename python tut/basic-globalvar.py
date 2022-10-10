# Global variable
# l=10 #global- this variable use in below func. as much as time it executed (global scope)
# def func1(n):
#     l=5 #local- if local and global have same name then in function,it first search local variable then global
#     m=6 #local-in function local varible has first priority,local variable not defined outside the function
#     print(l,m)
#     print(n,"I have printed",)
# func1("this is me")
# print(l)
# global could not change from inside the function error will occur.
# you have to take permission
# l=10
# def func1(n):
#     m=8
#     # l=5
#     l=l+45
#     print(l, m)
#     print(n,"I have printed",)
# func1("this is me")
# print(l)
# error occured
# you have to take permission
# l = 10
# def func1(n):
#     m = 8
#     # l=5
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed", )
# func1("this is me")
# print(l)
# def dk():
#     x=40
#     def dhanesh():
#         global x  #global directly go outside the func so x couldn't change output is 40
#         x=85
#     print("before calling dhanesh()",x)
#     dhanesh()
#     print("after calling dhanesh()",x)
# dk()


