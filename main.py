#!/usr/bin/python3
from math import cos, sin
import math
class Projectile():
    def __init__(self, x, y, vel, ang):
        self.x = x
        self.y = y
        self.vel = vel
        self.ang = ang
        self.g = -9.8
        print(self.get_duration())
        print(self.get_max_height())
        print(self.get_range())
        print(self.get_position_at(self.get_duration()))

    def get_range(self):
        # R = v0 ^ 2 / g * sin(2 * ang)
        rng = self.vel ** 2 / abs(self.g) * sin(2 * self.ang)
        return rng

    def get_max_height(self):
        # H = (v0^2 * sin(ang)) / 2g
        max_height = self.vel ** 2 * sin(self.ang) ** 2 / (2 * abs(self.g))
        return max_height

    def get_duration(self):
        # t = (2v0 * sin(ang)) / g
        duration = abs((2 * self.vel * sin(self.ang)) / self.g)
        return duration

    def get_position_at(self, sec):
        # y = -1/2 * g * t^2 + (v0 * sin(ang)) * t + y0
        return -1/2 * self.g * sec ** 2 + (self.vel * sin(self.ang)) * sec + self.y



if __name__ == "__main__":
    projectile = Projectile(0, 0, 10, 45);
