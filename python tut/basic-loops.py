#"For loop and While Loop"
# for loop example 1
# list1 = ["Harry", "Dairy", "Ferry", "Carry"]
# print(list1[0],list1[1])  #this is to show difference between simple print statment and the loop statment
# for items in list1:
#     print(items)
#for loop example 2
# list1 = [["Harry",1], ["Dairy",2], ["Ferry",34],["Carry",4852]]
# for items,candy in list1:
#     print(items,"has candy",candy)
#for loop example 3
# list1=[["Harry",1], ["Dairy",2], ["Ferry",34],["Carry",4852]]
# dict1=dict(list1)
# print(dict1)
# for items,candy in dict1.items():            #dict.items() for print dictionary for "for loop" statements
#     print(items,"has candy",candy)
# list1=[1,4,45,16,78,2,9,"harry","int","floar"]
# for items in list1:
#     if str(items).isnumeric() and items>6:
#         print(items)
#while loop example
i=0
while(i<45):
    i=i+5
    print(i)
    