# Create a class rectangle
class Rectangle():
	# Initialize two parameters using self
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    # compute area method
    def area(self):
        return self.breadth*self.length
# Enter length 
a=int(input("Enter length of rectangle: "))
# Enter breadth
b=int(input("Enter breadth of rectangle: "))
# Create instance of a class
inst=Rectangle(a,b)
print("Area of rectangle:",inst.area())
 
