#Function to read the matrix 
def read():
    row = int(input("Enter the no.of row's of matrix : "))
    col = int(input("Enter the no.of col's of matrix : "))
    l = list()
    for i in range(row):
        a = list()
        for j in range(col):
            print(f"l[{i}][{j}] = ")
            n = int(input())
            a.append(n)
        l.append(a)
    return (row,col,l)

#function to display the matrix 
def display(tpl):
    row = tpl[0]
    col = tpl[1]
    l = tpl[2]
    for i in range(row):
        for j in range(col):
            print(l[i][j],end=" ")
        print()
    print()

#function to Add the two matrixes
def addition():
    #First matrix input
    print("Enter the first matrix detail's ")
    tpl1 = read()
    row1 = tpl1[0]
    col1 = tpl1[1]
    l1 = tpl1[2]
    print("First Matrix ")
    display(tpl1)
    #Second matrix input
    print("Enter the second matrix detail's ")
    tpl2 = read()
    row2 = tpl2[0]
    col2 = tpl2[1]
    l2 = tpl2[2]
    print("Second Matrix ")
    display(tpl2)
    matrix = list()
    if(row1==row2 and col1==col2):
        for i in range(row1):
            a = list()
            for j in range(col1):
                a.append(l1[i][j]+l2[i][j])
            matrix.append(a)
    else:
        print("Matrix addition is not possible because two matrices order not same ")
        return 1
    print("Addation of two matrices is ")
    display((row1,col1,matrix))
    return matrix 

#function to Subtract the two matrixes
def subtraction():
    #First matrix input
    print("Enter the first matrix detail's ")
    tpl1 = read()
    row1 = tpl1[0]
    col1 = tpl1[1]
    l1 = tpl1[2]
    print("First Matrix ")
    display(tpl1)
    #Second matrix input
    print("Enter the second matrix detail's ")
    tpl2 = read()
    row2 = tpl2[0]
    col2 = tpl2[1]
    l2 = tpl2[2]
    print("Second Matrix ")
    display(tpl2)
    matrix = list()
    if(row1==row2 and col1==col2):
        for i in range(row1):
            a = list()
            for j in range(col1):
                a.append(l1[i][j]-l2[i][j])
            matrix.append(a)
    else:
        print("Matrix difference  is not possible because two matrices order not same ")
        return 1
    print("difference of two matrices is ")
    display((row1,col1,matrix))
    return matrix   
    
#function to Multiply  the two matrixes
def multiplication():
    #First matrix input
    print("Enter the first matrix detail's ")
    tpl1 = read()
    row1 = tpl1[0]
    col1 = tpl1[1]
    l1 = tpl1[2]
    print("First Matrix ")
    display(tpl1)
    #Second matrix input
    print("Enter the second matrix detail's ")
    tpl2 = read()
    row2 = tpl2[0]
    col2 = tpl2[1]
    l2 = tpl2[2]
    print("Second Matrix ")
    display(tpl2)
    matrix = list()
    a = list()
    if(col1==row2):
        for i in range(row1):
            for j in range(col2):
                sum = 0
                for k in range(col1):
                    sum += l1[i][k]*l2[k][j]
                a.append(sum)
            matrix.append(a)
    else:
        print("Matrix multiplication is not possible M1col != M2 row ")
        return 0
    print("Matrix multiplication is ")
    display((row1,col2,matrix))
    return matrix 

#Function to transpose the matrix 
def transpose():
    print("Enter the Matrix detail's ")
    tpl = read()
    row = tpl[0]
    col = tpl[1]
    l = tpl[2]
    print("Matrix before Transpose ")
    display(tpl)
    print("Matrix After Transpose ")
    matrix = list()
    for i in range(col):
        a = list()
        for j in range(row):
            a.append(l[j][i])
        matrix.append(a)
    display((col,row,matrix))
    return 0



#Main function for the python programme 
def main():
    while(1):
        print("Matrix Operation's ")
        print("\n1.Matrix Addition \n2.Matrix Subtraction \n3.Matrix Multiplication \n4.Transpose \n 5.exit")
        opt = int(input("Enter your option : "))
        if(opt==1):
            addition()
        elif(opt==2):
            subtraction()
        elif(opt==3):
            multiplication()
        elif(opt==4):
            transpose()
        elif(opt==5):
            break
        else:
            print(" Invalid Option ")
    
main()
x = 10
y = 20
print(f"the value of x = {x} and the value of y = {y}")

    