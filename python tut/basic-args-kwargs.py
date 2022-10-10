#args and kwargs
# def function_name_print(a,b,c,d,e):   #without args and kwargs
#     print(a,b,c,d,e)
# function_name_print("Dk","Sahi","hk","Sar","Se")
#example
# def funargs(*args):
#     for item in args:
#         print(item)
#
# d = ["Dk","Sahi","hk","Sar","Se"]
# funargs(*d)
#example with normal
def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)

d = ["Dk","Sahi","hk","Sar","Se","ddot","program"]
normal ="I am normal "
funargs(normal,*d)

#example of **kwargs
har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)