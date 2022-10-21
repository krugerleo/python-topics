def myexpo(num1: int, num2: int) -> int:
    '''
    This function takes one number to the power of another number and returns the result
    :param num1: This is the base
    :param num2: This is the exponent
    :return: The result of the calculation 
    '''
    return num1**num2

print(myexpo(8,2), help(myexpo), myexpo.__doc__)