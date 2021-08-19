def feast(beast,dish):
    # your code here
    a=beast[:1:].lower()
    a1=beast[-1::].lower()
    b=dish[:1:].lower()
    b1=dish[-1::].lower()
    if (a,a1) == (b,b1):
        return True
    else:
        return False
