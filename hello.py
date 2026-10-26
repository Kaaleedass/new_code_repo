print("hello world")

def multiply_by_five(number):
    try:
        return number * 5
    except TypeError:
        return "Input must be a number"
