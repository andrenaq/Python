# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:11:41 2017

@author: andre
"""

import cv2
import numpy as np

def dummy (val):
    pass

identity_kernal = np.array([[0,0,0] ,[0,1,0]  ,[0,0,0]])
sharpen_kernel =  np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
mean_kernel =  np.array([[1,1,1],[1,1,1],[1,1,1]],np.float)/9
gaussian_kernel =  cv2.getGaussianKernel(5,0)
#deriv_kernel = cv2.getDerivKernels()
kernels = [identity_kernal, sharpen_kernel,mean_kernel,gaussian_kernel]

color_original = cv2.imread('test.jpg')
#modified = color_original.copy()
gray_original = cv2.cvtColor(color_original,cv2.COLOR_BGR2GRAY)


cv2.namedWindow('app')
cv2.createTrackbar('contrast','app',1,100,dummy)
cv2.createTrackbar('brightness','app',50,100,dummy)
cv2.createTrackbar('filter','app',0,len(kernels)-1,dummy)
cv2.createTrackbar('grayscale','app',0,1,dummy)
count = 1
while True:
    #cv2.imshow('app',modified)
    k = cv2.waitKey(1) & 0xFF
    contrast    =       cv2.getTrackbarPos('contrast','app')
    brightness  =       cv2.getTrackbarPos('brightness','app')
    kernel      =       cv2.getTrackbarPos('filter','app')
    gray        =       cv2.getTrackbarPos('grayscale','app')
    if gray == 0:
        modified = cv2.filter2D(color_original,-1,kernels[kernel])
    else:
        modified = cv2.filter2D(gray_original,-1,kernels[kernel])
    
    modified = cv2.addWeighted(modified,contrast,np.zeros(modified.shape,dtype = modified.dtype),0,brightness-50)
    cv2.imshow('app',modified)
    if k == ord('q'):
        break
    elif k== ord('s'):
        cv2.imwrite('output{}.png'.format(count),modified)
        count+=1
cv2.destroyAllWindows()