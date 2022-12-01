f = lambda x : x * 5 # a lambda function
print(f(3), f(2142), f(-231))

# actual usage of lambda function
x = [23,45,67,22,87,41,82]

x2 = list(map(lambda i: i**2, x)) # map function
print(x2)

a = [2,3,1,5,5,1,2]
b = [2,3,1,2,4,4,2]

ab = list(map(lambda i,j: i * j, a, b)) # map function with multiple lists
print(ab)

# filter
evens = list(filter(lambda i: i % 2 == 0, x))
print(evens)