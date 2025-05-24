import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_satelite_path = './Satelite.jpeg'
raw_img = cv2.imread(img_satelite_path)
rgb_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)

gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
max_intensity = gray_img.max()
limiar_calc = int((max_intensity * 40) * 0.35)
_, bw_img = cv2.threshold(gray_img, limiar_calc, max_intensity, cv2.THRESH_BINARY_INV)

k_val = 5
kernel_s = np.ones((k_val, k_val), np.uint8)
bw_open = cv2.morphologyEx(bw_img, cv2.MORPH_OPEN, kernel_s)

blurred_img = cv2.blur(gray_img, ksize=(k_val, k_val))

canny_orig = cv2.Canny(gray_img, threshold1=0.45 * max_intensity, threshold2=0.45 * max_intensity)
canny_blur = cv2.Canny(blurred_img, threshold1=0.45 * max_intensity, threshold2=0.45 * max_intensity)

contours_detected, _ = cv2.findContours(bw_open, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_valid = []
for c in contours_detected:
    area_c = cv2.contourArea(c)
    if 800 < area_c < 18000:
        contour_valid.append(c)

final_img = rgb_img.copy()
cv2.drawContours(final_img, contour_valid, -1, (255, 0, 0), 2)

imgs_plot = [rgb_img, blurred_img, gray_img, canny_orig, canny_blur, bw_img, bw_open, final_img]
ncols = math.ceil(len(imgs_plot)**0.5)
nrows = ncols if (ncols**2 - len(imgs_plot)) <= ncols else ncols - 1

for i in range(len(imgs_plot)):
    plt.subplot(nrows, ncols, i + 1)
    plt.imshow(imgs_plot[i], cmap='gray' if len(imgs_plot[i].shape) == 2 else None)
    plt.xticks([]), plt.yticks([])
plt.show()
