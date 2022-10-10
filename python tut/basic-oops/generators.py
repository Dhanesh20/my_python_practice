"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
Generators concept is also very similar as it is used to make an iterator. 
The only difference comes in the return statement. The generator does not use a return statement. 
Instead, it uses a yield keyword. Yield functionality is very similar to return as it returns a value to the caller, 
but the difference is that it also saves the state of the iterator. Meaning that when we use the function again, 
the yield will resume the value from the place it left off.
Advantages of using Generators:
Producing iterables is extremely difficult and lengthy without Generators in Python.
Generators automatically implement __iter__(), __next__(), and StopIteration which otherwise, need to be explicitly specified.
The most significant advantage of generators is that the memory is saved as the items are produced when required.
Generators are also used to pipeline a series of operations, for example, Generate Fibonacci Series.
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
