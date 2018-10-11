import sys
def main():
    if (len(sys.argv) != 2 or int(sys.argv[1]) < 0):
        print("Wrong parameters, please especify an integer")
        return 
    print(check_if_odd(int(sys.argv[1])))

def check_if_odd(n):
    if n % 2 != 0:
        return True 
    return False

main()
