"""
Question 11 of 16 | Level — Hard | Concept — Type conversion edge cases
Predict the output of each line and explain why:
print(int(True))
print(int(False))
print(float("inf"))
print(int("0"))
print(bool(0.0))

"""

print(int(True))
print(int(False))
print(float("inf"))
print(int("0"))
print(bool(0.0))

"""

Clue 1 — you already learned that True = 1 and False = 0
So what should int(True) give you?
Clue 2 — int() converts to a whole number
So what should int(False) give you?
Clue 3 — float("inf") — inf means infinity in mathematics
What do you think Python returns for this?
Clue 4 — int("0") — you already did this in Q5, same concept
What does int() on a numeric string return?
Clue 5 — you already learned bool() on numbers checks if it's zero or non-zero
So what does bool(0.0) return?


---------
Line 3 explained — float("inf")
Python supports infinity as a valid float value. "inf" is a special string Python recognizes and converts to mathematical infinity.

print(float("inf"))    # inf
print(float("-inf"))   # -inf — negative infinity also works
print(type(float("inf")))  # <class 'float'>

It's used in real automation when you want to set no upper limit — for example a retry count or timeout that should never stop.

Interview line — "Python's float('inf') represents mathematical infinity — it's a valid float value, not an error. 
It's useful in scenarios where you need an unbounded upper limit, like max retries or timeouts."

"""