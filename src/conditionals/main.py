def main():
    print("Conditionals in Python.")

    print("The minimum of 3 and 4 is", min_2(3, 4))
    
    print(which_is_greater(3, 5))
    print(which_is_greater(42, 42))
    print(which_is_greater(-2, -7))

    print("same sign checks.")
    print(same_sign(3, 5))
    print(same_sign(-2, 0))
    print(same_sign(-23, 17))

# check multiple at the same time
    # does 0 have the same sign as 14 or -47? Question
    # for mathematician :D
    # let's treat it as 0 has the same sign as both positive
    # and negative numbers 
def same_sign(x: int, y: int) -> bool:
    """
    Returns True if two input integers have the same sign
    and False otherwise

    Parameters:
    -x (int)
    -y (int)

    Returns: 
    bool: True if x and y have the same sign and False 
    otherwise (zero has the same sign as all integers) 
    """
    # three cases:
    # 1. both positive (x * y >= 0, True)
    # 2. both negative (x * y >= 0, True)
    # 3. opposite signs (x * y < 0, False)
    
    # level 1
    # if (x >= 0 and y >= 0):
    #     return True
    # elif (x <= 0 and y <= 0):
    #     return True
    # else: 
    #     return False 

    # level 2
    # if x * y >= 0:
    #     return True
    # else: 
    #     return False 

    # level 3 (remove else)
    # if x * y >= 0:
    #     return True # function has returned
    # # if made it here, the function has not returned    
    # return False 

    # level 4 (best)
    return x * y >= 0 

def min_2(a:int, b:int) -> int:
    """
    Takes two integers and returns their minimum.

    Parameters:
    -a (int)
    -b (int)

    Returns:
    int: minimum of a and b
    """
    if a < b:
        return a
    else: 
        return b

def which_is_greater(x:int, y:int) -> int:
    """
    Takes two integers as input and returns 1 if the first
    one is larger, 0 if they''re equal, and -1 if the 
    second one is larger

    Parameters: 
    - x (int)
    - y (int)

    Returns:
    int: 1 if x > y, -1 if x < y, 0 if x = y
    """
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1

if __name__ == "__main__": 
    main()