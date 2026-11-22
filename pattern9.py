# Diamond
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=5
for i in range(n):
    # Print decreasing spaces
    for j in range(i,n-1):
        print(" ",end=" ")
        
    # Print increasing stars
    for j in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(n-1):
    # Print increasing spaces
    for j in range(i+1):
        print(" ",end=" ")

    # Print decreasing stars (first half)
    for j in range(i,n-1):
        print("*",end=" ")

    # Print decreasing stars (second half)
    for j in range(i,n-2):
        print("*",end=" ")

    print()