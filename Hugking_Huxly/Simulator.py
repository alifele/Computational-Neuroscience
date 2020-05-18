import numpy as np
import matplotlib.pyplot as plt
from Simulator_functions import *
import variables as var
from animutils import Animationcls
from animation_run import run_animation

v = -63
n = 0
m = 0
h = 0
dt = 0.001
t_total = 10
t = np.arange(0, t_total, dt)
I = 1 # nAmp
#I_list = [3*i for i in range(1,100)]
I_list = [20]
spikes_list = []

for I in I_list:
    v_list, n_list, m_list, h_list, N_spikes = experiment_run(v,n,m,h,I,t_total, dt)
    #print(N_spikes)
    spikes_list.append([I, N_spikes])

run_animation(v_list, n_list, m_list, h_list, N_spikes,I,t)
#spikes_list = np.array(spikes_list)
#plt.plot(spikes_list[:,0], spikes_list[:,1])
#plt.plot(v_list)
#plt.xlabel('I $nAmp$')
#plt.ylabel('Number of Spikes')
#plt.show()


#plt.plot(v_list, n_list, label='n_list')
#plt.plot(v_list, m_list, label='m_list')
#plt.plot(v_list, h_list, label='h_list')
