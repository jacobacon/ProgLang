# Rename methods to our built in methods (Mix, Cook, Brun, Etc.)
from stack import Stack

stack = Stack()


def add_to_stack(value):
    stack.push(value)


def return_stack():
    return stack.stack


def mix():
    # Add two values from the stack
    assert not stack.isempty()
    val1 = stack.pop()
    val2 = stack.pop()
    stack.push(val1 + val2)
    return


def subtract():
    assert not stack.isempty()
    val1 = stack.pop()
    val2 = stack.pop()
    stack.push(val2 - val1)
    return


def serve():
    assert not stack.isempty()
    print stack.pop()


# Rename to something more appropriate to check if a value is in the dictionary
def check_dictionary(argument):

    dictionary = {
        'mix': mix,
        'subtract': subtract,
        'serve': serve,
    }
    # Get the function from switcher dictionary
    # The Lambda will return the string "nothing" if the value is not in the dictionary
    func = dictionary.get(argument, lambda: "nothing")
    # Execute the function
    return func()


def parser(tokens):

    return




