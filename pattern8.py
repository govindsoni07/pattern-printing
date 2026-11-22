# Inverted Star Pyramid
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=5
for i in range(n):
    # First inner loop prints increasing spaces
    for j in range(i+1):
        print(" ",end=" ")

    # Second inner loop prints the left half of the stars
    for j in range(i,n):
        print("*",end=" ")

    # Third inner loop prints the right half of the stars
    for j in range(i,n-1):
        print("*",end=" ")
    # Moves to the next line
    print()