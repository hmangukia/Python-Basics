
# program for print fibonacci numbers in python by Sahaj Jain

def ReturnFibo(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return ReturnFibo(n-1)+ReturnFibo(n-2) 
    
print(ReturnFibo(9)) 
  
