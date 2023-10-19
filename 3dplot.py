import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def f(x, y):
	return x ** 1/3 * y ** 1/3
	
def Charles():
	ax = plt.axes(projection='3d')
	x, y = np.linspace(-10, 10, 200), np.linspace(-10, 10, 200)
	x, y = np.meshgrid(x, y)
	z = f(x, y)
	ax.set_title("Charles Truscott Watters")
	ax.plot_surface(x, y, z, cmap='rainbow')
	plt.show()
Charles()