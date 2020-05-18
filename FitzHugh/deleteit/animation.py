import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from animutils import Animationcls

x = np.arange(0,10,0.1)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([0,10])
ax.set_ylim([-1,1])
ax.plot(x,y)
line, = ax.plot([],[],'ro')

Lines = [line]
Pathes = [(x,y)]
init_data = [(x[0],y[0])]
draw_mode = ['line']

animobj = Animationcls(Lines, Pathes, init_data, fig, draw_mode)

animobj.start_animation()
