"""
Question 16 of 16 | Level — Interview | Concept — Output prediction

Predict the output and explain:
x = 10
y = int(10)
z = int("10")

print(x == y)
print(y == z)
print(x is y)
print(type(x) == type(z))
"""

x = 10
y = int(10)
z = int("10")

print(x == y)
print(y == z)
print(x is y)
print(type(x) == type(z))


"""
Interview line — "Python interns small integers between -5 and 256, so variables holding 
the same small integer value will share the same memory object — making both == and is 
return True for them."
"""