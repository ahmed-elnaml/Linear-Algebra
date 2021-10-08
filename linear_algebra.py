import numpy as np
import time as time

b = np.array([[2, 3, 6, 9], [5, 7, 9, 3], [0, -1, 7, 8], [5, -1, 0, 8]])


def gau_elmnt(n: np.array):
    "this function is to perform gauassiuan elemination to calcute the det"
    a = np.array(n, dtype=float);
    if a[0, 0] != 1:
        a[0] = a[0] / a[0, 0]

    for r in range(len(a)):
        for c in range(r):
            if a[r, c] == 0:
                pass
            else:
                if c == 0:
                    a[r] = a[r] - a[0] * a[r, c]
                else:
                    a[r] = a[r] - a[r - 1] * (a[r, c] / a[r - 1, c])
    return a


# print(np.linalg.det(b))
# print(np.linalg.det(gau_elmnt(b)))

# print(gau_elmnt(b))

def minor(n: np.array, r, c):
    a = np.delete(n, r, 0)
    a = np.delete(a, c, 1)
    return a


def det(n: np.array):
    a = np.array(n, dtype=float)
    re = 0
    if a.shape == (2, 2):
        return a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0]
    else:
        for (key, val) in enumerate(n[0]):
            re += (-1) ** key * val * det(minor(a, 0, key))
    return re


def trans(n: np.array):
    a = np.zeros(n.shape)
    for r in range(len(n)):
        for c in range(len(n[r])):
            a[r, c] = n[c, r]
    return a


def adj(n: np.array):
    a = np.zeros(n.shape,dtype=float)
    for r in range(len(n)):
        for c in range(len(n[r])):
            a[r,c] = (-1) ** (r+c) * det(minor(n, r, c))
    return a

def inv(n: np.array):
    return (1/det(n))*trans(adj(n))


print(det(b))
print(np.linalg.det(b))
