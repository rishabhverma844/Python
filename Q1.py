"""
Question 1 of 16 | Level — Easy | Concept — Arithmetic operators
A test suite has total_tests = 100. Out of these, passed = 87.

Calculate how many tests failed
Calculate the pass percentage (use regular division)
Calculate how many complete sets of 10 tests fit in the total (floor division)
Calculate how many tests are left over after making those sets (modulus)

Print all four results.

"""

total_tests = 100
passed = 87

failed = total_tests - passed
print(failed)

pass_percentage = passed * 100 / total_tests
print(pass_percentage)

complete_sets = passed // 10
print(complete_sets)

left_over = total_tests % 10
print(left_over)


"""
Interview line — "Floor division // gives how many times a number fits completely, 
and modulus % gives what's left over — together they're useful for pagination,
batching, and grouping test cases."
"""