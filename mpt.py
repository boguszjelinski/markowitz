from cvxopt import matrix
from cvxopt.solvers import qp
import numpy as np
n = 4
Cov = matrix([[0.076900, 0.039968, 0.018111, -0.000288 ],
    [ 0.039968, 0.050244, 0.019033, -0.000060 ],
    [ 0.018111, 0.019033, 0.021381, 0.007511 ],
    [-0.000288, -0.000060, 0.007511, 0.008542 ]])
Mean = matrix([0.0073, 0.0346, 0.0444, 0.0271])
r_min = 0.035
G = matrix(np.concatenate((-np.transpose(Mean), -np.identity(n)), 0))
h = matrix(np.concatenate((-np.ones((1,1))*r_min, np.zeros((n,1))), 0))
A = matrix(1.0, (1,n))
b = matrix(1.0)
q = matrix(np.zeros((n, 1)))
sol = qp(Cov, q, G, h, A, b)
print(sol[’x’])