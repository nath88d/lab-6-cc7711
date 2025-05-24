#Girafa
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = './GIRAFA.jpeg'
img_raw = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
max_val = img_gray.max()
limiar = 10 * max_val
_, img_thresh = cv2.threshold(img_gray, limiar, max_val, cv2.THRESH_BINARY_INV)

k_size = 5
element = np.ones((k_size, k_size), np.uint8)
img_thresh_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, element)

img_blurred = cv2.blur(img_gray, ksize=(k_size, k_size))

edge1 = cv2.Canny(image=img_gray, threshold1=0.5 * max_val, threshold2=0.5 * max_val)
edge2 = cv2.Canny(image=img_blurred, threshold1=0.5 * max_val, threshold2=0.5 * max_val)

conts, _ = cv2.findContours(image=img_thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
conts = sorted(conts, key=cv2.contourArea, reverse=True)
img_contorno = img_rgb.copy()
resultado = cv2.drawContours(img_contorno, conts, contourIdx=-1, color=(255, 0, 0), thickness=2)

imgs_resultado = [img_rgb, img_blurred, img_gray, edge1, edge2, img_thresh, img_thresh_open, resultado]
cols = math.ceil(len(imgs_resultado)**0.5)
rows = cols if (cols**2 - len(imgs_resultado)) <= cols else cols - 1

for i in range(len(imgs_resultado)):
    plt.subplot(rows, cols, i + 1)
    plt.imshow(imgs_resultado[i], cmap='gray' if len(imgs_resultado[i].shape) == 2 else None)
    plt.xticks([]), plt.yticks([])
plt.show()
