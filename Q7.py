"""
Question 7 of 16 | Level — Medium | Concept — String to bool casting
A config file returns is_headless = "True" as a string.

A junior dev writes bool("True") expecting True and bool("False") expecting False
Print both results
Explain why the output might surprise you and what the correct approach is



"""

is_headless = "True"

print(bool("False"))   # True  — non-empty string
print(bool("True"))    # True  — non-empty string
print(bool(""))        # False — empty string
print(bool("0"))       # True  — still non-empty!

result = is_headless == "True"
print(result)
print(type(result))

is_headless = "False"
result = is_headless == "True"
print(result)
print(type(result))



"""
You're simply comparing the string to "True" — if it matches, you get True, otherwise False.
Interview line — "bool() on a string checks emptiness, not content. To convert config string 
flags like 'True'/'False' to actual booleans, use a string comparison — value == 'True' — not bool(value)."

"""