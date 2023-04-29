import matplotlib.pyplot as plt
import numpy as np
from helper import f

"""
GRAPHING
"""

#graph("2*x", "3*x")
def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    """
    Graphs any number of 2D functions given a string function of x equating to y. The first 4 keyword arguments change the axis of the graph.
    """
    i = 0
    x = np.linspace(lrangex, urangex, graph_points)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    while i < len(args):
        if type(eval(args[i])) == np.ndarray:
            y = eval(args[i])
            plt.plot(x,y, "-b", label=args)
            i+=1
    plt.title(graph_title)
    plt.xlabel(xtitle,fontsize=20)
    plt.ylabel(ytitle,fontsize=20)
    plt.autoscale(enable=scaling)
    plt.grid(gridset)
    if lrangex or urangex != False:
        plt.xlim([lrangex,urangex])
        if lrangey or urangey != False:
            plt.ylim([lrangey,urangey])
            plt.show()

    
def graph3d_contour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    """
    Graphs any number of 3D functions given a string function of x equating to y as a contour. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        X, Y = np.meshgrid(x, y)
        Z = f(args[i], X, Y)
        ax.contour3D(X, Y, Z, 50, cmap=cmap)
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

#["2*x", "2*y"]
def graph3d_line(*args, lrangex=-10, lrangey=-10, lrangez = -10, urangex=10, urangey=10, urangez = 10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
    """
    Graphs any number of 3D functions given a list of 2 elements - a function of x and a function of y, both equating to z. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        lis = args[i]
        fz = lis[0]
        fy = lis[1]
        if type(eval(fz)) == np.ndarray:
            zline = eval(fz)
        else:
            pass
        if type(eval(fy)) == np.ndarray:
            yline = eval(fy)
        else:
            pass
        ax.plot3D(x, yline, zline, color)
        i+=1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

def graph3d_wire(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
    """
    Graphs any number of 3D functions given a string function of x equating to y as a wire. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(x, y)
    i = 0
    while i < len(args):
        Z = f(args[i], X, Y)
        if fill==False:
            ax.plot_wireframe(X, Y, Z, color=color)
        elif edgecolor == True:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor=color)
        elif edgecolor == False:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor='none')
        else:
            raise TypeError('Parameter "edgecolor" must be a boolean operator')
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)   
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()


"""
END OF GRAPHING
"""
