#%%
from scipy import sparse
from numpy import random

#%%
# Demo with sparse matrix.
##
# create a 30x1000 dense matrix random matrix.
D = random.random((30, 1000))
# keep entries with value < 0.10 (10% of entries in matrix will be non-zero)
# X is a "full" matrix that is intrinsically sparse.
X = D * (D < 0.10)  # note: element wise mult

# convert D into a sparse matrix (type coo_matrix)
S = sparse.coo_matrix(X)
print(S)
