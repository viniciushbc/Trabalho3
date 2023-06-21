import cv2  # Importa a biblioteca cv2, que nos permite trabalhar com imagens
import numpy as np  # Importa a biblioteca numpy, que nos permite fazer cálculos com números
img = cv2.imread('j.png', 0) # O codigo lê a imagem 'j.png' em escala de cinza
img_opening = cv2.imread('j_ruido.png', 0) # O código lê a imagem 'j_ruido.png' em escala de cinza
img_closing = cv2.imread('j_furos.png', 0) # O código lê a imagem 'j_furos.png' também em escala de cinza
altura, largura = img.shape # Obtém a altura e largura da imagem 'img'
kernel = np.ones((5, 5), np.uint8) # Cria uma matriz 5x5 preenchida com números um
print(kernel) # Imprime a matriz
