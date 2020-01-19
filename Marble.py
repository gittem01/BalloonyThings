import cv2

class Marble:
    def __init__(self, pos, speed=[0, 0], size=30):
        self.pos = pos
        self.speed = speed
        self.size = size

    def move(self, img):
        shapex = img.shape[1]
        shapey = img.shape[0]
        if self.pos[0]+self.size > shapex:
            self.speed[0]*= -1
        elif self.pos[0]-self.size < 0:
            self.speed[0]*=-1

        if self.pos[1]+self.size > shapey:
            self.speed[1]*= -1
        elif self.pos[1]-self.size < 0:
            self.speed[1]*=-1

        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def draw(self, img):
        cv2.circle(img, (round(self.pos[0]), round(self.pos[1])), self.size, (255, 255, 0), -1)
