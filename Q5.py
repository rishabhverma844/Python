"""
Question 5 of 16 | Level — Medium | Concept — Type casting
A test script reads timeout value from a config file. Config files return everything as a string,
so you receive timeout = "45".

Convert it to an int
Multiply it by 2
Print the result and its type
"""

timeout = "45"
convert_int = int(timeout)*2
print(convert_int , type(convert_int))



"""
Approach — int() casts a string to integer when the string contains a valid whole number. 
In an interview, say: "In automation, config files and API responses often return numeric values as 
strings — type casting is essential before performing any arithmetic on them."

Output your code produces:
90 <class 'int'>
"""