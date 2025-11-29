"""
Bugfix summary:
1. factorial function did not handle the case when n is negative
2. factorial function did not make sure n is an integer
3. fibonacci function did not handle the case when n is negative
4. fibonacci function did not make sure n is an integer
5. when factorial and fibonacci are called, the input argument is not passed
"""

def factorial(n):
    #bugfix: factorial function did not handle the case when n is negative
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers")
    #bugfix: make sure n is an integer
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers")
    
    if n == 0:
        return 1
    return n * factorial(n - 1)  



def fibonacci(n):
    #bugfix: fibonacci function did not handle the case when n is negative
    if n<0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    #bugfix: make sure n is an integer
    if not isinstance(n, int):
        raise ValueError("Fibonacci is only defined for integers")

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        #bugfix: factorial function must have an input argument
        #ans = factorial()
        #ans= factorial(-1)
        #ans= factorial(1.5)
        ans = factorial(5)
    elif choice == "2":
        #bugfix: fibonacci function must have an input argument
        #ans = fibonacci()
        #ans= fibonacci(-1)
        #ans= fibonacci(1.5)
        ans = fibonacci(5)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
