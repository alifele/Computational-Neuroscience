import numpy as np
from variables import *

def alpha_n (v):
    result = 0.01 * (10-v)/(np.exp((10-v)/10) - 1)
    return result

def beta_n (v):
    result = 0.125*np.exp(-v/80)
    return result


def alpha_m(v):
    result = 0.1 * (25-v)/(np.exp((25-v)/10) -1)
    return result

def beta_m(v):
    result = 4*np.exp(-v/18)
    return result

def alpha_h(v):
    result = 0.07*np.exp(-v/20)
    return result

def beta_h(v):
    result = 1/(np.exp((30-v)/10)+1)
    return result



def n_inf(v):
    result = alpha_n(v) / (alpha_n(v) + beta_n(v))
    return result

def m_inf(v):
    result = alpha_m(v) / (alpha_m(v) + beta_m(v))
    return result

def h_inf(v):
    result = alpha_h(v) / (alpha_h(v) + beta_h(v))
    return result


def tau_n(v):
    result = 1 / (alpha_n(v) + beta_n(v))
    return result

def tau_m(v):
    result = 1 / (alpha_m(v) + beta_m(v))
    return result

def tau_h(v):
    result = 1 / (alpha_h(v) + beta_h(v))
    return result


def v_dot(v,n,m,h,I):
    result = I - G_k*n**4*(v-E_k) - G_na*m**3 *h*(v-E_na) - G_l*(v-E_l)
    result /= C
    return result

def updater(v,v_dot_val):
    return v + v_dot_val*dt



def n_f(v,t):
    n_0 = 0.4
    n_inf_ = n_inf(v)
    tau_n_ = tau_n(v)
    result = n_inf_ - (n_inf_ - n_0) * np.exp(-t/tau_n_)
    return result

def m_f(v,t):
    m_0 = 0
    m_inf_ = m_inf(v)
    tau_m_ = tau_m(v)
    result = m_inf_ - (m_inf_ - m_0) * np.exp(-t/tau_m_)
    return result

def h_f(v,t):
    h_0 = 0.6
    h_inf_ = h_inf(v)
    tau_h_ = tau_h(v)
    result = h_inf_ - (h_inf_ - h_0) * np.exp(-t/tau_h_)
    return result
