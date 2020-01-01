import numpy as np
import pygame
pygame.init()
class Screen:
  def __init__(self,scale):
    self.scale = scale
		self.pixels = [pixel(x,y,self.scale) for x in range(25) for y in range(25)]
	def draw(self):
		for pixel in self.pixels:
			pixel.draw()
	def update(self):
		self.loop = True
		while self.loop:
			self.draw()
			if pygame.key.get_pressed()[pygame.K_s]:
				self.loop = False
				self.iden = [[1],[0]]
			elif pygame.key.get_pressed()[pygame.K_s]:
				self.loop = False
				self.iden = [[0],[1]]
		return (np.asarray(np.reshape([x.value for x in self.pixels], (625,1)),np.asarray(self.iden))
	def update_test(self):
		self.loop = True
		while self.loop:
			self.draw()
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.loop = False
		return numpy.asarray([[x.value] for x in self.pixels])
	
class Pixel:
	def __init__(self,x,y,scale):
		self.scale = scale
		self.value = 0.0
		self.rect = (x,y,self.scale,self.scale)
	def draw(self):
		if pygame.mouse.get_pressed()[0] and pygame.Rect(self.rect).collidepoint(pygame.mouse.get_pos()):
			self.value+=20
		pygame.draw.rect(win,(255*self.value,255*self.value,255*self.value),self.rect)
if __name__  = "__main__":
	scale = 4
	win = pygame.display.set_mode((25*scale,25*scale))
	data = np.load("data.npy")
	exit = False
	while not(exit):
		for event in pygame.event.get():
        if event.type == pygame.QUIT:
		exit = True
	data.append(Screen(scale).update())
	np.save("data",data)
	np.save("data",data)
