import cv2
import numpy as np

img = cv2.imread('assets/fotos/cats.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
reactangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

recorte1 = cv2.bitwise_and(circle, reactangle)
recorte2 = cv2.bitwise_or(circle, reactangle)
recorte3 = cv2.bitwise_xor(circle, reactangle)
recorte4 = cv2.bitwise_not(circle)

mask1 = cv2.bitwise_and(img, img, mask=recorte1)
mask2 = cv2.bitwise_and(img, img, mask=recorte2)
mask3 = cv2.bitwise_and(img, img, mask=recorte3)
mask4 = cv2.bitwise_and(img, img, mask=recorte4)

cv2.imshow('Original', img)
cv2.imshow('Recorte 1', recorte1)
cv2.imshow('Recorte 2', recorte2)
cv2.imshow('Recorte 3', recorte3)
cv2.imshow('Recorte 4', recorte4)

cv2.imshow('Mask 1', mask1)
cv2.imshow('Mask 2', mask2)
cv2.imshow('Mask 3', mask3)
cv2.imshow('Mask 4', mask4)

cv2.waitKey(0)