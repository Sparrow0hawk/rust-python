from numba import jit, types
import numba as nb
import numpy as np

def count_doubles(val):

    total = 0 
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total

def count_doubles_numpy(val):

    byte_array = np.frombuffer(val.encode(), np.byte)
    return np.sum(byte_array[:-1] == byte_array[1:])

@jit(nopython = True)
def count_doubles_numpy_jit(val):

    val_array = []

    for idx in range(len(val)):
        val_array.append(ord(val[idx]))

    byte_array = np.array(val_array, dtype=np.int8)
    return np.sum(byte_array[:-1] == byte_array[1:])

def count_doubles_numpy_loop(val):

    val_array = []

    for idx in range(len(val)):
        val_array.append(ord(val[idx]))

    byte_array = np.array(val_array, dtype=np.int8)
    return np.sum(byte_array[:-1] == byte_array[1:])