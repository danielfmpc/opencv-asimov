import cv2

# Ler video
video = cv2.VideoCapture('assets/videos/dog.mp4')

while True:
  _, frame = video.read()

  cv2.imshow('Video', frame)

  if cv2.waitKey(20) & 0xFF == ord('q'):
    break

video.release()
cv2.destroyAllWindows()
