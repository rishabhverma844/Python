"""
Question 3 of 16 | Level — Easy | Concept — Logical operators
You're writing a test condition. A test should only run if:

Browser is "chrome" AND timeout is greater than 20
OR if headless mode is False

browser = "chrome"
timeout = 30
headless = False
Print whether the test should run using one combined logical expression.

"""

browser = "chrome"
timeout = 30
headless = False

test_run = (browser == "chrome" and timeout > 20) or (headless is False)
print(test_run)


"""
Interview line — "and has higher precedence than or in Python, 
but always use parentheses when combining both — it removes ambiguity and 
makes the logic readable for anyone maintaining the code."
"""