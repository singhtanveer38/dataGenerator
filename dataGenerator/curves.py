import numpy as np
import matplotlib.pyplot as plt

class sin(object):

	def __init__(self, amplitude, phase, minValue, maxValue, steps):
		self.amplitude = amplitude
		self.phase = phase
		self.minValue = minValue
		self.maxValue = maxValue
		self.steps = steps
		# self.phaseMultiplier = phaseMultiplier
		# self.phaseOffset = phaseOffset
		# self.valueOffset = valueOffset

	def calculate(self):
		self.x = np.arange(self.minValue, self.maxValue, self.steps)
		self.y = np.sin(self.x*self.phase) + self.amplitude

	def plot(self):
		plt.scatter(self.x, self.y)
		plt.show()





data = sin(amplitude=0, phase=2, minValue=0, maxValue=10, steps=0.1)
data.calculate()
print(data.x)
print(data.y)
data.plot()
