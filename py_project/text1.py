from functools import reduce


a = [1,2,3,4,5]
b = []
for i in a:
    x = i * 2
    b.append(x)
print(b)

def square(x):
    return x*2

def multi(x):
    return x*x

# c = map(map(multi, a))
c = map(lambda x:x*2,a)
print(list(c))