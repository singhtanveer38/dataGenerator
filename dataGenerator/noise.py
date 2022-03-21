import numpy as np
import matplotlib.pyplot as plt

class noise1D(object):

	def __init__(self, mean=0, std=1, size=100):
		
		self.mean = mean
		self.std = std
		self.size = size


	def calculate(self):

		self.x = np.random.normal(loc=self.mean, scale=self.std, size=self.size)

	def plot(self, color="r", linewidth=2):

		plt.plot(self.x, c=color, linewidth=linewidth)
		plt.show()

	def save(self, filename):

		pd.DataFrame({"x":self.x}).to_csv(filename, index=None)

noise = noise1D()
noise.calculate()

print(noise.x)