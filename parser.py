from stack import Stack
from variablestorage import Variables
import re

stack = Stack()
variables = Variables()


# Debugging methods


def add_to_stack(value):
    stack.push(value)


def return_stack():
    return stack.stack


# End Debugging methods


def add():  # Mix
    # Add two values from the stack
    assert not stack.isempty(), "Cannot mix the stack... Stack is empty!"
    val1 = float(stack.pop())
    val2 = float(stack.pop())
    stack.push(val1 + val2)
    return


def subtract():  # Skim
    assert not stack.isempty(), "Cannot skim the stack... Stack is empty!"

    val1 = float(stack.pop())
    val2 = float(stack.pop())

    stack.push(val2 - val1)
    return


def popAll():  # Popcorn
    assert not stack.isempty(), "Cannot make popcorn... Stack is empty!"
    while stack.size() != 0:
        print stack.pop()


def print_stack():  # Serve
    assert not stack.isempty(), "Cannot serve the stack... Stack is empty!"
    print(stack.pop())


def peek():  # Clarify
    assert not stack.isempty(), "Cannot clarify the stack... Stack is empty!"
    print(stack.peek())


def length():  # Measure
    print(stack.size())


def delete():  # Grind
    stack.pop()
    return


def multiply():  # Cure
    assert not stack.isempty(), "Cannot cure the stack... Stack is empty!"
    val1 = float(stack.pop())
    val2 = float(stack.pop())
    stack.push(val1 * val2)


def divide():  # Dust
    assert not stack.isempty(), "Cannot dust the stack... Stack is empty!"
    val1 = float(stack.pop())
    val2 = float(stack.pop())
    stack.push(val1 / val2)


def floorDivide():  # Grill
    assert not stack.isempty(), "Cannot grill the stack... Stack is empty!"
    val1 = float(stack.pop())
    val2 = float(stack.pop())
    stack.push(val1 // val2)


def getRemainder():  # Dissolve
    assert not stack.isempty(), "Cannot dissolve the stack... Stack is empty!"
    val1 = float(stack.pop())
    val2 = float(stack.pop())
    stack.push(val2 % val1)


# Check if the token is in the dictionary.
def check_dictionary(argument):
    dictionary = {
        'mix': add,
        'skim': subtract,
        'serve': print_stack,
        'popcorn': popAll,
        'clarify': peek,
        'measure': length,
        'dust': divide,
        'grill': floorDivide,
        'dissolve': getRemainder,
        'cure': multiply,
        'pack': store_var,
        'shop': get_var,
        'trash': delete_var,
        'order': get_input,
        'grind': delete

    }
    # Get the function from dictionary
    # The Lambda will return -1 if the value is not in the dictionary
    func = dictionary.get(argument, lambda: -1)
    # Execute the function
    return func()


def store_var():  # Pack the variable
    value = stack.pop()
    name = stack.pop()

    variables.set_var(name, value)

    return


def get_var():  # Shop for the variable
    assert not variables.isempty()

    name = stack.pop()

    stack.push(variables.get_var(name))
    return


def delete_var():  # trash the variable
    assert not variables.isempty()

    name = stack.pop()
    print name
    return


def get_input():  # read input from console to stack
    user_input = raw_input('Input: ')

    stack.push(user_input.strip())
    return


def parser(tokens):  # parse each word if it is a number, string, or variable
    number = re.compile(r'[0-9]+(\.[0-9][0-9]?)?')
    string = re.compile(r'^[a-zA-Z]*$')
    variable = re.compile(r'^\$[A-Za-z0-9._]+$')

    for token in tokens:

        if number.match(token):
            stack.push(token)
        elif variable.match(token):
            stack.push(token)
        elif string.match(token):
            value = check_dictionary(token)
            if value:
                raise RuntimeError("Invalid Token " + token)
    return
