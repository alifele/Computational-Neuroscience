import numpy as np
import matplotlib.pyplot as plt
from functions import *
from variables import *
from plotutils import *


def v_n_m_h_experiment(t_limits,v0,dt,I):

    v_list = []
    n_list = []
    m_list = []
    h_list = []

    t_total = t_limits[1] - t_limits[0]

    v = v0
    t = t_limits[0]
    #v_list.append([t,v])

    for _ in range(int(t_total/dt)):

        n_val = n_f(v,t)
        m_val = m_f(v,t)
        h_val = h_f(v,t)
        v_dot_val = v_dot(v,n_val,m_val,h_val,I[_])
        v = updater(v,v_dot_val)

        v_list.append([t,v])
        m_list.append([t,m_val])
        n_list.append([t,n_val])
        h_list.append([t,h_val])

        t += dt


    return np.array(v_list), np.array(n_list), np.array(m_list), np.array(h_list)
