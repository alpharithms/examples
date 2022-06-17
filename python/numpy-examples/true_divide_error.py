"""
Example to illustrate the division of NumPy arrays containing a zero or NaN value
such that the following error occurs:

    runtimewarning: invalid value encountered in true_divide

@author: Zack West <alphazwest@gmail.com>
@version: 6/16/2022
"""
import numpy as np

# Define some arrays
a_1 = [6, 7, 8, 9, 10]
a_2 = [1, 2, 3, 4, 5]

# print output sample true_divide operation
print(np.true_divide(a_1, a_2))

# use a single value as well
print(np.true_divide(a_1, 3))

# # implicit use via / and // operators
# # Error
# print(a_1 / a_2)
#
# Implicit use after converting to an array
print(np.array(a_1) / np.array(a_2))

# Implicit use after converting to an array,
# and using static value
print(np.array(a_1) / 3)

# Use of floor division
print(np.array(a_1) // np.array(a_2))

# Use of floor division with single value
# Use of floor division
print(np.array(a_1) // 3)

# Elementwise division of two lists
vals = [x / a_2[i] for i, x in enumerate(a_1)]
print(vals)

# Elementwise division of two lists, using floor division
vals = [x // a_2[i] for i, x in enumerate(a_1)]
print(vals)

print('------------------- true divide examples ---------------------')
b_1 = np.array([5, 6, 7, 8, 0])
b_2 = np.array([1, 2, 3, 4, 1])

print(np.true_divide(b_1, b_2))




