import time

def main():
    print("Studying GCD algorithms.")
    print("The GCD of 42 and 63 is", trivial_gcd(63, 42))
    print("The GCD of 42 and 63 is", euclid_gcd(63, 42))

    # time the algorithms
    x = 3782026
    y = 2731479

    # time the trivial algorithm
    start = time.time() # starts a stopwatch
    d = trivial_gcd(x, y)
    elapsed = time.time() - start # stops the stopwatch

    # print the time in a pretty way 
    print(f"trivial_gcd took {elapsed:.6f} seconds.")

    # time the Euclidean algorithm
    start = time.time() # starts a stopwatch
    d = euclid_gcd(x, y)
    elapsed_2 = time.time() - start # stops the stopwatch

    # print the time in a pretty way 
    print(f"euclid_gcd took {elapsed_2:.6f} seconds.")

    # the speedup is the ratio of the two times
    print(f"euclid_gcd is {elapsed/elapsed_2:.2f} times faster than trivial_gcd.")

def euclid_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using Euclid's algorithm.

    Parameters:
    -a (int)
    -b (int)

    Returns:
    int: GCD of a and b
    """
    # solve the negative first before 0. In case it is (-1, 0) or (0, -1). 
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    # a = abs(a)
    # b = abs(b)

    if a == 0:
        return b # this works even if b == 0, since GCD(0, 0) = 0
    if b == 0:
        return a

    # facts about GCD: GCD(a, b) = GCD(a-b, b) when a > b
    # GCD(63, 42) = GCD(21, 42) = GCD(21, 21) = 21 
    # keep doing this, therefore use loop. Two cases depending on whether a > b or b > a

    while a != b:
        if a > b:
            a = a - b
        else: 
            # know that b > a 
            b = b - a
    # what do we know if we're here? a == b
    return a # or b


def trivial_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using a trivial 
    algorithm that tries every possible divisor of a and b.

    Parameters:
    -a (int)
    -b (int)

    Returns:
    int: GCD of a and b
    """
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    if a == 0:
        return b # this works even if b == 0, since GCD(0, 0) = 0
    if b == 0:
        return a

    d = 1

    m = min(a, b)

    # try every possible candidate divisor up to and 
    # including m, and update d everytime we find a divisor
    for p in range(2, m+1):
        # if p is a divisor of both, then d = p
        # if a % p == 0:  # divisor of a 
        #     if b % p == 0: # divisor of b 
   
        # this is nesting too much. Use "and". 
        if (a % p == 0) and (b % p == 0):
        # if (a % p == 0) or (b % p == 0):  # this returns m
            d = p 
            # with "and": if the first statement is False, then the whole thing is imediately False and the second condition isn't read

    return d 

# x        y       x and y     x or y
# True     True    True        True
# True     False   False       True
# False    True    False       True
# False    False   False       False 

# if first statement (x) if True, x or y short circuits to True

if __name__ == "__main__": 
    main()