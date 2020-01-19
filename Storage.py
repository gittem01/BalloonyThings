import cv2
import numpy as np
import random
import math

class Storage:
    def __init__(self, pos, baseSize=100, angle=0, color=(255, 255, 255)):
        self.pos = pos
        self.xSize = baseSize
        self.ySize = baseSize
        self.baseSize = baseSize
        self.angle = angle
        self.color = color
        self.potential = [0, 0]
        self.elasticity = 0.01


    def draw(self, img):
        cv2.ellipse(img, (round(self.pos[0]), round(self.pos[1])), (round(self.xSize), round(self.ySize)),
         self.angle, 0, 360, self.color, -1)

    def data(self, m):
        xDist = m.pos[0]-self.pos[0]
        yDist = m.pos[1]-self.pos[1]
        dist = (xDist**2+yDist**2)**0.5-m.size
        try:
            angle = math.atan(yDist/xDist)
        except ZeroDivisionError:
            angle = math.pi/2
        #print(angle, 1)
        m0 = 1
        if (xDist<0 and yDist<0) or (xDist<0 and yDist>0):
            m0 = -1

        return (dist, angle, m0)

    def update(self, m):
        dist, angle, m0 = self.data(m)
        if dist < self.baseSize:
            value = (self.baseSize/dist)**2
            m.speed[0] += math.cos(angle)*value*self.elasticity*m0
            m.speed[1] += math.sin(angle)*value*self.elasticity*m0
            self.angle = angle*(180/math.pi)
            self.xSize = dist
            self.ySize = self.baseSize+(self.baseSize-dist)
            self.color = (255-255*(1-dist/self.baseSize), 255-255*(1-dist/self.baseSize), 255)
