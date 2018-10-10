n = int(input("Enter no of terms.."))

firstNum = 0
secondNum = 1

for i in range(n):
    print(firstNum,end=' ,')
    temp = firstNum + secondNum
    firstNum = secondNum
    secondNum = temp
    
        
        

