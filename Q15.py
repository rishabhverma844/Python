"""
Question 15 of 16 | Level — Interview | Concept — Output prediction
What is the output? Predict and explain every line:

print(type(1))
print(type(1.0))
print(type("1"))
print(type(True))
print(1 == 1.0)
print(1 == True)
print(1.0 == True)
"""

print(type(1))
print(type(1.0))
print(type("1"))
print(type(True))
print(1 == 1.0)
print(1 == True)
print(1.0 == True)


"""
Interview line — "Python's == does value comparison across compatible numeric types 
— int, float, and bool can all compare equal if their numeric values match. 
But their types remain distinct, which type() or isinstance() will confirm."
"""