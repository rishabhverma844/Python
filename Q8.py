"""
Question 8 of 16 | Level — Medium | Concept — Walrus operator
Earlier in Q4 of Topic 1 you saw := and I told you it's the walrus operator — used for a different purpose. Now let's cover it.
The walrus operator := assigns a value to a variable and returns that value — all in one expression. It's useful when you want to assign and check in the same line.

# Without walrus
response = get_response()
if response:
    print(response)

# With walrus
if response := get_response():
    print(response)

Now your question — you're reading test results one by one. Use the walrus operator to assign and check in a single line:

test_results = [True, True, False, True]
total = len(test_results)

Use walrus operator to assign passed = sum(test_results) inside a print statement condition
Print "Majority passed: X" where X is the count

"""

test_results = [True, True, False, True]
total = len(test_results)

print(passed := sum(test_results))
print("Majority passed:", passed)


"""
The only thing to remember today:

:= is the walrus operator — assigns and checks in one expression
It works best inside if conditions and loops
"""