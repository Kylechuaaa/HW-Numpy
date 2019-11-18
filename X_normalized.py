import numpy as np
M = np.random.random((5,5))
print (M)


N = M.mean()
print (' ')
print ("The mean is: ", N)


O = M.std()
print (' ')
print("Input the standard deviation: ", O)


P = (M - N)/O
print (' ')
print ("The normalized M is: ", P)