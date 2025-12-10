i=1
j=1
while (i<=50):
    count = 0
    while (j<=1):
        if j % i==0:
            count +=1
        j+=1
    i+=1
if count == 2:
    print(i)
