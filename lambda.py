# Lambda Function to add 25 with the given number 

def add(x):
    return lambda num :  x + num                                    #lambda function

num = int(input("Enter a number to add 25 : "))                     #input frm user

result = add(25)                                                    #Calling the function
print("Result: ",result(num))