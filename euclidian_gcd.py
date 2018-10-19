def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
   return x 

if __name__ == "__main__":
    x, y = map(int, raw_input().split())
    print computeGCD(x, y)