# Star Pyramid
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

n=5
for i in range(n):
    
    # First inner loop prints spaces
    for j in range(i,n):
        print(" ",end=" ")

    # Second inner loop prints odd numbers of stars
    for j in range(2*i+1):
        print("*",end=" ")

    # Moves to the next line
    print()