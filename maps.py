# program to triple all numbers of a given list of integers by using Python map

num = int(input("Enter the total number of elements in the list: "))       # Taking user-input for a list
lst = []
for i in range(num):
    ele = int(input("Enter element: "))
    lst.append(ele)
print("Oeiginal List: ",lst)


def triple(lst):                                                           # Function to triple all  the elements of the list
    return lst*3

result = list(map(triple,lst))                                             # Calling the function inside map and converting data to List 
print("Triples of list Numbers: ",result)