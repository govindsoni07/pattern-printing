# Repeated Row Number Triangle
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n=5
for i in range(1,n+1): #rows
    for j in range(1,i+1): #cols
        print(i,end=' ')
    print()