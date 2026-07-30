import math

def main():
    print("Prime finding in Python.")

    n = 11
    prime_booleans = trivial_prime_finder(n)
    print(prime_booleans)

def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Finds all prime numbers up to and possibly including n, using the Sieve of Eratosthenes algorithm from anceint Greece.

    Parameters:
    - n: int

    Output: 
    list[bool]: the element at index p will be True if p is prime and False if it is not
    (i.e., prime_booleans[p] = True if p is prime)

    Raises a ValueError if input is negative
    """
    if n < 0: 
        raise ValueError("Error: negative integer given as input")

    prime_booleans = [True] * (n+1) # set default values

    # 0 and 1 are not prime, so we can skip them
    prime_booleans[0] = False
    prime_booleans[1] = False

    for p in range(2, int(math.sqrt(n)) + 1): 
        # cross off the multiples of p as composite numbers (i.e., not prime)
        if prime_booleans[p]:
            prime_booleans = cross_off_multiples(prime_booleans, p)

    return prime_booleans



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
    bool: True if p is prime, False otherwise
    """
    if p < 0: 
        raise ValueError("Error: negative integer given as input") 

    # easy cases: p = 0 or 1 (False)
    if p < 2:
        return False 

    # we need to check every possible candidate divisor of p
    for k in range(2, int(math.sqrt(p)) + 1): 
        # is k a divisor of p?
        if p % k == 0:
            return False

    # if we survive all the divisor checks, we know that p is prime
    return True

# if p = k * b with k <= b, then k <= sqrt(p) and b >= sqrt(p)
# proof by contradiction: if k > sqrt(p) and b > sqrt(p), then k * b > p, which is a contradiction.
    

if __name__ == "__main__": 
    main()