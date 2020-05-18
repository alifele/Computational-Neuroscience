import numpy as np
import matplotlib.pyplot as plt
from functions import *
from variables import *


def n_m_h_plotter(ax):
    ax.plot(v, n_inf(v), label='n_inf')
    ax.plot(v, m_inf(v), label='m_inf')
    ax.plot(v, h_inf(v), label='h_inf')
    ax.legend(loc=6)


def n_m_h_tau_plotter(ax):
    ax.plot(v, tau_n(v), label='n_tau')
    ax.plot(v, tau_m(v), label='m_tau')
    ax.plot(v, tau_h(v), label='h_tau')
    ax.legend(loc=1)

def v_n_m_h_plotter(v_list, n_list, m_list, h_list,fig):
    ax = fig.add_subplot(5,1,1)
    ax.plot(v_list[:,0], v_list[:,1], label='v')
    ax.set_xticks([])
    ax = fig.add_subplot(5,1,2)
    ax.plot(n_list[:,0], n_list[:,1],'g', label='n')
    ax.set_xticks([])
    ax = fig.add_subplot(5,1,3)
    ax.plot(m_list[:,0], m_list[:,1],'orange', label='m')
    ax.set_xticks([])
    ax = fig.add_subplot(5,1,4)
    ax.plot(h_list[:,0], h_list[:,1],'r', label='h')
    ax.set_xticks([])
    ax = fig.add_subplot(5,1,5)
    ax.plot(h_list[:,0], I,'r', label='h')

    fig.legend()
