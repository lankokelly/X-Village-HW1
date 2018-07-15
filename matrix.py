import random
import copy
from copy import deepcopy
class Matrix:
    def __init__(self, mrows, ncols):
        """Construct a (mrows X ncols) matrix"""
        self.m = int( mrows )
        self.n = int( ncols )
        k = self.m
        
        list1 = [ [1] * self.n ]
        list2 = [1] * self.n
        
        for i in range ( 1, self.n+1 ):
            list1[0][i-1] = random.randint(0,9)
        while (k>1):
            list1.append( list2 )  
            k -= 1
        for i in range ( 1, self.m ):
            list1[i] = [1] * self.n
            for j in range ( 0, self.n ):
                list1[i][j] = random.randint(0,9)
        for i in range( 0, self.m ):
            for j in range( 0, self.n ):
                print (list1[i][j], sep=" " , end=" ")
            print ("")
        print ("")  
        self.list = list1
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        print("========== A + B ==========")
        add_matrix = copy.deepcopy(m)
        for i in range( 0, self.m ):
            for j in range( 0, self.n ):
                add_matrix.list[i][j] = self.list[i][j] + m.list[i][j]
                print (add_matrix.list[i][j], sep=" " , end=" ")
            print ("")
        print ("")
        return add_matrix
        pass
    
    def sub(self, m):
        """return a new Matrix object after substraction"""
        print("========== A - B ==========")
        sub_matrix = copy.deepcopy(m)
        for i in range( 0, self.m ):
            for j in range( 0, self.n ):
                sub_matrix.list[i][j] = self.list[i][j] - m.list[i][j]
                print (sub_matrix.list[i][j], sep=" " , end=" ")
            print ("")  
        print ("") 
        return sub_matrix
        pass

a_rows = input ( "Enter A matrix's rows : ")
a_cols = input ( "Enter A matrix's cols : ")
print ("Matrix A (" , a_rows, "," , a_cols, ") :")
A = Matrix ( a_rows , a_cols )

b_rows = input("Enter B matrix's rows : ")
b_cols = input("Enter B matrix's cols : ")
print ("Matrix B (" , b_rows, "," , b_cols, ") :")
B = Matrix ( b_rows , b_cols )

C = A.add(B)
print (type(C))
D = A.sub(B)
print (type(D))