#Lists, tuples and dictionaries

#Assigning elements to a list
n1 = int(input("Enter the number of elements for list\n"))
list1 = []

print("Enter the elements")
for i in range(0, n1):
    ele = input()
    list1.append(ele)

print("The elements are ")
print(list1)


#Accesing elements of a tuple
n2 = int(input("Enter the number of elements for tuple\n"))
tuple1 = []

print("Enter the elements")
for i in range(0, n2):
    ele = input()
    tuple1.append(ele)
 
print("The elements are ")
tuple1 = tuple(tuple1)
print(tuple1)

ch = int(input("Enter the index of element you want to access\n"))
if ch < len(tuple1):
    print(tuple1[ch])
else:
    print("Invaild index")


#Deleting elements from dictionary
n3 = int(input("Enter the number of keys for dictionary\n"))
dict1 = {}

print ("enter the keys and values\n")
for i in range(0, n3):
    k = input()
    v = input()
    dict1[k]=v

print(dict1)

delete = input("Enter key to be deleted\n")
if delete in dict1:
    del dict1[delete]
    print(dict1)
else:
    print("Invaild key")
