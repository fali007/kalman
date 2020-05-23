from math import *
import numpy as np
# import matplotlib.pyplot as plt

def gaussian(mean, var,x):
    coeff=1/sqrt(2*pi*var**2)
    expo=exp((x-mean)**2/(-2*var**2))
    return coeff*expo
def update(m1,v1,m2,v2):
    mean=(v2*m1+v1*m2)/(v1+v2)
    var=1/(1/v1+1/v2)
    return [mean,var]
def predict(m1,v1,m2,v2):
    mean=m1+m2
    var=v1+v2
    return [mean,var]
measurements = [5., 6., 7., 9., 10.]
motions = [1., 1., 2., 1., 1.]

measurement_sig = 4.
motion_sig = 2.
mean = 0.
var = 10000.
for n in range(len(measurements)):
    mean,var=update(mean,var,measurements[n],measurement_sig)
    mean,var=predict(mean,var,motions[n],motion_sig)
    print("[{}, {}]".format(mean,var))
