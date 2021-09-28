import numpy as np

def deflate ( mat, i, j ):
	mat1=np.delete(mat, i, 0)
	mat1=np.delete(mat1, j, 1)
	return mat1

def det ( mat ):
	shape = mat.shape
	if len(shape) != 2:
		print( "This is not a matrix")
		return 0
	if shape[0] != shape[1]:
		print ("This is not a square matrix")
		return 1
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
		
	
a = np.arange(16).reshape(4, 4)
print(a)
print(det(a))

a = np.arange(9).reshape(3, 3)
print(a)
print(det(a))

a = np.random.random((4,4))
print(a)
print(det(a))

a = np.random.random((5,5))
print(a)
print(det(a))

def main():
	file = open("matrix.txt","r")
	rows=file.readlines()
	list1=[]
	for u in rows:
		row=u.split()
		floatrow = np.asarray(row, dtype=np.float64)
		list1.append(floatrow)
		print(u)
	mat = np.asarray(list1, dtype=np.float64)
	print(mat)
	print(det(mat))
	file.close()


if __name__ == "__main__":
	main()

