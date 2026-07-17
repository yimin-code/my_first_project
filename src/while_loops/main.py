def main():
    print("While loops in Python.") 

    n = 5
    m = factorial(n)
    print(m)

    print("0! is", factorial(0))
    # n! = n*(n-1)!
    # 1! = 1*0!
    # 1 = 0! 
    # :D
    # However, (-100)! should be undefined, like any (negative number)!
    # print("-100! is", factorial(-100))

    print(sum_first_n_integers(100))
    print(gauss_sum(100))

# Ancient Greek Wisdom here:
# def euclid_gcd(a: int, b: int) -> int:
    # input: two integers
    # ... 

def gauss_sum(n: int) -> int:
    """
    Sums the first n positive integers.

    Parameters:
    -n (int)

    Returns:
    int: Sum of the first n positive integers.
    
    Raises an error if n < 0.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to sum_first_n_integers().")
    
    return (n+1)*(n/2)
    

def sum_first_n_integers(n: int) -> int:
    """
    Sums the first n positive integers.

    Parameters:
    -n (int)

    Returns:
    int: Sum of the first n positive integers.
    
    Raises an error if n < 0.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to sum_first_n_integers().")
    
    s = 0

    i = 1

    while i <= n:
        s += i  # this is shorhand for s = s + i
        i += 1  # shorthand for i = i + 1

    # also: s *= i, s /= i, s -= i 

    # at this point, we know that i > n 
    return s


def factorial(n: int) -> int:
    """
    Produces n! = n * (n-1) * ... (2) * 1

    Prameters:
    -n (int)

    Returns:
    int: n!

    Raises an error if n < 0.
    """
    if n < 0:
        # handle negative input with an error
        raise ValueError("Error: negative input given to factorial().")

    p = 1 # think of p as the container that will 
    # represent my growing product

    i = 1 # this is a counter variable to keep track of
    # how many multiplications we've done 

    while i <= n:   # can think as (if + repeating behavior)
        p = p * i   # left side: variable, right side: value 
        i = i + 1   # update the counter 

    # if i = i + 1 is commented out, will enter infinite loop
    # ctrl + C to stop running

    return p

if __name__ == "__main__": 
    main()