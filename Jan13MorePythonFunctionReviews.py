#function definition
def circleCircumference(r):
    return 3.14*r*2

result = circleCircumference(5) # function call
print("The sum of the numbers is:", result)

#function definition
def iseven(num):
    if num%2==0:
        return True
    else:
        return False

result = iseven(8)
print(result)
result = iseven(3)
print(result)

#function defintion
def frog(num):
    for i in range(num):
        print("ribbit")
        
        
frog(5) #function call
