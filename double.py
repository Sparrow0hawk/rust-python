from numba import jit

def count_doubles(val):

    total = 0 
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total

@jit(nopython=True)
def count_doubles_jit(val):

    total = 0 
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total