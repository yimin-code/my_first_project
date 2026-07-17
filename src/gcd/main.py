def main():
    print("Studying GCD algorithms.")
    
    x = 63
    y = 42 # GCD should be 21

    print("The GCD of 42 and 63 is", trivial_gcd(63, 42))

def euclid_gcd(a:int, b:int) -> int:
    """
    Returns the GCD of two integers using Euclid's algorithm.

    Parameters:
    -a (int)
    -b (int)

    Returns:
    int: GCD of a and b
    """
    if (a <= 0) or (b <= 0):
        raise ValueError("Error: negative input give to trivial_gcd()") # this should go at the beginning of the function to not damage anything

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
    if (a <= 0) or (b <= 0):
        raise ValueError("Error: negative input give to trivial_gcd()") # this should go at the beginning of the function to not damage anything

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