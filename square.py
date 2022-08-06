# programm to sqaure the element of a list by using Map() function

num = int(input("Enter the total number of elements in the list: "))          # Taking input from the user
lst = []
for i in range(num):
    ele = int(input("Enter element: "))
    lst.append(ele)
print("Oeiginal List: ",lst)

def squre (lst):
    return lst**2                                                             # Function to squaare all  the elements of the list

data = list(map(squre,lst))                                                   

print(data)

