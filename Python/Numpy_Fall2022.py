# %%
import numpy as np
# %%
# Access NumPy functions with np.<function>
my_array = np.array([1, 2, 3, 4])
# %%
print(my_array)
# %%
print(2*my_array)
# %%
print(np.sqrt(my_array))

# %%
matrix_A = np.array([[10.5, 63], [12, 66],[10, 68],[11,70]])
# %%
print(matrix_A)

# %%
matrix_A.shape

# %%
print(matrix_A/10)  # This will NOT work on a standard list!

# %%
# This will NOT work on a standard list!
print(matrix_A * (1/matrix_A))

# %%
# element:            0  1  2  3  4  5  6
my_vector = np.array([0,10,20,30,40,50,60])

# %%
print(my_vector[3])
# %%
print(my_vector[2:5])
# %%
my_vector[2:5] = 100
# %%
print(my_vector)
# %%
print(matrix_A)
# %%
print(matrix_A[1,1])
# %%
print(matrix_A[0:2,:]) # ':' alone gives all elements

# %%
# one layer of square brackets
arr_1d = np.array([1, 2, 3, 4])
# %%
# 2 layers of square brackets
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
# %%
# 3 layers of square brackets
arr_3d = np.array([[[1, 2, 3, 4],
                    [5, 6, 7, 8]],
                  [[9, 10, 11, 12],
                   [13, 14, 15, 16]]])

# %%
arr_3d[0,:,:]
# %%
print(my_vector)

# %%
a_slice = my_vector[1:3]
# %%
print(a_slice)

# %%
a_slice[:] = 27

# %%
print(my_vector)

# %%
print(matrix_A)

# %%
matrix_A.mean()
# %%
matrix_A.std()

# %%
# axis = index we are aggregating ACROSS
matrix_A.mean(axis = 0)
# %%
matrix_A.std(axis = 0)

# %%
print(arr_3d.mean(axis=0))
# %%
print(arr_3d.sum(axis=0))
# %%
A = np.array([[1, 2, 3],
              [3, 2, 1]])
# %%
B = np.array([[1, 4],
              [0, 3],
              [2,1]])

# %%
print(A + A)
# %%
print(3*A)
# %%
AB = np.dot(A,B)
# %%
print(AB)

# %%
from numpy.linalg import inv
# %%
ABinv = inv(AB)
# %%
print(ABinv)
# %%
print(np.dot(AB, ABinv))
# %%
np.arange(10,15)
# %%
zeros = np.zeros((2,2))
# %%
ones = np.ones((2,2))
# %%
a_matrix = np.array([[1,2,3],[4,5,6]]) # 2 by 3 matrix
# %%
np.zeros_like(a_matrix)
# %%
np.random.uniform()
# %%
np.random.normal(loc = 10, size = (3,1))

# %%
# change dtype between DP: float64, SP: float32, HP: float16
Random_Mat = np.random.uniform(size = (6000,6000)).astype('float64')
# %%
print(Random_Mat.dtype)
# %%
from sys import getsizeof
# %%
getsizeof(Random_Mat)/1024/1024 # size in MB

# %%
import time # provides accurate timing
# %%
t0 = time.time()
# %%
inv = np.dot(Random_Mat,Random_Mat)
# %%
print(f"Matrix inversion took {np.round(time.time() - t0, 2)}s")
# %%
ones_DP = np.ones((2,2)).astype("float64")
# %%
ones_SP = np.ones((2,2)).astype("float32")
# %%
(ones_DP + ones_SP).dtype

# %%
np.sqrt(4)
# %%
np.cos(3.14159265358979)

# %%
np.exp(ones_DP + ones_SP) # elementwise operation: exp(2)

# %%
from scipy import pi
# %%
from scipy.interpolate import interp1d
# %%
xSeq = np.linspace(0, pi, 20)
# %%
ySeq = np.sin(2 * pi * xSeq)

# %%
Yinterp = interp1d(xSeq, ySeq) # kind argument for type of interpolation
# %%
type(Yinterp)
# %%
xInterpSeq = np.linspace(0, pi, 100)
# %%
ySeq[0:3]
# %%
Yinterp(xInterpSeq)[0:10]

# %%
# quad: automatic integration routines via the
# QUADPACK FORTRAN library
from scipy.integrate import quad
# %%
def stdnorm(x):
  return np.exp(-(x**2)/2)

# %%
quad(stdnorm, -1*np.inf, np.inf)[0]
# %%
np.sqrt(2*pi)

# %%
from scipy.optimize import minimize
# %%
minimize(lambda x: x**2, x0=1)

# %%
from scipy.optimize import minimize
# %%
opt = minimize(lambda x: -1*(-x**2 + 1), x0 = 1)
# %%
opt

# %%
print(f"The maximum is {-1*opt.fun}")

# %%
from scipy import stats
# %%
NormalDist = stats.norm() # N(0,1) by default
# %%
type(NormalDist)
# %%
NormalDist.support()
# %%
NormalDist.stats()
# %%
from scipy.optimize import minimize
# %%
from tqdm import tqdm # for sweet progress bar
# %%
def RoU_Samp(p, n):
  a=0
  b = -1*minimize(lambda x: -1*np.sqrt(p(x)), x0=1).fun
  c =    minimize(lambda x:  x*np.sqrt(p(x)), x0=1).fun
  d = -1*minimize(lambda x: -x*np.sqrt(p(x)), x0=1).fun
  # stats.uniform(loc, scale) == U(loc, loc + scale)
  U1 = stats.uniform(0, b)
  U2 = stats.uniform(c, d - c)

  FinalSamples = np.zeros(n, dtype='float64')
  for i in tqdm(range(FinalSamples.shape[0])):
    while True:
      u1Sample = U1.rvs()
      u2Sample = U2.rvs()
      if u1Sample <= np.sqrt(p(u2Sample/u1Sample)):
        break
    FinalSamples[i] = u2Sample/u1Sample
  return FinalSamples

# %%
randomVals = RoU_Samp(p = stdnorm, n = 10000)
# %%
np.histogram(randomVals,bins = 5)

