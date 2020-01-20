import numpy as np
import pygame
import gzip as gz
import pickle
if __name__ == "__main__":
	scale = 25
	win = pygame.display.set_mode((25*scale,25*scale))
class Screen:
	def __init__(self,scale):
		self.scale = scale
		self.pixels = []
		for y in range(25):
			for x in range(25):
				self.pixels.append(Pixel(x,y,self.scale))
	def draw(self,window):
		global win
		for pixel in self.pixels:
			pixel.draw(window)
	def update(self):
		self.loop = True
		global win
		global go
		global skip
		skip = False
		while self.loop:
			self.draw(win)
			if pygame.key.get_pressed()[pygame.K_s]:
				self.loop = False
				self.iden = [[1],[0]]
				return (np.asarray(np.reshape([x.value for x in self.pixels], (625,1))),np.asarray(self.iden))
			if pygame.key.get_pressed()[pygame.K_f]:
				self.loop = False
				self.iden = [[0],[1]]
				return (np.asarray(np.reshape([x.value for x in self.pixels], (625,1))),np.asarray(self.iden))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.loop = False
					skip = True
					go = False
	def update_test(self,window):
		self.loop = True
		while self.loop:
			self.draw(window)
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				self.loop = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.loop = False
		pygame.quit()
		return np.asarray([[x.value] for x in self.pixels])


class Pixel:
	def __init__(self,x,y,scale):
		self.scale = scale
		self.value = 0.0
		self.x = x*scale
		self.y = y*scale
		self.rect = (self.x,self.y,self.scale,self.scale)
		self.sq = scale
	def draw(self,window):
		global win
		if self.clicked():
			self.value+=.17
			if self.value>1:
				self.value = 1
			pygame.draw.rect(window,(round(255*self.value),round(255*self.value),round(255*self.value)),self.rect)
			pygame.display.update()
	def clicked(self):
		if pygame.mouse.get_pressed()[0] == True and self.value< 1 and pygame.Rect((self.x,self.y,self.sq,self.sq)).collidepoint(pygame.mouse.get_pos()) == True:
			#print("clicked",pygame.mouse.get_pos())
			return True
		else:
			return False
if __name__  == "__main__":
	skipi = False
	skip = False
	go = True
	if not(skipi):
		while go:
			pygame.init()
			win = pygame.display.set_mode((25*scale,25*scale))
			win.fill((0,0,0))
			f=open("data/data.data","rb")
			data = pickle.load(f)
			f.close()
			print(len(data))
			data.append(Screen(scale).update())
			if skip == False:
				f=open("data/data.data","wb")
				pickle.dump(data,f)
				f.close()
				pygame.quit()
