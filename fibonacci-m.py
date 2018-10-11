import sys
def main():
    if len(sys.argv) != 2:
        print("Wrong parameters number")
        return -1
    n = int(sys.argv[1])
    print(fibonacci(n))

def fibonacci(n):
    fib = {0:0, 1:1, 2:1}

    if n in fib:
        return fib[n]
    else:
        fib[n] = fibonacci(n - 2) + fibonacci(n - 1)
        return fib[n]
main()
