import double 
import random
import string 

val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_double_python(benchmark):
    benchmark(double.count_doubles, val)
