#recursive
# def print2(str1):       #recurisve error
#     print2(str)
#     print("this is"+str)
# print2("dk")

# def factorial_iterative(n):
#     """
#     :param n:Integer
#     :return:n*n-1*n-2*n-3*.....1
#     """
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# number=int(input("Enter the no."))
# print("Factorial using iterative method",factorial_iterative(number))
# def factorial_recursive(n):
#     """
#     :param n:Integer
#     :return:n*n-1*n-2*n-3*.....1
#     """
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
#
# number=int(input("Enter the no."))
# print("Factorial using recursive method",factorial_recursive(number))
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("Enter the no."))
print("fibonacci",fibonacci(number))