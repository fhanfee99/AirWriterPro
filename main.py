import cv2
import time
from utils.hand_tracker import HandTracker
from utils.gestures import Gestures
from utils.drawing import Drawing

cap = cv2.VideoCapture(0)

tracker = HandTracker()
draw = Drawing()

pTime = 0

prev_x, prev_y = 0, 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img, hands = tracker.find_hands(img)
    img = draw.draw_ui(img)

    if hands:
        lm_list = hands[0]

        x1, y1 = lm_list[8][1], lm_list[8][2]

        fingers = Gestures.fingers_up(lm_list)

        h, w, _ = img.shape
        draw.select_color(x1, y1, w)

        # DRAW
        draw_mode = fingers[1] and not fingers[2]
        draw.draw(x1, y1, draw_mode)

        # PINCH MOVE
        dist = Gestures.distance(lm_list[4][1:], lm_list[8][1:])

        if dist < 40:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x1, y1

            dx = x1 - prev_x
            dy = y1 - prev_y

            draw.move_strokes(dx, dy)

            prev_x, prev_y = x1, y1
        else:
            prev_x, prev_y = 0, 0

        # CLEAR
        if fingers == [1,1,1,1,1]:
            draw.clear()

        # PLASMA
        if fingers == [0,1,1,0,0]:
            img = draw.apply_plasma(img, hands)

        cv2.circle(img, (x1, y1), 10, draw.color, cv2.FILLED)

    img = draw.render(img)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Air Writing PRO", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()