"""
Question 6 of 16 | Level — Medium | Concept — Type casting pitfall
Same scenario. This time the value coming from the config is timeout = "45.6" — a decimal value inside a string.

Try converting it directly to int
Then show the correct way to handle it and still get an int at the end
Print the final result and its type



"""

timeout = "45.6"
timeout_str_to_float = float(timeout)
timeout_float_to_int = int(timeout_str_to_float)

print(timeout_float_to_int, type(timeout_float_to_int))




"""
Approach — int("45.6") directly throws a ValueError because Python won't cast a decimal string straight to int. 
The correct path is str → float → int. In an interview, say: 
"You can't cast a float-formatted string directly to int — Python raises a ValueError. 
The safe approach is to cast to float first, then to int, which truncates the decimal."

Output your code produces:
45 <class 'int'>

Note — it truncates, not rounds. 45.9 would also give 45, not 46. Keep that in mind.

"""