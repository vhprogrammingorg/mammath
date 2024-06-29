from .helper import parse_graphing, f, deprecated
import numpy as np
import matplotlib as plt

@deprecated
def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    """
    Plots any number of 2D functions given a string function of x equating to y. The first 4 keyword arguments change the axis of the graph.
    
    Args:
        *args (str): Any number of string functions of x equating to y.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 100.
        gridset (bool, optional): Whether to display the grid or not. Defaults to True.
        scaling (bool, optional): Whether to enable autoscaling or not. Defaults to True.
        graph_title (str, optional): The title of the graph. Defaults to None.
        xtitle (str, optional): The label for the x-axis. Defaults to None.
        ytitle (str, optional): The label for the y-axis. Defaults to None.

    Returns:
        None
    """
    args = list(args)
    for i in range(0, len(args)):
        args[i] = parse_graphing(args[i])
    
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

@deprecated
def graph3d_wire(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
    """
    Plots any number of 3D wireframe functions given a string function of x equating to y as a wire. The first 6 keyword arguments change the axis of the graph.
    
    Args:
        *args (str): Any number of string functions of x equating to y.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        lrangez (float, optional): The lower bound for the z-axis. Defaults to -10.
        urangez (float, optional): The upper bound for the z-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        edgecolor (bool, optional): Whether to display edge colors for the wireframe or not. Defaults to False.
        color (str, optional): The color of the wireframe lines. Defaults to 'black'.
        fill (str, optional): The colormap to use for the wireframe. Defaults to 'viridis'
        
    Returns:
        None
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

@deprecated
def graph3d_surface(fx, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
    """
    Plots a 3D surface function given a string function fx of x and y.
    
    Args:
        fx (str): The string function of x and y.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        lrangez (float, optional): The lower bound for the z-axis. Defaults to -10.
        urangez (float, optional): The upper bound for the z-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        edgecolor (bool, optional): Whether to display edge colors for the surface or not. Defaults to False.
        color (str, optional): The color of the surface lines. Defaults to 'black'.
        fill (str, optional): The colormap to use for the surface. Defaults to 'viridis'
        
    Returns:
        None
    """
    
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    X, Y = np.meshgrid(x, y)
    Z = f(fx, X, Y)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    if edgecolor == True:
        ax.plot_surface(X, Y, Z, cmap=fill, edgecolor=color)
    elif edgecolor == False:
        ax.plot_surface(X, Y, Z, cmap=fill, edgecolor='none')
    else:
        raise TypeError('Parameter "edgecolor" must be a boolean operator')
    
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    
    ax.set_zlim(lrangez, urangez)
    ax.set_xlim(lrangex, urangex)
    ax.set_ylim(lrangey, urangey)
    
    plt.show()

@deprecated
def graph3d_wireframe(fx, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='black'):
    """
    Plots a 3D wireframe function given a string function fx of x and y.
    
    Args:
        fx (str): The string function of x and y.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        lrangez (float, optional): The lower bound for the z-axis. Defaults to -10.
        urangez (float, optional): The upper bound for the z-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        color (str, optional): The color of the wireframe lines. Defaults to 'black'.
        
    Returns:
        None
    """
    
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    X, Y = np.meshgrid(x, y)
    Z = f(fx, X, Y)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    ax.plot_wireframe(X, Y, Z, color=color)
    
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    
    ax.set_zlim(lrangez, urangez)
    ax.set_xlim(lrangex, urangex)
    ax.set_ylim(lrangey, urangey)
    
    plt.show()
