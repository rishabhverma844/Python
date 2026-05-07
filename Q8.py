"""
Question 8 of 16 | Level — Medium | Concept — Dynamic typing
In Python, a variable can change its type during execution.

Start with data = 100
Reassign it to "hundred"
Reassign it again to 99.9
Print the type after each assignment

Then answer this — is this a good practice in real automation code and why?

"""

data = 100
print(type(data))

data = "hundred"
print(type(data))

data = 99.9
print(type(data))






"""
Answer to the second part — is this good practice?
No. In real automation code this is bad practice because:

It makes the code unpredictable and hard to debug
A reader can't trust what type data holds at any point
It can cause runtime errors if you perform operations expecting a specific type

In production automation frameworks, variables should hold the same type throughout — use different variable names if you need different types.
Interview line — "Python is dynamically typed, meaning a variable's type can change at runtime through reassignment. 
But in real-world automation code, this is avoided because it reduces readability and increases the chance of type-related bugs."
"""