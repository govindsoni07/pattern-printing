# Right-Aligned Triangle
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=5
for i in range(n):
    # First inner loop prints spaces
    for j in range(i,n):
        print(" ",end=" ")

    # Second inner loop prints stars
    for j in range(i+1):
        print("*",end=" ")
        
    # Moves to the next line after each row
    print()