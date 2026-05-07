"""
Question 2 of 16 | Level — Easy | Concept — type() vs isinstance()
Same config variables from Q1. Now instead of printing the type,
check whether each variable is of the expected type using isinstance() and print True or False for each.
"""

browser_name = "chrome"
timeout_value = 30
headless_mode = True
failure_rate = 0.5

print(isinstance(browser_name, str))
print(isinstance(timeout_value, int))
print(isinstance(headless_mode,bool))
print(isinstance(failure_rate,float))



"""
Approach — isinstance(variable, type) returns a boolean directly, making it cleaner than type(x) == str for checks. 
In an interview, say: "I prefer isinstance() over type() for validation because it also handles inheritance 
— it's the more Pythonic way to type-check."

Output your code produces:
True
True
True
True
"""