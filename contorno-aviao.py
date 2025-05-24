import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

caminho_img = './Aviao.jpeg'
imagem_base = cv2.imread(caminho_img)
imagem_rgb = cv2.cvtColor(imagem_base, cv2.COLOR_BGR2RGB)

imagem_gray = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2GRAY)
valor_max = imagem_gray.max()
limiar_bin = int(valor_max * 0.35)
_, imagem_thresh = cv2.threshold(imagem_gray, limiar_bin, valor_max, cv2.THRESH_BINARY_INV)

tam_kernel = 5
elemento = np.ones((tam_kernel, tam_kernel), np.uint8)

img_close = cv2.morphologyEx(imagem_thresh, cv2.MORPH_CLOSE, elemento, iterations=1)
img_dilatada = cv2.dilate(img_close, elemento, iterations=2)
img_aberta = cv2.morphologyEx(img_dilatada, cv2.MORPH_OPEN, elemento, iterations=1)
imagem_thresh_proc = img_aberta

imagem_suave = cv2.blur(imagem_gray, ksize=(tam_kernel, tam_kernel))

borda1 = cv2.Canny(imagem_gray, threshold1=0.45 * valor_max, threshold2=0.45 * valor_max)
borda2 = cv2.Canny(imagem_suave, threshold1=0.45 * valor_max, threshold2=0.45 * valor_max)

contornos, _ = cv2.findContours(imagem_thresh_proc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contornos_filtrados = []
for contorno in contornos:
    ar = cv2.contourArea(contorno)
    if 3000 < ar < 120000:
        contornos_filtrados.append(contorno)

imagem_final = imagem_rgb.copy()
cv2.drawContours(imagem_final, contornos_filtrados, -1, (255, 0, 0), 2)

imagens_finais = [imagem_rgb, imagem_suave, imagem_gray, borda1, borda2, imagem_thresh, imagem_thresh_proc, imagem_final]
colunas = math.ceil(len(imagens_finais) ** 0.5)
linhas = colunas if (colunas ** 2 - len(imagens_finais)) <= colunas else colunas - 1

for i in range(len(imagens_finais)):
    plt.subplot(linhas, colunas, i + 1)
    plt.imshow(imagens_finais[i], cmap='gray' if len(imagens_finais[i].shape) == 2 else None)
    plt.xticks([]), plt.yticks([])
plt.show()
