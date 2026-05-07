"""
Question 16 of 16 | Level — Interview | Concept — Operator trap
Last question before exit test. Predict the output and explain:

print(0 == False)
print(0 is False)
print("" == False)
print([] == False)
print(bool([]) == False)

"""
print(0 == False)
print(0 is False)
print("" == False)
print([] == False)
print(bool([]) == False)


"""
print(bool("") == False)   # True  — bool of empty string is False
print("" == False)         # False — empty string is NOT False itself
print(bool([]) == False)   # True  — bool of empty list is False
print([] == False)         # False — empty list is NOT False itself


Interview line — "Falsy and False are not the same thing. '' and [] are falsy — 
they behave like False in conditions — but '' == False is False. 
Only 0 and 0.0 actually equal False due to the bool/int relationship."
"""