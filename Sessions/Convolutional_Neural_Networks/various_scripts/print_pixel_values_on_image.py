import numpy as np
import matplotlib.pyplot as plt
import cv2

show_image = True
show_pixel_values = True


gray_img = cv2.imread('profile_picture.png', cv2.IMREAD_GRAYSCALE)

img_size = gray_img.shape

figure = plt.figure(num=None, figsize=(28,21), dpi=80, facecolor='w', edgecolor='k')

alpha = 1

if not show_image:
    alpha = 0

plt.imshow(gray_img, cmap='gray', alpha=alpha)
#
# #
if show_pixel_values:
    for y in range(img_size[0]):
        for x in range(img_size[1]):
            pixel_value = gray_img[y][x]
            plt.text(x, y, str(pixel_value), fontsize=20, horizontalalignment='center', verticalalignment='center')

if show_image:
    saved_img_name = 'profile_picture_pixel_values_on_image.png'
else:
    saved_img_name = 'profile_picture_pixel_values.png'


# plt.show()
plt.savefig(saved_img_name, dpi=figure.dpi)

