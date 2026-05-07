"""
Question 1 of 16 | Level — Easy | Concept — Variable assignment and type()
I have a test config where I need to store the following values. Assign them to variables and then print the type of each:

browser name: "chrome"
timeout value: 30
headless mode: True
failure rate: 0.5

"""

browser_name = "chrome"
timeout_value = 30
headless_mode = True
failure_rate = 0.5

print(type(browser_name))
print(type(timeout_value))
print(type(headless_mode))
print(type(failure_rate))

"""
Approach — assign each value directly using =, let Python infer the type automatically, then use type() to verify. 
In an interview, say: "Python is dynamically typed — you don't declare types, the interpreter infers them at runtime."

Output your code produces:
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'float'>
"""