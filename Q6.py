"""
Question 6 of 16 | Level — Medium | Concept — Membership operators

supported = ["chrome", "firefox", "safari"]
tags = ["smoke", "regression", "sanity"]
Check and print:

Is "edge" in the supported list?
Is "chrome" in the supported list?
Is "performance" not in tags?
Is "smoke" not in tags?

"""

supported = ["chrome", "firefox", "safari"]
tags = ["smoke", "regression", "sanity"]

print("edge" in supported)
print("chrome" in supported)
print("performance" not in tags)
print("smoke" not in tags)



"""
Interview line — "in and not in are membership operators that work on any 
sequence — lists, strings, tuples, dictionaries. 

In automation they're perfect for validating whether a browser, tag, 
or config value exists in an allowed set."
"""