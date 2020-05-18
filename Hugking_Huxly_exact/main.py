import numpy as np
import matplotlib.pyplot as plt
from functions import *
from variables import *
from plotutils import *
from experiments import *


#fig = plt.figure()
#ax = fig.add_subplot(2,1,1)
#n_m_h_plotter(ax)
#ax = fig.add_subplot(2,1,2)
#n_m_h_tau_plotter(ax)
#plt.show()


v_list, n_list, m_list, h_list = v_n_m_h_experiment(t_limits,v0,dt,I)

fig = plt.figure()

v_n_m_h_plotter(v_list, n_list, m_list, h_list,fig)
#print(np.arange(t_limits[0], t_limits[1],dt).shape)
print(v_list[:,0].shape)
plt.show()
