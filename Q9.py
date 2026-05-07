"""
Question 9 of 16 | Level — Hard | Concept — Short circuit evaluation
In Python, AND and OR use short circuit evaluation — meaning Python stops
evaluating as soon as the result is determined.

and — if the first value is False, Python skips the second entirely
or — if the first value is True, Python skips the second entirely

Predict the output of each line:

print(False and 1/0)
print(True or 1/0)
print(True and 1/0)
print(False or 1/0)

"""

print(False and 1/0)
print(True or 1/0)
print(True and 1/0)
print(False or 1/0)




"""
The pattern to remember:
Operator. First value.  Second evaluated?
and      False.         No — result already False
and      True.          Yes — need to check second
or       True           No — result already True
or        False         Yes — need to check second

Real automation use case:
# Safe way to check — if driver is None, second part is skipped
if driver is not None and driver.find_element("id", "btn"):
    click()

Without short circuit, driver.find_element() would crash if driver is None. 
Short circuit saves you.

Interview line — "Python uses short circuit evaluation — and stops at the first False, 
or stops at the first True. This is used in automation to guard against null/None 
checks before calling methods on an object."
"""