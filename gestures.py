import math

class Gestures:

    @staticmethod
    def fingers_up(lm_list):
        fingers = []

        fingers.append(lm_list[4][1] > lm_list[3][1])

        tips = [8, 12, 16, 20]
        for tip in tips:
            fingers.append(lm_list[tip][2] < lm_list[tip - 2][2])

        return fingers

    @staticmethod
    def distance(p1, p2):
        return math.hypot(p2[0]-p1[0], p2[1]-p1[1])