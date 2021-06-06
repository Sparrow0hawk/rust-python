import double 
import random
import string
import myrustlib 
import cdouble

val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_double_python(benchmark):
    benchmark(double.count_doubles, val)

def test_double_rust(benchmark):
    benchmark(myrustlib.count_doubles, val)

def test_cdouble(benchmark):
    benchmark(cdouble.count_doubles, val)

def test_double_np(benchmark):
    benchmark(double.count_doubles_numpy, val)

def test_double_np_jit(benchmark):
    benchmark(double.count_doubles_numpy_jit, val)

def test_count_doubles_numpy_loop(benchmark):
    benchmark(double.count_doubles_numpy_loop, val)