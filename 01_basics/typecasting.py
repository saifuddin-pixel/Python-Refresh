a = 34
b = "34"

print(a)
print(type(a))
print(b)
print(type(b))

print("-"*10)
# print(b+a)
print("cannot add a+b because different data types")
print("-"*10)

#converting b from string -> integer
b = int(b)
print("b after convertion")
print(type(b))
print("-"*10)
print(a+b)
print("-"*10)

# converting float -> integer
pi = 3.14
print(pi)
print(type(pi))

pi_int = int(pi)
print(pi_int)
print(type(pi_int))