# STACK: Stack is a linear data structure which follows the principle
# LIFO: Last in first out

# create a class stack

class Stack:

	# Create an empty list of string

	def __init__(self):
		self.items = []

	# Check if stack is empty or not

	def isEmpty(self):
		return self.items == []

	# push element in stack from top

	def push(self, item):
		self.items.append(item)

	# Pop elements

	def pop(self):
		return self.items.pop()

	# check peek elements

	def peek(self):
		return self.items[len(self.items)-1]

	# Check size of stack

	def size(self):
		return len(self.items)

	def total(self):
		return self.items

# Instance of class Stack
s = Stack()
print(s.isEmpty())
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.size())
print(s.total())
s.pop()
print(s.total())