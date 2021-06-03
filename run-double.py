import double
import random 
import string 

def main():

    val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

    return double.count_doubles(val)


if __name__ == "__main__":
    main()