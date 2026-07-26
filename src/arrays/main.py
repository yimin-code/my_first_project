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

    n = 10
    print("Factorials up to", n, "are", factorial_array(n))

    c = [3, 2, 1]
    print(min_integer_array(c))

    print("Minimum of 3, 4, and -7 is", min_integers(3, 4, -7))

    # integers, strings, floats are pass by value (brand-new copy is created when they go into a function)
    # this means that changes made inside the function do not affect the original variable outside 
    # lists are not pass by value, they are pass by reference
    # chnages made will modify the original data 

    c = [0] * 6
    change_first_element(c)

    print(c)

def factorial_array(n:int) -> list[int]:
    """
    Produces a list of all factorials from 0! to n!

    Parameters:
    - n (int)

    Returns: 
    list[int]: A list of length n+1, where the k-th element is k! 
    """

    if n < 0:
        raise ValueError("Error: negative input given.")

    fact = [0] * (n + 1) # set number of elements

    fact[0] = 1

    # range through and set k! = k * (k - 1)! 
    for k in range(1, n + 1): # if only n+1, will get fact[last element] in the next line 
        fact[k] = fact[k-1] * k

    return fact

def min_integer_array(a: list[int]) -> int:
    """
    Returns the minimum element from list a. 
    """
    if len(a) == 0:
        raise ValueError("Error: empty list given to function.")

    m = a[0] # stores our minimum. should not be 0 in case of all positive numbers

    # this is good:
    # for i in range(len(a)): 
    #     # is the current value better than what I currently have?
    #     if a[i] < m:
    #         # update m appropriately 
    #         m = a[i]

    for val in a: 
        if val < m: 
            m = val 

    return m 

# min() in Python can take an arbitrary number of inputs 
# min(2, 3), min(-1, 37, 58, 109092), etc. 
def min_integers(*numbers: int) -> int: # *numbers indicates that we can have an arbitrary number of inputs
    # numbers is a tuple
    if len(numbers) == 0:
        raise ValueError("No values given to function.")

    # redundant code! call the other function
    # m = numbers[0]

    # for val in numbers: 
    #     if val < m: 
    #         m = val 
    m = min_integer_array(list(numbers)) # list is a built-in function that converts tuples into lists
    
    return m 

def change_first_element(a: list[int]):
    if len(a) == 0:
        raise ValueError("No values given to function.")

    a[0] = 1

if __name__ == "__main__": 
    main()