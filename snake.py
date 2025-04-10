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

class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

def draw_grid(surface, rows, width):
    pass

def redraw_window(surface, snake, snack, score):
    pass

def random_snack(rows, item):
    pass

def message_box(subject, content):
    pass

def main():
    pass