import math
import time

def main():
    print("Prime finding in Python.")

    n = 11
    prime_booleans = trivial_prime_finder(n)
    print(prime_booleans)
    print(sieve_of_eratosthenes(n))

    n = 20000

    # trivial timer
    start = time.time()
    trivial_prime_finder(n)
    elapsed_trivial = time.time() - start
    print(f"Trivial prime finder took {elapsed_trivial:.6f} seconds.")

    # sieve timer
    start = time.time()
    sieve_of_eratosthenes(n)
    elapsed_sieve = time.time() - start
    print(f"Sieve of Eratosthenes took {elapsed_sieve:.6f} seconds.")

    # ratio 
    speedup = elapsed_trivial/elapsed_sieve
    print(f"Speedup: {speedup:.2f}x faster")

    prime_list = list_primes(23)
    print(prime_list)

    # how many prime numbers are there? 
    # proof that there infinite prime numbers:

    # how many prime numbers in <= n?
    # is there a formula in terms of n?

    # plot all primes up to n
    print(prime_count_array(23))

def prime_count_array(n: int) -> list[int]:
    """
    Produces a list storing the number of primes encountered up to a given interger.

    Prameters:
    -n (int)

    Output: 
    list[int]: list having length n+1 whose k-th element is equal to the number of primes less than or equal to k
    """
    if n < 0: 
        raise ValueError("Error: negative integer given as input.")

    # first, get all the prime values as True or False
    prime_booleans = sieve_of_eratosthenes(n)

    # next, let's make the list we care about
    result = [0] * (n+1)

    # we need to keep track of how many primes we have encountered up to a point in time
    prime_counter = 0

    # range over list of primes
    for i, is_prime in enumerate(prime_booleans):
        # is the current number primer?
        if is_prime:
            #found a prime! so update counter
            prime_counter += 1
        # set the current value of my list equal to number of primes encountered thus far
        result[i] = prime_counter

    return result

def list_primes(n: int) -> list[int]:
    """
    Returns a list of all primes up to and (possibly including) n.

    Parameters:
    -n: int

    Output:
    list[int]: list of all primes up to and including n.
    """
    if n < 0: 
        raise ValueError("Error: negative integer given as input.")

    # I don't know how big the list is going to be.

    prime_list = [] # or list()

    prime_booleans = sieve_of_eratosthenes(n)

    # range through this list and identify which ones are True

    for p, is_prime in enumerate(prime_booleans): 
    # p stores index  
    # is_prime is a variable that stores True or False
        if is_prime:
            # append the current integer to the list
            prime_list.append(p)

    return prime_list

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

def cross_off_multiples(prime_booleans: list[bool], p: int) -> list[bool]:
    """
    Crosses off the multiples of p as composite numbers (i.e., not prime).

    Parameters:
    - prime_booleans: list[bool]
    - p: int

    Output: 
    list[bool]: the element at index p will be True if p is prime and False if it is not
    (i.e., prime_booleans[p] = True if p is prime)
    """
    if p < 2:
        raise ValueError("Error: p must be at least 2.")

    if len(prime_booleans) < 2:
        raise ValueError("Error: prime_booleans must have length at least 2.")

    n = len(prime_booleans) - 1 # the largest number we are checking for primality

    for k in range(2*p, n+1, p): # start at 2*p and go up to n, with step size p
        if k % p == 0:
            prime_booleans[k] = False

    # range over all indices of prime_booleans that are multiples of p, starting at 2*p and ending at the last index of prime_booleans, with step size p

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