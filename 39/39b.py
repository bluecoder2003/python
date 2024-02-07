import numpy as np

matrix=np.random.randint(20,30,size=(4,4))

print("original matrix \n",matrix)
matrix_t=matrix.transpose()
matrix_t[1]=np.random.randint(20,30,size=4)
matrix=matrix_t.transpose()

print("inserted \n",matrix)
