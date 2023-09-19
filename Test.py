import numpy as np
import cv2
import matplotlib.pyplot as plt
import projUtils as ut

img = cv2.imread("uggla/1.jpg",0);
img2 = cv2.imread("RoughtTest/test_0001_Layer-4.png",0);
img3 = cv2.imread("RoughtTest/test_0002_Layer-2.png",0)
img = cv2.resize(img,[200,500])
print(len(ut.create_gaussian_pyramid(img,3)))
print(len(ut.create_laplacian_pyramid(ut.create_gaussian_pyramid(img,3))))
laplace,gaus = ut.create_laplacian_pyramide(img)
# test_pyramide2 = ut.create_laplacian_pyramide(img2)
# test_pyramide3 = ut.create_laplacian_pyramide(img3)


# cv2.imshow("test",test_pyramide[0]);
# cv2.waitKey(0);
i = 0

for obj in laplace:

    cv2.imwrite("{}bild1.jpg".format(i),obj)
    i = i+1
# ut.display_pyramid(gaus)
ut.reconstructTeset(laplace,gaus)

# i = 0
# for obj in test_pyramide2:

#     cv2.imwrite("{}bild2.jpg".format(i),obj)
#     i = i+1

# i = 0
# for obj in test_pyramide3:

#     cv2.imwrite("{}bild3.jpg".format(i),obj)
#     i = i+1
    
