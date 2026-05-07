"""
Question 9 of 16 | Level — Hard | Concept — int and bool relationship
In Python, bool is a subclass of int.

Print True + True
Print True + 5
Print False * 100
Print isinstance(True, int)

Predict the outputs first, then verify with code.

"""

print(True + True)
print(True + 5)
print(False * 100)
print(isinstance(True, int))





"""
The key fact — bool is a subclass of int in Python.
This means Python treats True and False as numbers internally:

True = 1
False = 0

That's it. Once you know this, every output becomes obvious.

print(True + True)       # 1 + 1 = 2
print(True + 5)          # 1 + 5 = 6
print(False * 100)       # 0 * 100 = 0
print(isinstance(True, int))  # True — bool IS a subclass of int

Output:
2
6
0
True

Why does this exist?
Historically Python built bool on top of int — so boolean values can participate in arithmetic without any casting. 
This is useful in real code:

tests = [True, False, True, True, False]
passed = sum(tests)   # counts True as 1
print(passed)         # 3 — number of passed tests

This pattern actually comes up in real automation — counting how many assertions passed in a test suite.

Interview line — "bool is a subclass of int in Python — True equals 1 and False equals 0. 
This means booleans can be used directly in arithmetic, which is useful for counting pass/fail results in test suites."

"""