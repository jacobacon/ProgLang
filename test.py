def zero():
    return 1+1

def one():
    return "one"

def numbers_to_functions_to_strings(argument):
    switcher = {
        'ADD': zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()


print numbers_to_functions_to_strings(5)
