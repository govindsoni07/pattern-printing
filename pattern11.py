# Hollow Right-Angled Triangle
'''
*
* *
*   *
*     *
* * * * *
'''
n=5
for i in range(n):
    for j in range(i+1):
        # Check boundary conditions
        if i==n-1 or j==0 or j==i:
            print("*",end=" ")
        # Print spaces inside the triangle
        else:
            print(" ",end=" ")
    # Move to the next row
    print()