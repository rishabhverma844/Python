"""
Question 10 of 16 | Level — Hard | Concept — Comparison chaining
Python allows chaining comparisons in a way most languages don't. Predict the output:

x = 5

print(1 < x < 10)
print(1 < x > 3)
print(10 > x > 1)
print(x == 5 == 5.0)
print(1 < x < 4)

"""

x = 5

print(1 < x < 10)
print(1 < x > 3)
print(10 > x > 1)
print(x == 5 == 5.0)
print(1 < x < 4)


"""
Interview line — "Python supports chained comparisons like 1 < x < 10 — 
it's evaluated as 1 < x and x < 10. 
This is more readable than writing two separate conditions and is 
unique to Python among major languages."
"""