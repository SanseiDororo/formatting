def test_func():
    return "get back"


# Example Python file with common mistakes


def example_function(
    arg1,
    arg2,
):
    print("Hello, world!")  # Using double quotes instead of single quotes
    print("Another line of code")  # Single quotes

    if arg1 == 1:
        print("Argument 1 is one")
    elif arg1 == 2:
        print("Argument 1 is two")

    # Excessive whitespace
    result = arg1 + arg2

    # Trailing comma in a list
    my_list = [
        1,
        2,
        3,  # Trailing comma
    ]

    # Missing docstring
    def another_function():
        return my_list

    # Incorrect indentation
    if True:
        print("This line is incorrectly indented")

    return result


# Function call with extra space
example_function(1, 2)
