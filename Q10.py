"""
Question 10 of 16 | Level — Hard | Concept — Mutable default and variable identity
Run this in your head first:
a = "test"
b = "test"
c = 1000
d = 1000

print(a is b)
print(c is d)
Predict both outputs and explain why they differ.

"""

a = "test"
b = "test"
c = 1000
d = 1000

print(a is b)
print(c is d)


"""
Concept - String Interning

a = "test"
b = "test"
print(a is b)    # True
Python interns short strings — meaning it reuses the same memory object for identical small strings. 
So a and b point to the exact same object in memory.

c = 1000
d = 1000
print(c is d)    # False
Python only interns small integers (-5 to 256). Since 1000 is outside that range, 
Python creates two separate objects in memory — so c and d point to different objects even though their values are equal.

Interview line — "is checks object identity, not equality. Python interns small integers up to 256 and short strings, 
so is returns True for those. For larger integers or new objects, always use == for value comparison — never is."
"""