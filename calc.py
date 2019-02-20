

def add(x,y):
	return (x+y)

def substract(x,y):
	return(x-y)

def multiply(x,y):
	return(x*y)

def main():
	a = 7, b = 8
	print("Addition operation for a = ", a, " and b = ", b, " is ", add(a,b))
	print("Multiplication and substraction in one row below")
	print("Substract operation for a =", a," and b = ", b, " is", subtract(a,b), " and multiplication for a=" , a," and b= ", b ," is ", multiply(a,b))

if __name__ == '__main__':
	main()
	
