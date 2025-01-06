import cv2
import numpy as np

blank = np.zeros([800,800], dtype='uint8')
cv2.imshow('Blank', blank)

reactangle = cv2.rectangle(blank.copy(), (30,30), (770,770), 255, -1)
circle = cv2.circle(blank.copy(), (400,400), 400, 255, -1)
cv2.imshow('Rectangle', reactangle)
cv2.imshow('Circle', circle)

# Bitwise AND --> Intersection of two images
bitwise_and = cv2.bitwise_and(reactangle, circle)
cv2.imshow('AND', bitwise_and)

# Bitwise OR --> Union of two images
bitwise_or = cv2.bitwise_or(reactangle, circle)
cv2.imshow('OR', bitwise_or)

# Bitwise XOR --> Difference of the two images
bitwise_xor = cv2.bitwise_xor(reactangle, circle)
cv2.imshow('XOR', bitwise_xor)

# Bitwise NOT --> Invert the binary color
bitwise_not = cv2.bitwise_not(reactangle, circle)
cv2.imshow('NOT', bitwise_not)


cv2.waitKey(0)