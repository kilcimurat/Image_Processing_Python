#Simge Uçkun-180403053-hw6
#15.12.2023

from random import random, gauss
import math
import cv2
import numpy as np
def noises(type,M,N,a,b):
    if type=="uniform":
        n=np.zeros([M,N])
        for i in range(M):
            for j in range(N):
                n[i,j]=random()

        R=a+(b-a)*n
        return R
    elif type=="gaussian":
        n = np.zeros([M, N])
        for i in range(M):
            for j in range(N):
                n[i, j] = gauss(0,1)
        R = a + b * n
    elif type== "lognormal":
        n = np.zeros([M, N])
        for i in range(M):
            for j in range(N):
                n[i, j] = gauss(0,1)
        R=a*np.exp(b*n)
    elif type=="rayleigh":
        n = np.random.rand(M, N)
        R = a + (-b * np.log(1 - n)) ** 0.5
        return R
    elif type == "exponential":
        n = np.zeros([M, N])
        for i in range(M):
            for j in range(N):
                n[i, j] = random()
        k = -1 / a
        R = k * np.log(1 - n)
    elif type=="erlang":
        n = np.zeros([M, N])
        for i in range(M):
            for j in range(N):
                n[i, j] = random()
        k = -1 / a
        R = np.zeros([M, N])
        for i in range(b):
            R = R + k * np.log(1 - n)
    return R

def salt_papper(image,prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def add_periodic(img):
    orig = img
    sh = orig.shape[0], orig.shape[1]
    noise = np.zeros(sh, dtype='float32')

    X, Y = np.meshgrid(range(0, sh[0]), range(0, sh[1]))

    A = 40
    u0 = 45
    v0 = 50

    noise += A*np.sin(X*u0 + Y*v0)

    A = -18
    u0 = -45
    v0 = 50

    noise += A*np.sin(X*u0 + Y*v0)

    noiseada = orig+noise
    return(noiseada)


