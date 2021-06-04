import double 
import random
import string
import myrustlib 

val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_double_python(benchmark):
    benchmark(double.count_doubles, val)

def test_double_rust(benchmark):
    benchmark(myrustlib.count_doubles, val)
