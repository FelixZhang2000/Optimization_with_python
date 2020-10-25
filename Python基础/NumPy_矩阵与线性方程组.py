#利用numpy实现矩阵的各种运算
import numpy as np

a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[6,5,4],[3,2,1]])

#矩阵对应元素相乘
print(a1*a2)

#矩阵点乘
print(a1*3)

#矩阵乘法用np.dot(x1,x2)函数
a3 = a2.T#矩阵转置
print(np.dot(a1,a3))

#矩阵求逆用np.linalg.inv(a)函数
a = np.array([[1,2,3],[4,5,6],[5,4,3]])
print(np.linalg.inv(a))

#矩阵特征值与特征向量:np.linalg.eig(a)函数
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
eigenValues, eigenVectors = np.linalg.eig(a)
print(eigenValues)
print(eigenVectors)

#奇异值分解:np.linalg.svd(a)函数
U, sigma, V = np.linalg.svd(a)
print(U)
print(sigma)
print(V)

#矩阵行列式:np.linalg.det(a)函数
value = np.linalg.det(a)
print(value)

#QR分解：np.linalg.qr(a)函数
Q, R = np.linalg.qr(a)
print(Q)
print(R)

#求解线性方程组
#x - 2y + z = 0
#2y - 8z = -8
#-4x + 5y +9z = 9
A = np.array([[1,-2,1],[0,2,-8],[-4,5,9]])
b = np.array([0,-8,9])

result = np.linalg.solve(A, b)#result是一个数组
