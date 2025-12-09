# count number of digits in a number
a = int(input("enter a number: "))
count = 0
if a == 0:
    count = 1
else:
    while a > 0:
        a //= 10
        count += 1
print(count)
