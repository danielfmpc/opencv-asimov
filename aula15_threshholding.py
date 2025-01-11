import cv2
import numpy as np

img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

'''
Para os threshs simples usaremos a função cv2.threshold()
cv2.threshold(image, valor_thresh, maxval, metodo_do_thresh)
'''

threshold, thresh = cv2.threshold(gray, 129, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh simples', thresh)

threshold, thresh = cv2.threshold(gray, 129, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh simples invertido', thresh)

adap_g_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Thresh adaptativo', adap_g_thresh)
adap_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

cv2.waitKey(0)