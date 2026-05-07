"""
Question 7 of 16 | Level — Medium | Concept — Logical operators with not
You have these test flags:

is_logged_in = False
is_admin = True
has_permission = False
Print the result of these expressions and predict each output:

not is_logged_in
not is_admin
is_admin and not has_permission
not is_logged_in and not has_permission

"""

is_logged_in = False
is_admin = True
has_permission = False


print(not is_logged_in)
print(not is_admin)
print(is_admin and not has_permission)
print(not is_logged_in and not has_permission)


"""
Interview line — "not simply flips a boolean — not False gives True and vice versa. 
Combining not with and/or is common in test conditions where you need to check 
absence of a state, like 'user is not logged in and does not have permission'."
"""