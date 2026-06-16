import numpy as np

# linear algebra
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.add(a, b))       # [5 7 9]
print(np.subtract(a, b))  # [-3 -3 -3]
print(np.multiply(a, b))  # [4 10 18]
print(np.divide(a, b))    # [0.25 0.4  0.5 ]
print(np.mod(a, b))       # [1 2 3]
print(np.power(a, b))     # [  1  32 729]

# rounding
c = np.array([1.4, 2.6, -3.5])
print(np.round(c))   # [1. 3. -4.]
print(np.floor(c))   # [ 1.  2. -4.]
print(np.ceil(c))    # [ 2.  3. -3.]
print(np.trunc(c))   # [ 1.  2. -3.]

#exponentiation
d = np.array([1, 2, 3])
print(np.exp(d))      # Exponential function e^x -> [ 2.718 7.389 20.085]
print(np.expm1(d))    # e^x - 1 (for small values to avoid precision errors) -> [ 1.718 6.389 19.085]
print(np.log(d))      # Natural logarithm (ln(x)) -> [0. 0.693 1.099]
print(np.log10(d))    # Logarithm base 10 -> [0. 0.301 0.477]
print(np.log2(d))     # Logarithm base 2 -> [0. 1. 1.585]
print(np.log1p(d))    # ln(1 + x) (for small x values) -> [0.693 1.099 1.386]

# trigonometric functions
#e = np.array([0, np.pi/2, np.pi])  # Array of angles in radians
e=np.array([0,1,2])
print(np.sin(e))      # Sine function -> [0.000 1.000 0.000]
print(np.cos(e))      # Cosine function -> [ 1.000  0.000 -1.000]
print(np.tan(e))      # Tangent function -> [ 0.000  1.633e16  0.000]

# Inverse trigonometric functions
print(np.arcsin([0, 1]))  # Arcsin (inverse sine) -> [0.  1.5708]
print(np.arccos([1, 0]))  # Arccos (inverse cosine) -> [0.  1.5708]
print(np.arctan([0, 1]))  # Arctan (inverse tangent) -> [0.  0.7854]

#Statistics
f = np.array([2,4,6,8])
g=np.array([3,7,5,9])
print(np.mean(f))       # Mean (average) -> 3.0
print(np.median(f))     # Median -> 3.0
print(np.std(f))        # Standard deviation -> 1.414
print(np.var(f))        # Variance -> 2.0
print(np.cov(f,g))  # Covariance of 'f' -> Single value, variance since it's 1D
print(np.corrcoef(f,g))  # Correlation coefficient -> 1.0 (since f is perfectly linear)
# Given correlation matrix
corr_matrix = np.array([[1.0, 0.8], [0.8, 1.0]])
#Extract correlation between the two variables (off-diagonal element)
corr_value = corr_matrix[0, 1]  # or corr_matrix[1, 0]
print(corr_value)  # Output: 0.8
print(np.min(f))        # Minimum value -> 1
print(np.max(f))        # Maximum value -> 5
print(np.percentile(f, 50))  # 50th percentile (median) -> 3.0
print(np.quantile(f, 0.5))   # 50th quantile (same as median) -> 3.0

# Matrix operations
g = np.array([[1, 2], 
              [3, 4]])
h = np.array([[5, 6], 
              [7, 8]])
e=np.array([[8,-8,2],[4,-3,-2],[3,-4,1]])
print(np.dot(g, h))       # Dot product -> [[19 22] [43 50]]
print(np.matmul(g, h))    # Matrix multiplication -> [[19 22] [43 50]]
print(np.linalg.inv(g))   # Inverse of matrix g -> [[-2.   1. ] [ 1.5 -0.5]]
print(np.linalg.det(g))   # Determinant of matrix g -> -2
print(np.linalg.eig(e))   # Eigenvalues and Eigenvectors of g
print(np.linalg.svd(g))   # Singular Value Decomposition (SVD)
print(np.linalg.norm(g))  # Norm of matrix g -> 5.477

# Random numbers
np.random.seed(42)  # Set random seed for reproducibility

print(np.random.rand(3))           # Random numbers from uniform distribution [0,1]
print(np.random.randn(3))          # Random numbers from normal distribution (mean=0, std=1)
print(np.random.randint(1, 10, 3)) # Random integers between 1 and 10
print(np.random.choice([10, 20, 30], 2)) # Randomly pick 2 values from given list

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)  # Shuffle the array randomly
print(arr)

#miscellaneous 
i = np.array([-5, -1, 0, 1, 5])

print(np.abs(i))      # Absolute value -> [5 1 0 1 5]
print(np.sign(i))     # Returns sign: -1 (negative), 0 (zero), 1 (positive) -> [-1 -1  0  1  1]
print(np.clip(i, -2, 2)) # Clips values between -2 and 2 -> [-2 -1  0  1  2]
print(np.cumsum(i))   # Cumulative sum -> [-5 -6 -6 -5  0]
print(np.cumprod(i))  # Cumulative product -> [ -5   5   0   0   0]
