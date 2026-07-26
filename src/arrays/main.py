def main():
    print("Arrays in Python (tuples and lists).")

    # tuples are useful if we know the values in a dvance
    primes = (2, 3, 5, 9, 11)
    print(primes)

    # tuples are immutable 
    # oh no, 9 is not prime
    # tuples are 0-indexed
    # primes[3] = 7     # this will not work
    
    # most of the time, we will use lists in python 
    empty_list = []     # or = list()

    # sometimes, I just want a bunch of values 
    n = 6
    a = [0] * 6     # [0, 0, 0, 0, 0, 0]

    # let's make a small list
    # it can even have different types 
    mixed_list = [1, 3.14, -42, "Python", True]

    # print(empty_list, a, mixed_list) # this outputs in terminal left to right
    
    # lists use 0-based indexing (indices range from 0 to n-1, where n ins length of the list)

    a[0] = -8   # initial element

    i = 3
    k = 4
    a[2 * i - 4] = (k // 2) ** 4 + 1    # a[2] = 17

    # len(a) gives number of elements in list a

    # negative indexing
    # how do I set the final element of a list? 
    # elements indices of a list range from 0 to len(a) - 1
    # a[len(a) - 1] = 43  # sets the last element
    a[-1] = 43  
    # a[-1]: element of list a
    # a[-2]: penultimate element
    # a[-3]: antepenultinmate element 
    # ... this goes back how far? 
    # a[-len(a)]: first element of a
    print("a is now", a)

    # indices outside the range from -len(a) to len(a) - 1 produce IndexErrors
    # a[len(a)] = 7
    # a[-len(a) - 1] = 2

def factorial_array(n:int) -> list[int]:
    """
    Produces a list of all factorials from 0! to n!

    Parameters:
    - n (int)

    Returns: 
    list[int]: A list of length n+1, where the k-th element is k! for k = 0, 1, ..., n
    """

if __name__ == "__main__": 
    main()