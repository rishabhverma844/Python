"""
Question 4 of 16 | Level — Easy | Concept — Assignment operators
Start with pass_count = 0. A test suite runs and you need to:

Add 5 passed tests using +=
Then add 3 more using +=
Then subtract 2 failed retries using -=
Then multiply the count by 2 (running a second cycle) using *=

Print the final count.

"""

pass_count = 0

pass_count += 5
pass_count += 3
pass_count -= 2
pass_count *= 2

print(pass_count)



"""
Interview line — "Assignment operators like +=, -=, *= update the variable in 
place — they're shorthand for x = x + n. In automation, they're commonly 
used for counters, retry logic, and accumulating test results."

"""