import cv2
import numpy as np

cap = cv2.VideoCapture('assets/videos/dog.mp4')

def rescale_frame(frame: np.array, scale: float = 0.75) -> np.array:
  largura = int(frame.shape[1] * scale)
  altura = int(frame.shape[0] * scale)
  dimensoes = (largura, altura)

  return cv2.resize(frame, dimensoes, interpolation=cv2.INTER_AREA)

def resize_frame(width: int, height: int) -> None:
  cap.set(3, width)
  cap.set(4, height)

img = cv2.imread('assets/fotos/cat_large.jpg')
cv2.imshow('cat', img)

img_resized = rescale_frame(img, 0.2)
cv2.imshow('resized_cat', img_resized)
cv2.waitKey(0)

while True:
  ret, frame = cap.read()

  frame_resized = rescale_frame(frame, 0.5)

  cv2.imshow('video', frame_resized)
  if cv2.waitKey(20) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()