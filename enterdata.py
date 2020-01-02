import numpy as np
import pygame
skip = False
pygame.init()
class Screen:
	def __init__(self,scale):
		self.scale = scale
		self.pixels = []
		for y in range(25):
			for x in range(25):
				self.pixels.append(Pixel(x,y,self.scale))
	def draw(self):
		for pixel in self.pixels:
			pixel.draw()
	def update(self):
		self.loop = True
		global skip
		skip = False
		while self.loop:
			self.draw()
			if pygame.key.get_pressed()[pygame.K_s]:
				self.loop = False
				self.iden = [[1],[0]]
				print(np.asarray(np.reshape([x.value for x in self.pixels], (625,1))),self.iden)
				return (np.asarray(np.reshape([x.value for x in self.pixels], (625,1))),np.asarray(self.iden))
			if pygame.key.get_pressed()[pygame.K_f]:
				self.loop = False
				self.iden = [[0],[1]]
				print(np.asarray(np.reshape([x.value for x in self.pixels], (625,1))))
				return (np.asarray(np.reshape([x.value for x in self.pixels], (625,1))),np.asarray(self.iden))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.loop = False
					skip = True
		print("skipped")
	def update_test(self):
		self.loop = True
		while self.loop:
			self.draw()
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.loop = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.loop = False
		return numpy.asarray([[x.value] for x in self.pixels])
	
class Pixel:
	def __init__(self,x,y,scale):
		self.scale = scale
		self.value = 0.0
		self.x = x*scale
		self.y = y*scale
		self.rect = (self.x,self.y,self.scale,self.scale)
		self.sq = scale
	def draw(self):
		global win
		if self.clicked():
			self.value=1
		pygame.draw.rect(win,(round((255*self.value)),round(255*self.value),round(255*self.value)),(self.x,self.y,self.sq,self.sq))
	def clicked(self):
		if pygame.mouse.get_pressed()[0] == True and pygame.Rect((self.x,self.y,self.sq,self.sq)).collidepoint(pygame.mouse.get_pos()) == True:
			return True
		else:
			return False
if __name__  == "__main__":
	scale = 25
	win = pygame.display.set_mode((25*scale,25*scale))
	win.fill((5,5,5))
	if not(skip):	
		data = np.load("data.npy")
		np.append(data,Screen(scale).update())
		np.save("data",data)