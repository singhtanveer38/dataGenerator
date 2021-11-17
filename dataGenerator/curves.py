import numpy as np
import matplotlib.pyplot as plt

class sin(object):

	def __init__(self, amplitude, wavelength, phase, offset, minValue, maxValue, steps):
		self.amplitude = amplitude
		self.wavelength = wavelength
		self.phase = phase
		self.offset = offset
		self.minValue = minValue
		self.maxValue = maxValue
		self.steps = steps
		# self.phaseMultiplier = phaseMultiplier
		# self.phaseOffset = phaseOffset
		# self.valueOffset = valueOffset

	def calculate(self):
		self.x = np.arange(self.minValue, self.maxValue, self.steps)
		self.y = self.amplitude * np.sin((2*np.pi*self.x)/self.wavelength + self.phase) + self.offset

	def plot(self, size, color):
		plt.scatter(self.x, self.y, s=size, c=color)
		plt.show()


data = sin(amplitude=1, wavelength=4, phase=0, offset=0, minValue=0, maxValue=10, steps=0.1)
data.calculate()
print(data.x)
print(data.y)

data.plot(size=5, color="r")