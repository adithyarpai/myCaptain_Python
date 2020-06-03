#fibonacci series

terms = int(input("How many terms\n"))

x = 0
y = 1
counter = 0
if terms <= 0:
    print("Try again with a positve number")
elif terms == 1:
    print(x)
else:
   print("Fibonacci sequence:")
   while counter < terms:
    print(x)
    z = x + y
    # update values
    x = y
    y = z
    counter += 1
