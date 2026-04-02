import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        all_hands = []

        if results.multi_hand_landmarks:
            h, w, _ = img.shape

            for handLms in results.multi_hand_landmarks:
                lm_list = []

                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append((id, cx, cy))

                all_hands.append(lm_list)

                self.mp_draw.draw_landmarks(
                    img, handLms, self.mp_hands.HAND_CONNECTIONS
                )

        return img, all_hands