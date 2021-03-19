
def float_check(x):
    if x.isdigit():
        return True
    else:
        try:
            float(x)
            return True
        except ValueError:
            return False
