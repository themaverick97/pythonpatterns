i=1
while(i<=5):
    j=i
    while(j<5):
        print(" ",end=" ")
        j=j+1
    k=1
    while(k<=i):
        print("*",end=" ")
        k=k+1
    print("")
    i=i+1


rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1
