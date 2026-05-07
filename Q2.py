"""
Question 2 of 16 | Level — Easy | Concept — Comparison operators
You have these two test execution times:

test_a_time = 4.5
test_b_time = 6.0
threshold = 5.0

Write comparisons to answer all of these and print each result:

Is test_a_time faster than test_b_time?
Is test_b_time exceeding the threshold?
Are both times equal?
Is test_a_time within the threshold (less than or equal)?



"""

test_a_time = 4.5
test_b_time = 6.0
threshold = 5.0


print(test_a_time > test_b_time)
print(test_b_time > threshold)
print(test_a_time == test_b_time)
print(test_a_time <= threshold)



"""
Interview line — "Comparison operators always return a boolean — they're the 
foundation of every assertion in an automation framework. <= and >= are inclusive, 
meaning they return True when values are equal too."
"""