#1 solution
def to_alternating_case(string):
    result = []
    for c in string:
        if c.islower():
            result.append(c.upper())
        else:
            result.append(c.lower())
    return ''.join(result)
#2 solution
def to_alternating_case(string):
    return string.swapcase()
