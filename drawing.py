import cv2
import numpy as np

class Drawing:

    def __init__(self):
        self.color = (255, 0, 255)

        self.colors = [(255,0,0), (0,255,0), (0,0,255), (0,255,255)]

        # stroke system
        self.strokes = []
        self.current_stroke = []

    def draw_ui(self, img):
        h, w, _ = img.shape

        overlay = img.copy()
        cv2.rectangle(overlay, (w-100, 0), (w, h), (20,20,20), -1)
        img = cv2.addWeighted(overlay, 0.6, img, 0.4, 0)

        for i, col in enumerate(self.colors):
            cy = 120 + i*100
            cx = w - 50
            cv2.circle(img, (cx, cy), 25, col, -1)

        return img

    def select_color(self, x, y, w):
        if x > w - 100:
            for i, col in enumerate(self.colors):
                if 100 + i*100 < y < 140 + i*100:
                    self.color = col

    # DRAW (store strokes)
    def draw(self, x1, y1, draw_mode):
        if draw_mode:
            self.current_stroke.append((x1, y1))
        else:
            if self.current_stroke:
                self.strokes.append(self.current_stroke)
                self.current_stroke = []

    # RENDER ALL
    def render(self, img):
        for stroke in self.strokes:
            for i in range(1, len(stroke)):
                cv2.line(img, stroke[i-1], stroke[i], self.color, 6)

        for i in range(1, len(self.current_stroke)):
            cv2.line(img,
                     self.current_stroke[i-1],
                     self.current_stroke[i],
                     self.color, 6)

        return img

    # MOVE (REAL DRAG)
    def move_strokes(self, dx, dy):
        new_strokes = []

        for stroke in self.strokes:
            new_stroke = []
            for (x, y) in stroke:
                new_stroke.append((x + dx, y + dy))
            new_strokes.append(new_stroke)

        self.strokes = new_strokes
        self.current_stroke = [(x+dx, y+dy) for (x,y) in self.current_stroke]

    def clear(self):
        self.strokes = []
        self.current_stroke = []

    # PLASMA EFFECT
    def apply_plasma(self, img, hands):
        import numpy as np

        all_points = []

        # collect all finger tips from all hands
        tips = [4, 8, 12, 16, 20]

        for lm_list in hands:
            for t in tips:
                x, y = lm_list[t][1], lm_list[t][2]
                all_points.append((x, y))

                # glow
                for i in range(5):
                    radius = 10 + i*6
                    alpha = 0.6 - i*0.1

                    overlay = img.copy()
                    cv2.circle(overlay, (x, y), radius, (0,255,255), 2)
                    img = cv2.addWeighted(overlay, alpha, img, 1-alpha, 0)

                # sparks
                for _ in range(5):
                    dx = np.random.randint(-25,25)
                    dy = np.random.randint(-25,25)
                    cv2.line(img, (x,y), (x+dx,y+dy), (0,255,255), 1)

        # ⚡ CONNECT ALL POINTS (REAL ELECTRIC WEB)
        for i in range(len(all_points)):
            for j in range(i+1, len(all_points)):

                x1, y1 = all_points[i]
                x2, y2 = all_points[j]

                # zig-zag lightning
                for _ in range(2):
                    mx = (x1 + x2)//2 + np.random.randint(-30,30)
                    my = (y1 + y2)//2 + np.random.randint(-30,30)

                    cv2.line(img, (x1,y1), (mx,my), (0,255,255), 1)
                    cv2.line(img, (mx,my), (x2,y2), (0,255,255), 1)

        return img