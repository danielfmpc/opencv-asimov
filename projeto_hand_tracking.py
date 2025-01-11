import cv2
import numpy as np
import mediapipe as mp
import time
from typing import Union

class Dector:
  def __init__(self,
              mode: bool = False,
              number_hands: int = 2,
              model_complexity: int = 1,
              min_detect_confidence: float = 0.5,
              min_tracking_confidence: float = 0.5):
    self.mode = mode
    self.number_hands = number_hands
    self.model_complexity = model_complexity
    self.min_detect_confidence = min_detect_confidence
    self.min_tracking_confidence = min_tracking_confidence

    self.mp_hands = mp.solutions.hands
    self.hands = self.mp_hands.Hands(
      self.mode, 
      self.number_hands, 
      self.model_complexity,
      self.min_detect_confidence, 
      self.min_tracking_confidence
    )
    self.tips_ids = [4, 8, 12, 16, 20]
    self.mp_draw = mp.solutions.drawing_utils
    pass
  
  def find_hands(self, img, draw: bool=True):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    self.results = self.hands.process(img_rgb)

    print(self.results.multi_hand_landmarks)

    if self.results.multi_hand_landmarks and draw:
      for hand in self.results.multi_hand_landmarks:
        self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
    
    return img

  def find_position(self, img, hand_number: int = 0):
    self.required_landmark_list = []

    if self.results.multi_hand_landmarks:
      print(len(self.results.multi_hand_landmarks[hand_number].h))
      my_hand = self.results.multi_hand_landmarks[hand_number]

      h, w, _ = img.shape
      for id, lm in enumerate(my_hand.landmark):
        center_x, center_y = int(lm.x * w), int(lm.y * h)
        self.required_landmark_list.append([id, center_x, center_y])

    return self.required_landmark_list

if __name__ == "__main__":
  detector = Dector()

  cap = cv2.VideoCapture(0)

  previous_time = 0
  current_time = 0
  
  while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.find_hands(img)

    print(detector.hands)

    landmark_list_0 = detector.find_position(img)
    if landmark_list_0:
      cv2.putText(img, "dedo indicador", (landmark_list_0[8][1],landmark_list_0[8][2]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
      cv2.line(img, (landmark_list_0[8][1],landmark_list_0[8][2]), (landmark_list_0[8][1], landmark_list_0[8][2]), (255, 0, 255), 3)

    # landmark_list_1 = detector.find_position(img, 1)
    # if landmark_list_1:
    #   print(landmark_list_1[8])
    #   print(landmark_list_1[8][1:])
    #   cv2.putText(img, "dedo indicador", (landmark_list_1[8][1],landmark_list_1[8][2]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
    #   cv2.line(img, (landmark_list_1[8][1],landmark_list_1[8][2]), (landmark_list_1[8][1], landmark_list_1[8][2]), (255, 0, 255), 3)

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)


    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
