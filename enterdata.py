import numpy as np
import pygame
pygame.init()
class Screen:
  def __init__(self):
    self.pixels = [pixel(x,y) for x in range(25) for y in range(25)]
 
