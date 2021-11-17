import numpy as np
import matplotlib.pyplot as plt

class sin(object):

	def __init__(self, amplitude=1, wavelength=4, phase=0, offset=0, minValue=0, maxValue=10, steps=0.1, noise=False, noise_factor=0.1):
		
		self.amplitude = amplitude
		self.wavelength = wavelength
		self.phase = phase
		self.offset = offset
		self.minValue = minValue
		self.maxValue = maxValue
		self.steps = steps
		self.noise = noise
		self.noise_factor = noise_factor

	def calculate(self):

		self.x = np.arange(self.minValue, self.maxValue, self.steps)

		if self.noise == True:
			self.noisySignal = np.random.normal(0,self.noise_factor,self.x.shape)
			self.y = self.amplitude * np.sin((2*np.pi*self.x)/self.wavelength + self.phase) + self.offset + self.noisySignal

		else:
			self.y = self.amplitude * np.sin((2*np.pi*self.x)/self.wavelength + self.phase) + self.offset

	def plot(self, size=5, color="r"):
		plt.scatter(self.x, self.y, s=size, c=color)
		plt.show()