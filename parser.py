# Rename methods to our built in methods (Mix, Cook, Brun, Etc.)
from stack import Stack

stack = Stack()


def add_to_stack(value):
    stack.push(value)


def return_stack():
    return stack.stack


def add(): #add
    # Add two values from the stack
    assert not stack.isempty(), "Cannot mix the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    stack.push(val1 + val2)
    return


def subtract(): #subtract
    assert not stack.isempty(), "Cannot skim the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    stack.push(val2 - val1)
    return

def popAll(): #popall
    assert not stack.isempty(), "Cannot make popcorn... Stack is empty!"
    for i in stack:
        print(stack.pop())


def print(): #print
    assert not stack.isempty(), "Cannot serve the stack... Stack is empty!"
    print(stack.pop())

def peek(): #peek
    assert not stack.isempty(), "Cannot clarify the stack... Stack is empty!"
    print(stack.peek())

def length(): #length
    assert not stack.isempty(), "Cannot measure the stack... Stack is empty!"
    print(len(stack))

def multiply(): #multiplication
    assert not stack.isempty(), "Cannot cure the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    print(val1 * val2)

def divide(): #division
    assert not stack.isempty(), "Cannot dissolve the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    print(val1 / val2)

def floorDivide(): #floor division
    assert not stack.isempty(), "Cannot dust the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    print(val1 // val2)

def getRemainder(): #getRemainder
    assert not stack.isempty(), "Cannot grill the stack... Stack is empty!"
    val1 = stack.pop()
    val2 = stack.pop()
    print(val1 % val2)

# Rename to something more appropriate to check if a value is in the dictionary
def check_dictionary(argument):

    dictionary = {
        'mix': add,
        'skim': subtract,
        'serve': print,
        'popcorn': popAll,
        'clarify': peek,
        'measure': length,
        'dust' : divide,
        'grill' : floorDivide,
        'dissolve' : getRemainder(),
        'cure' : multiply(),

    }
    # Get the function from switcher dictionary
    # The Lambda will return the string "nothing" if the value is not in the dictionary
    func = dictionary.get(argument, lambda: "nothing")
    # Execute the function
    return func()


def parser(tokens):

    return




