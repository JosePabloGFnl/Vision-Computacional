# -*- coding: utf-8 -*-
"""filtros.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QfdIVM5nBqIZm3IrPMDDCpRJGoBwvlF-
"""

#Importamos las librerias
import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

#Leemos la imagen
img = cv2.imread('claseruido.jpg')


#Filtros paso bajo

#Creamos los kernels para colvolucionar nuestra imagen
kernel3x3=np.ones((3,3),np.float32)/9.0
kernel5x5=np.ones((5,5),np.float32)/25.0
kernel7x7=np.ones((5,5),np.float32)/49.0

# Matriz 3 x 3
# [1,1,1]
# [1,1,1]
# [1,1,1]   Un total de 9 elementos

#Intrucción Crear una variable kernel7x7 para aplicar un filtro paso bajo


#Aplicamos los filtros

salida3 = cv2.filter2D(img,-1,kernel3x3)
salida5 = cv2.filter2D(img,-1,kernel5x5)
salida7 = cv2.filter2D(img,-1,kernel7x7)

#Intrucción: Aplicar el filtro a un kernel de 7x7 y guardarlo en una variable llamada salida7



#Otros filtros

#filtro gaussiano
filtrogaussiano = cv2.GaussianBlur(img,(5,5),0)

#filtro mediana
filtromediana = cv2.medianBlur(img,5)

#Filtro blur
blur = cv2.blur(img,(7,7))


print("\nOriginal")
cv2_imshow(img)
print("Filtros paso Bajo")
print("\nKernel 3x3")
cv2_imshow(salida3)
print("\nKernel 5x5")
cv2_imshow(salida5)
print("\nKernel 7x7")
cv2_imshow(salida7)

print("Filtro Gaussiano")
cv2_imshow(filtrogaussiano)

print("\nFiltro mediana")
cv2_imshow(filtromediana)

print("\nFiltro Blur")
cv2_imshow(blur)

print("\n\n")
#Intrucción Imprimir la imagen con el filtro utilizando un kernel de 7x7


#Binorización por umbral

#Leemos la imagen en blanco y negro
img = cv2.imread('claseruido.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

titles = ['Original Image B/W','BINARY','BINARY_INV']
images = [img, thresh1, thresh2]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)

