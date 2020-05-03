###################################
##  SMART CITIES CHAPTER 7 CODE  ##
###################################
######## HeatMap Generator ########
###################################
# Anil Ozturk # Fidan Khalilbayli #
###################################

from scipy import stats, integrate
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def generate_heatmap(network, mode="nodes"):
            
    coords = []
    line_coords = []

    if mode=="nodes":
        for node in network.nodes:
            for i in range(int(node.size)):
                coords.append([node.x, node.y])
                
    elif mode=="lines":
        for line in network.lines:
            for i in range(int(line.size)):
                cx = (line.start_x + line.end_x) / 2
                cy = (line.start_y + line.end_y) / 2               
                coords.append([cx, cy])
            line_coords.append([line.start_x, line.end_x, line.start_y, line.end_y])
    
    return coords, line_coords


def plot_heatmap(network, mode="nodes"):

    """
    Input:
    - mode: Which kind of graph will it be?
    ; 'nodes','lines' 
    """

    plt.gca().invert_yaxis()

    coords, line_coords = generate_heatmap(network=network, mode=mode)
    x,y = np.array(coords).T
    ax = sns.kdeplot(x, y, cmap="Blues", shade=True, shade_lowest=False, n_levels=100)

    if mode == "nodes":
        ax.scatter(x, y, color='black')

    elif mode == "lines":
        for line in line_coords:
            ax.plot(line[:2], line[2:], color='black')

    ax.set_frame_on(False)
    plt.axis('off')
    plt.show()