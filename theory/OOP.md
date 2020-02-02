# Object Orientated Programming

OOP is a way in which code is written. When writing code in OOP we structure the code into objects.
Each object should have one "job". 
i.e:
```
def add(number_one, number_two):
    return number_one + number_two
```
The above function does one thing, adds two numbers. As our functions get more complex and more needs to be done in each function, it is important to remember what the core "job" of the function is. 
```
# Not OOP:
def play(move):
    # Checks the input is a number
    if type(move) == int:
        moves[move - 1] = "X"
        return True
    else:
        print("move not valid")
        return False
```
The above code does everything in one function. While this will work without an issue, it means that our code is not structured in an OOP manner. Below the same code is re-written to comply with the OOP style of coding. OOP also makes code easier to read, so long as we have a good variable and function naming standard. 
```
# OOP
def validate_move(move):
    if type(move) == int:
        return True
    else:
        return False

def play(move):
    if validate_move(move):
        moves[move - 1] = "X"
    else:
        print("move not valid")
```
During the lesson today, we will be writing our program in a OOP style. This means we need to make sure that each function only does one core "job". Later in the lesson we will look at making our code as re-usable as possible. 

Making code in such a way that it can be re-used as often as possible is important, as it means we can get more done with less code. 