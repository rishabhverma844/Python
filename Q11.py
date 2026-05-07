"""
Question 11 of 16 | Level — Hard | Concept — Truthy and Falsy values
In Python, every value has a boolean nature — even non-booleans. Predict the output:

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
print(bool(0.0))
print(bool("hello"))
print(bool(42))
print(bool([1,2,3]))

"""

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
print(bool(0.0))
print(bool("hello"))
print(bool(42))
print(bool([1,2,3]))



"""
Real automation use case:

pythontest_results = []
if not test_results:    # Instead of writing len(test_results) == 0
    print("No tests ran")
    
Empty list is falsy — so not test_results is True when the list is empty. 
Clean and Pythonic.

Interview line — "In Python, zero, empty strings, empty collections, and 
None are all falsy — everything else is truthy. This allows clean condition 
checks like - if not results instead of if len(results) == 0."
"""