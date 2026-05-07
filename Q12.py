"""
Question 12 of 16 | Level — Hard | Concept — Bitwise operators
Bitwise operators work on binary representation of numbers. You only need to know enough to answer interview questions.

Operator.     Meaning.                       Example
&             AND — both bits must be 1      5 & 3 = 1
|             OR — at least one bit is 1     5 | 3 = 7
^             XOR — bits must be different   5 ^ 3 = 6
<<            Left shift — multiply by 2     5 << 1 = 10
>>            Right shift — divide by 2      5 >> 1 = 2

Predict the output:
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 << 1)
print(5 >> 1)

"""

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 << 1)
print(5 >> 1)



"""
The only thing to memorize for interviews:

<< = multiply by 2
>> = divide by 2
&, |, ^ = compare bit by bit

Interview line — "Bitwise operators work on binary representations — 
& needs both bits to be 1, | needs at least one, ^ needs them to differ. 
Left shift doubles the value, right shift halves it."
"""