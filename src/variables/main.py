def main():
    print("Variables.")

    # declare variables

    j = 14      # int
    x = -2.3    # float
    yo_world = "Hi" # str, this is snake_case
    statement = True # bool variable 

    print(j)
    print(x)
    print(yo_world)
    print(statement)

    # print(j, x, yo_world, statement)

    # tab is 4 spaces
    # unexpected space -> indentation error 
    # Python uses dynamic typing (type of variable can change)  
    j = 20
    print(j)
    print("j has type", type(j))

    print(type(j), type(x), type(yo_world), type(statement))

    # math
    print(x + 2*(j+5))

    # python allows mixed type math
    print(x*j)

    print("After multiplication, j has type", type(x*j))

    # we have 3 additional operations
    print(14/3)     # 4.66666...
    print(14//3)    # this is integer division (4)
    print(14%3)     # this tells us the remainder (2)
    print(14**3)    # this gives us 14 to the power of 3 

if __name__ == "__main__": 
    main() 

