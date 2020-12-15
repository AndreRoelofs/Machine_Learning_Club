import numpy as np
import matplotlib.pyplot as plt
import cv2

show_image = False
show_pixel_values = True

gray_img = cv2.imread('profile_picture.png', cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Sobel(gray_img,cv2.CV_64F, 1, 0, ksize=3)

img_size = gray_img.shape

figure = plt.figure(num=None, figsize=(28,21), dpi=80, facecolor='w', edgecolor='k')

alpha = 1

if not show_image:
    alpha = 0

plt.imshow(laplacian, cmap='gray', alpha=alpha)
#
# #

if show_pixel_values:
    for y in range(img_size[0]):
        for x in range(img_size[1]):
            pixel_value = laplacian[y][x]
            plt.text(x, y, str(pixel_value), fontsize=12, horizontalalignment='center', verticalalignment='center')


# plt.show()
plt.savefig("profile_image_extracted_edges.png", dpi=figure.dpi)

