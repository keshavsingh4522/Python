'''
author: ddalgi29
desc: particle swarm optimisation visualisation using pyswarms and matplotlib
'''

#modules
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image
from numpy.core.fromnumeric import mean

#pyswarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher
from pyswarms.utils.plotters.formatters import Designer

m = Mesher(func=fx.sphere)
d = Designer(limits=[(-1,1),(-1,1),(-0.1,1)], label = ['x-axis', 'y-axis', 'z-axis'])
options = {'c1':0.5, 'c2':0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=2, options=options)
cost, pos = optimizer.optimize(fx.sphere, iters=100)

pos_history_3d = m.compute_history_3d(optimizer.pos_history)

animation3d = plot_surface(pos_history=pos_history_3d, mesher=m, designer=d, mark=(0,0,0))
plt.show()


