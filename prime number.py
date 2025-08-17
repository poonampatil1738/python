s = int(input("Enter start of range: "))
e = int(input("Enter end of range: "))

for x in range(s, e):
    if x > 1:  # Only numbers greater than 1 can be prime
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print(x, end=" ")
