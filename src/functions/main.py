# def function_name(parameters):
# always snake_case, starting with action verb

def main():
    """
    Special function that takes no inputs, produces no outputs, but 
    that constitutes the runnable component of our program
    """

    print("Functions in Python.")

    # calling the function
    x = 3
    y = 2.7
    n = sum_two_ints(x, 4) #(floats won't break the code)
    print("The sum of 3 and 4 is", n)
    print(double_and_duplicate(y))
    print_hi()

    # let's call add_one()
    m = 17
    print(add_one(m)) # we are not changing the underlying value of m when calling function
    print("m is now", m) # what happens here? m is not changed by function call
    
    # With basic types (str, int, float, etc.) Python uses "pass by value". 
    # When a variable is passed into a funtion as a parameter, a copy is created. 

    # "Pass by reference" means that when you pass a variable into a function, you can change it!
    # All of this is not technically quite right :)
    # Python does use pass by reference for some things. 

def sum_two_ints(a:int, b:int) -> int: # type hints are just hints. You can still do indented things due to Python's hyper-flexibility
    """
    Doc string
    1. explain the function
        Returns the sum of two input integers. 
    2. input
        Parameters: 
        - a (int)
        - b (int)
    3. output
        Returns:
        int: a + b 
    """
    return a+b # this is the output of the function

# Functions can also return more than one value
def double_and_duplicate(x: float) -> tuple[float, float]: # tuple is when you 
    """
    Double the input variable and return two copies of it. 

    Parameters:
    - x (float)

    Returns:
    Two copies of 2*x
    """
    return 2*x, 2*x 

# Functions do not have to take input or return anything
def print_hi():
    """
    Takes no input and simply prints "Hi" to the console.
    """
    print("Hi")
    # other things could happen here???
    # nothing ultimately gets returned by the function

def add_one(k: int) -> int:
    """
    Add one to the input variable and return the result.

    Parameters: 
    - k (int)

    Returns:
    int: k+1
    """
    # return k + 1
    k = k+1 # this looks wrong, BUT: Left side is variable. Right side is values. 
    return k
    # k has served its meaningful life. See main() - m is used. 

# The definition of function can occur in any order
# BUT ... when excutions are executed, definitions must have already 
# been encountered
# the below says, run what is inside def main()
if __name__ == "__main__": 
    main()