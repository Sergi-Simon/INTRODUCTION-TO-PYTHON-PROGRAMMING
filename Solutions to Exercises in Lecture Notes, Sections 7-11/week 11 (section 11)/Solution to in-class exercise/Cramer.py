import numpy as np

def deflate ( mat, i, j ):
    mat1=np.delete(mat, i, 0)
    mat1=np.delete(mat1, j, 1)
    return mat1

def det ( mat ):
    shape = mat.shape
    if len(shape) != 2:
        print( "This is not a matrix")
        return []
    if shape[0] != shape[1]:
        print ("This is not a square matrix")
        return []
    if shape==(1,1):
        return mat[0,0]
    if shape == (2,2):
        return mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0]
    n = shape[0]
    s = 0
    p = 1
    for j in range(n):
        mat1=deflate( mat, 0, j )
        s += mat[0,j]*det(mat1)*p
        p = -p
    return s

def main():
    file = open("system.txt","r")
    rows=file.readlines()
    num_rows = len(rows)
    list1=[]
    list2=[]
    for i in range(int(num_rows/2)):
        u = rows[i]
        row=u.split()
        list1.append(row)
    for i in range(int(num_rows/2),num_rows):
        list2.append(float(rows[i]))
    mat = np.asarray(list1, dtype=np.float64)
    b = np.asarray(list2, dtype=np.float64)
    x = Cramer( mat, b )
    print(x)
    file.close()
def Cramer ( mat, b ):
    shape = mat.shape
    x=[]
    if shape[0] != shape[1]:
        print("Your matrix is not square")
        return -1
    det_a = det(mat)
    n = shape[0]
    for j in range(n):
        mat1 = np.copy(mat)
        for i in range(n):
            mat1[i,j]=b[i]
        det1=det(mat1)
        x.append(det1/det_a)
    return x
    

if __name__ == "__main__":
    main()

