# Rename methods to our built in methods (Mix, Cook, Brun, Etc.)


def zero():
    # Add python handling code for our methods.
    return "zero"


def one():
    return "one"


# Rename to something more appropriate to check if a value is in the dictionary
def numbers_to_functions_to_strings(argument):

    dictionary = {
        0: zero,
        1: one,
    }
    # Get the function from switcher dictionary
    # The Lambda will return the string "nothing" if the value is not in the dictionary
    func = dictionary.get(argument, lambda: "nothing")
    # Execute the function
    return func()





