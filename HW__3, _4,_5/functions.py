def func(var_a, var_b):
    if type(var_a) == str or type(var_b) == str:
        return 'str'
    elif var_a > var_b:
        return '>'
    elif var_a == var_b:
        return '='
    else:
        return '<'


print(func(9,9))
