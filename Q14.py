"""
Question 14 of 16 | Level — Interview | Concept — and/or return values

This is a trap most developers fall into. and and or don't always
return True or False — they return the actual value that determined the result.

print(0 or "default")
print("" or "fallback")
print("active" or "default")
print(None and "value")
print(5 and "ready")

"""


print(0 or "default")
print("" or "fallback")
print("active" or "default")
print(None and "value")
print(5 and "ready")


"""
OR rule — returns the first truthy value it finds:

0 or "default"    # 0 is falsy → check next → "default" is truthy → return "default"
"" or "fallback"  # "" is falsy → check next → "fallback" is truthy → return "fallback"
"active" or "default"  # "active" is truthy → stop here → return "active"

--

AND rule — returns the first falsy value it finds:

None and "value"  # None is falsy → stop here → return None
5 and "ready"     # 5 is truthy → check next → "ready" is truthy → return "ready"

With and — if all values are truthy, it returns the last value.

--

Simple way to remember:

or → returns first truthy value, or last value if all falsy
and → returns first falsy value, or last value if all truthy
"""