"""
Question 13 of 16 | Level — Interview | Concept — Output prediction
What is the output of this code? Predict and explain:

x = 5
y = x
x = 10
print(y)
"""

x = 5
y = x
x = 10
print(y)


"""
Integers in Python are immutable. When you wrote y = x, Python didn't link y to x permanently — 
it just copied the reference to the value 5. When x was reassigned to 10, y stayed pointing at 5 untouched.

Interview line — "In Python, assigning one variable to another copies the reference, 
not a live link. For immutable types like int, reassigning the original has no effect 
on the copy."
"""