import numpy as np

class sin(object):

	def __init__(self, val):
		self.val = val

	def calculate(self):
		return np.sin(self.val)