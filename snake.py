import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

