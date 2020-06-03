#Print positive numbers in a list

n = int(input("Enter number of elements : \n"))
list1 = []
print("Enter  elements :\n")
for i in range(0, n): 
    ele = int(input()) 
  
    list1.append(ele)
     
print(list1)
print("Positive  elements :\n")
for i in list1
:
    if i >= 0 :
        print(i, end = " ")
