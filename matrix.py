import random
from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        pass

    def sub(self, m):
        """return a new Matrix object after substraction"""
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        pass
    
    def display(self):
        """Display the content in the matrix"""
        pass

m=4
n=2
k=m
list1=[[1]*n]
list2=[1]*n

for i in range (1,n+1):
    list1[0][i-1]=random.randint(0,9)

while (m>1):
    list1.append(list2)  
    m-=1

for i in range(1,k):
    list1[i]=[1]*k
    for j in range (0,k):
        list1[i][j]= random.randint(0,9)

for i in range(0,k):
    for j in range(0,n):
        print (list1[i][j],sep=" ",end=" ")
    print ("")
