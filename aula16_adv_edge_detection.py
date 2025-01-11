import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')
cv2.imshow('Original', img)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplaciano = cv2.Laplacian(cinza, cv2.CV_64F)
laplaciano = np.uint8(np.absolute(laplaciano))
cv2.imshow('Laplaciano', laplaciano)

sobelX = cv2.Sobel(cinza, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(cinza, cv2.CV_64F, 0, 1)
cv2.imshow('Sobel X', sobelX)
cv2.imshow('Sobel Y', sobelY)

combined_sobel = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow('Sobel combinado', combined_sobel)

canny = cv2.Canny(img, 150, 175)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
