def main():
    print("Prime finding in Python.")

def trivial_prime_finder(n: int) -> list[bool]:
    """
    Finds all prime numbers up to and possibly including n.

    Parameters:
    - n: int

    Output: 
    list[bool]: the element at index p will be True if p is prime and False if it is not
    (i.e., prime_booleans[p] = True if p is prime)

    Raises a ValueError if input is negative
    """
    if n < 0: 
        raise ValueError("Error: negative integer given as input")

    prime_booleans = [False] * (n+1) # set default values

    for p in range(2, n+1): # we know 0 and 1 are not prime
        # is it the case that p is prime? 
        prime_booleans[p] = is_prime(p) 

    return prime_booleans

def is_prime(p: int) -> bool:
    """
    Returns True if input integer is prime and False otherwise. 

    Parameters:
    - p (int)

    Output: 
    """
    if p < 0: 
        raise ValueError("Error: negative integer given as input") 

    # easy cases: p = 0 or 1 (False)
    if p < 2:
        return False 

    # we need to check every possible candidate divisor of p
    for k in range(2, p+1):
        # is k a divisor of p?
        return k % p == 0
    

if __name__ == "__main__": 
    main()