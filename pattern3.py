# Inverted Right-Angled Triangle

'''
* * * * *
* * * *
* * *
* *
*
'''
n=5
for i in range(n,0,-1): #rows
    for j in range(i):   #cols
        print("*",end=" ")
    print()
