import numpy as np
from functions import *


#f_list = [alpha_n, beta_n, alpha_m, beta_m, alpha_h, beta_h]



E_k = -12
E_na = 120
E_l = 10.6

G_k = 36
G_na = 120
G_l = 0.3
C = 1

t_limits = [0,20]
v0 = -0
dt = 0.01
#I = 20


N_points = (t_limits[1] - t_limits[0])/dt
I = np.zeros(int(N_points)) + 20
#I[int(N_points*3/10):int(N_points*3.5/10)] = 3
#I[int(N_points*6/10):int(N_points*6.2/10)] = 30
#I[int(N_points*7/10):] = 2
