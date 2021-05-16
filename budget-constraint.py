"""
@author: Melika_Golgoon
"""

import numpy as np

from scipy.optimize import fsolve

def func(teta_star):
    b = 0
    for i in range(j):
        a = c[i]*np.sqrt(2*D[i]*A[i]/(h[i]+2*teta_star*c[i]))
        b = b + a
    return b-x


print("Welcome")
print("Please specify your total budget limit : ")
x = float(input())
print("Please specify how many types of products do you have ?")
j = int(input())


D = np.zeros([j])
c = np.zeros([j])
h = np.zeros([j])
A = np.zeros([j])

for counter in range(j):

    print("for product ", str(counter+1), " ,how many products of this kind are demanded? ")
    D[counter] = int(input())
    print("for product ", str(counter+1), " , what is the price of this product ?")
    c[counter] = float(input())
    print("for product ", str(counter+1), " , what is the cost of maintaining this product?")
    h[counter] = float((input()))
    print("for product ", str(counter+1), " , what is the cost of ordering this product?")
    A[counter] = float(input())

Q_w = np.sqrt(2*D*A/h)
flag = sum(c*Q_w) <= x

if flag == True:
    Q_star = Q_w
else:
    teta_star = fsolve(func,0)

    Q_star = np.zeros([j])
    for i in range(j):
        Q_star[i] = np.sqrt(2*D[i]*A[i]/(h[i]+2*teta_star[0]*c[i]))

print(np.floor(Q_star))
