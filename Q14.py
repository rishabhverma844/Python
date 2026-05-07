"""
Question 14 of 16 | Level — Interview | Concept — Output prediction
What is the output? Predict and explain:
a = None
b = None
print(a is b)
print(a == b)
"""

a = None
b = None
print(a is b)
print(a == b)


"""
None is a singleton in Python. There is only ever one None object in memory — 
every variable assigned None points to that exact same object. So both is and == return True.
This is actually the one case where using is is correct and recommended — always check for None using is, never ==.

Interview line — "None is a singleton in Python — only one instance exists in memory. 
That's why is None always works reliably, and it's the Pythonic way to check for absence 
of value."
"""