import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
def create_laplacian_pyramide(img):
    gaussian = []
    gaussian_layer = img.copy()
    # gaussian.append(gaussian_layer)
    k = 3 #number of layers of the pyramid
    for i in range(k):
        gaussian_layer = cv2.pyrDown(gaussian_layer)
        gaussian.append(gaussian_layer)
        # cv2.imshow('Gaussian Layer -{}'.format(i),gaussian_layer)
        resizedGas = gaussian_layer
        # print(i)
        # for j in range(i):
        #     resizedGas = expand(resizedGas)
        # cv2.imwrite("_gaussian{}.jpg".format(i), resizedGas)
       
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(len(gaussian))

    laplacian =  []
    for i in range(len(gaussian)-1,0,-1):
       # print(i)
        size = (gaussian[i - 1].shape[1], gaussian[i - 1].shape[0])
        gaussian_expanded = cv2.pyrUp(gaussian[i], dstsize=size)
        laplacian_layer = cv2.subtract(gaussian[i-1], gaussian_expanded)
        laplacian.append(laplacian_layer)
        
    return [laplacian,gaussian]

def expand(img):
    width = int(img.shape[1] * 2)
    height = int(img.shape[0] * 2)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_LANCZOS4)
def reduce(img):
    width = int(img.shape[1] / 2)
    height = int(img.shape[0] / 2)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_LANCZOS4)

def create_gaussian_pyramid(img,levels):
    gaussian = []
    gaussian_layer = img.copy()
    gaussian.append(gaussian_layer) #base of the pyramid should be the original image
    
    for i in range(levels):
        print
        gaussian_layer = reduce(gaussian_layer) #further smoothing should be incorporated but pyrdown is good for now
        gaussian.append(gaussian_layer)
        print(gaussian_layer.shape[1],gaussian_layer.shape[0])
       
        resizedGas = gaussian_layer

    
    ##testing section to see the different levels of the pyramid  
    j = 0  
    for g in gaussian:
        cv2.imwrite("_gaussian{}.jpg".format(j), g) 
        j=j+1

    return gaussian

def create_laplacian_pyramid(gaussianPyramid):
    laplace = []
    
    for i in range(0,len(gaussianPyramid)-1,1):
        
        # The concept of divisions is somewhat troublesome... 
        layer = cv2.subtract(gaussianPyramid[i],sameShape(gaussianPyramid[i],expand(gaussianPyramid[i+1])))
        laplace.append(layer)
    j = 0 

    ##testing section to see the different levels of the pyramid  
    for l in laplace:
        cv2.imwrite("_laplace{}.jpg".format(j), l) 
        j=j+1
    return laplace

def sameShape(img1,img2):
    print("shape 1" + str(img1.shape))
    print("shape 2" + str(img2.shape))
    img2 = cv2.resize(img2,[img1.shape[1],img1.shape[0]])
    
    print("shape 1" + str(img1.shape))
    print("shape 2" + str(img2.shape))

def reconstructTeset(lap,gas):
    # for g in gas
    top = gas[len(gas)-1] #this is the top of the gaussian pyramid 
    currentGas = top
    for layer in lap:
        currentGas = expand(currentGas)-layer
    print(currentGas.shape[1])
    cv2.imshow("reconstructed",currentGas)
    cv2.waitKey(0)
        
    # for l in lap:
    #     cv2.imshow("test",l)
    #     cv2.waitKey(0)


for i in range(0):
    print(i)