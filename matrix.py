import random
from copy import deepcopy
class Matrix:
    def __init__(self, mrows, ncols): #Construct a (mrows X ncols) matrix
        self.m = mrows 
        self.n = ncols 
        k = self.m   
        list1 = [ [0] * self.n ]
        while (k>1): #create a m*n matrix default value=0
            list1.append( [k] * self.n )  
            k -= 1
        for i in range ( 0, self.m ): 
            for j in range ( 0, self.n ):
                list1[i][j] = random.randint(0,9) 
        self.list = list1
        pass

    def add(self, m): #return a new Matrix object after summation
        print("========== A + B ==========")
        if ((self.m != m.m) or (self.n != m.n )):
            print("Matrix's size should be in the same size")
            return None
        else:
            add_matrix = deepcopy(m)
            for i in range( 0, self.m ):
                for j in range( 0, self.n ):
                    add_matrix.list[i][j] = self.list[i][j] + m.list[i][j]
                    #add_matrix[i][j] = self[i][j] + m[i][j]
            print(type(add_matrix))
            return add_matrix
        pass
        
    
    def sub(self, m): #return a new Matrix object after substraction
        print("========== A - B ==========")
        if ((self.m != m.m) or (self.n != m.n )):
            print("Matrix's size should be in the same size")
            return None
        else:
            sub_matrix = deepcopy(m)
            for i in range( 0, self.m ):
                for j in range( 0, self.n ):
                    sub_matrix.list[i][j] = self.list[i][j] - m.list[i][j]
                    #sub_matrix[i][j] = self[i][j] - m[i][j]
            return sub_matrix
        pass

    def mul(self, m): #return a new Matrix object after multiplication
        print("========== A * B ==========")
        multimatrix = deepcopy(self) 
        #multimatrix.list = [ [0] * m.n ]
        #while (k>1): #create a m*n matrix default value=0
        #    aaa.append( [k] * m.n )  
        #    k -= 1
        #print(aaa)
        #a=0
        #matrix = self.m*[m.n*[0]]
        
        for i in range( 0, self.m ):
            for j in range( 0, m.n ):
                multimatrix.list[i][j]=0
                for k in range( 0, self.n ):
                    multimatrix.list[i][j]+=self.list[i][k]*m.list[k][j]
        print(multimatrix)
        return multimatrix
        pass
    
    def transpose(self): #return a new Matrix object after transpose
        print("===== the transpose of A * B =====")
        tempmatrix = deepcopy(self)
        transmatrix = deepcopy (self)
        for i in range (0,self.m):
            for j in range(0,self.n):
                transmatrix.list[j][i] = tempmatrix.list[i][j]
        return transmatrix
        pass
    
    def display(self):
        if(self==None):
            pass
        for i in range( 0, self.m ):
            for j in range( 0, self.n ):
                print (self.list[i][j], sep=" " , end=" ")
                ##print (self[i][j], sep=" " , end=" ")
            print ("")
        print ("")
        pass

a_rows = int(input ( "Enter A matrix's rows : "))
a_cols = int(input ( "Enter A matrix's cols : "))
print ("Matrix A (" , a_rows, "," , a_cols, ") :")
A = Matrix ( a_rows , a_cols ) #create a instance obj A by class Matrix
A.display()

b_rows = int(input("Enter B matrix's rows : "))
b_cols = int(input("Enter B matrix's cols : "))
print ("Matrix B (" , b_rows, "," , b_cols, ") :")
B = Matrix ( b_rows , b_cols ) #create a instance obj B by class Matrix
B.display()
C = A.add(B) #C is a matrix obj, but return None if size of A is not equal to B
while (C): #if C is not None, display it
    print(type(C)) #<class '__main__.Matrix'>
    C.display()
    break
D = A.sub(B) #D is a matrix obj, but return None if size of A is not equal to B
while (D): #if D is None, display it
    D.display()
    break
E = A.mul(B)
while (E): #if D is None, display it
    E.display()
    break
T = E.transpose()
while (T):
    T.display()
    break
