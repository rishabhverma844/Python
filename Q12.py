"""
Question 12 of 16 | Level — Hard | Concept — Variable swapping
In most languages you need a temp variable to swap two values. Python has a cleaner way.
Swap a and b without using a third variable:

a = "login_test"
b = "logout_test"

After swapping, a should be "logout_test" and b should be "login_test". Print both after swapping.

"""

a = "login_test"
b = "logout_test"

a , b = b , a
print(a)
print(b)




"""
Approach — Python evaluates the entire right side first before assigning, 
so b, a is captured as a tuple and then unpacked into a, b simultaneously. 
No temp variable needed. 

In an interview, say: "Python uses tuple unpacking to swap variables in a single line — 
the right side is fully evaluated before any assignment happens, making a temporary 
variable unnecessary."

"""