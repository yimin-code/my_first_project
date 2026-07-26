import time

# GCD(50, 375)  = GCD(50, 325) 
#               = GCD(50, 25) 
#               = GCD(25, 25) 
#               = 25 
# many substractions is division.
#               = GCD(50, 375%50)
#               
# GCD(50, 25)    = GCD(50 % 25, 25) 
#               = GCD(0, 25) 
#               = 25

def main():
    print("Studying GCD algorithms.")
    print("The GCD of 42 and 63 is", trivial_gcd(63, 42))
    print("The GCD of 42 and 63 is", euclid_gcd(63, 42))
    print("The GCD of 42 and 63 is", faster_euclid_gcd(63, 42))

    # time the algorithms - use large numbers to see the difference in speed up margins - the larger the data, the more the difference in speedup.
    x = 378202999
    y = 27319

    # time the trivial algorithm
    start = time.time() # starts a stopwatch
    d = trivial_gcd(x, y)
    elapsed_trivial = time.time() - start # stops the stopwatch

    # print the time in a pretty way 
    print(f"trivial_gcd took {elapsed_trivial:.6f} seconds.")

    # time the Euclidean algorithm
    start = time.time() # starts a stopwatch
    d = euclid_gcd(x, y)
    elapsed_euclid = time.time() - start # stops the stopwatch

    # print the time in a pretty way 
    print(f"euclid_gcd took {elapsed_euclid:.6f} seconds.")

    # time the faster Euclidean algorithm
    start = time.time() # starts a stopwatch
    d = faster_euclid_gcd(x, y)
    elapsed_faster_euclid = time.time() - start # stops the stopwatch

    # print the time in a pretty way
    print(f"faster_euclid_gcd took {elapsed_faster_euclid:.6f} seconds.")

    #####################################################################

    # the speedup is the ratio of the two times
    speedup = elapsed_trivial / elapsed_euclid
    print(f"Speedup of Euclid vs. Trivial: {speedup:.2f} times faster.")
    speedup = elapsed_euclid / elapsed_faster_euclid
    print(f"Speedup of Faster Euclid vs. Normal Euclid: {speedup:.2f} times faster.")
    

def faster_euclid_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using Euclid's algorithm.

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

    # we are going to keep going for how long? 
    while (a != 0) and (b != 0):
        if a > b:
            a = a % b
        else: 
            # know that b > a 
            b = b % a

    # if we make it here, either a or b is 0. The other one is the GCD.
    return a + b 


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