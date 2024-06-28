import matplotlib.pyplot as plt
import warnings
import numpy as np
from .helper import f, parse_graphing
from .constants import *
from .operations import *


"""
GRAPHING
"""
#graph("2*x", "3*x")
def graph_str(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
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

def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    warnings.warn(
        "This function is deprecated and will be removed in a future version. It has been replaced with graph_str for this purpose and graph_func for other purposes.",
        DeprecationWarning,
        stacklevel=2
    )
    return graph_str(*args, lrangex=lrangex, urangex=urangex, lrangey=lrangey, urangey=urangey, graph_points=graph_points, gridset=gridset, scaling=scaling, graph_title=graph_title, xtitle=xtitle, ytitle=ytitle)

def plot_histogram(data, bins=10, range=None, xlabel='Value', ylabel='Frequency', title=None):
    """
    Plots a histogram of the given data.
    
    Args:
        data (array-like): The data to plot.
        bins (int, optional): The number of bins. Defaults to 10.
        range (tuple, optional): The lower and upper range of the bins. Defaults to None.
        xlabel (str, optional): The label for the x-axis. Defaults to 'Value'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Frequency'.
        title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    plt.hist(data, bins=bins, range=range)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.show()

def plot_box(data, labels=None, xlabel=None, ylabel='Value', title=None):
    """
    Plots a box plot of the given data.
    
    Args:
        data (array-like): The data to plot. Each element in the array should be a dataset.
        labels (array-like, optional): The labels for each dataset. Defaults to None.
        xlabel (str, optional): The label for the x-axis. Defaults to None.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Value'.
        title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    plt.boxplot(data, labels=labels)
    if xlabel:
        plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.show()

def plot_scatter_with_regression(x, y, xlabel='X', ylabel='Y', title=None):
    """
    Plots a scatter plot of the given data with a regression line.
    
    Args:
        x (array-like): The x-coordinates of the data points.
        y (array-like): The y-coordinates of the data points.
        xlabel (str, optional): The label for the x-axis. Defaults to 'X'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Y'.
        title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    plt.scatter(x, y, label='Data Points')
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, color='red', label='Regression Line')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.legend()
    plt.show()

def plot_heatmap(data, xlabel='X', ylabel='Y', title=None, cmap='viridis'):
    """
    Plots a heatmap of the given data.
    
    Args:
        data (array-like): The data to plot. Should be a 2D array or matrix.
        xlabel (str, optional): The label for the x-axis. Defaults to 'X'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Y'.
        title (str, optional): The title of the graph. Defaults to None.
        cmap (str, optional): The colormap to use. Defaults to 'viridis'.
    
    Returns:
        None
    """
    plt.imshow(data, aspect='auto', cmap=cmap)
    plt.colorbar()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.show()

def plot_time_series(time, values, xlabel='Time', ylabel='Value', title=None):
    """
    Plots a time series of the given data.
    
    Args:
        time (array-like): The time points.
        values (array-like): The values at each time point.
        xlabel (str, optional): The label for the x-axis. Defaults to 'Time'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Value'.
        title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    plt.plot(time, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.show()

def plot_lissajous(a, b, delta, t_max=10, num_points=1000, xlabel='X', ylabel='Y', title='Lissajous Curve'):
    """
    Plots a Lissajous curve with the given parameters.
    
    Args:
        a (float): Parameter a for the x equation.
        b (float): Parameter b for the y equation.
        delta (float): Phase shift.
        t_max (float, optional): The maximum value of t. Defaults to 10.
        num_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        xlabel (str, optional): The label for the x-axis. Defaults to 'X'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'Y'.
        title (str, optional): The title of the graph. Defaults to 'Lissajous Curve'.
    
    Returns:
        None
    """
    t = np.linspace(0, t_max, num_points)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def plot_mandelbrot(xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=256, cmap='hot'):
    """
    Plots the Mandelbrot set.
    
    Args:
        xmin (float, optional): The minimum x-value. Defaults to -2.
        xmax (float, optional): The maximum x-value. Defaults to 2.
        ymin (float, optional): The minimum y-value. Defaults to -2.
        ymax (float, optional): The maximum y-value. Defaults to 2.
        width (int, optional): The width of the image in pixels. Defaults to 800.
        height (int, optional): The height of the image in pixels. Defaults to 800.
        max_iter (int, optional): The maximum number of iterations. Defaults to 256.
        cmap (str, optional): The colormap to use. Defaults to 'hot'.
    
    Returns:
        None
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = Z.copy()
    
    img = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)
    
    for i in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mask = np.logical_and(mask, np.abs(Z) < 2)
        img += mask
    
    plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap=cmap, origin='lower')
    plt.colorbar(label='Iterations')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title('Mandelbrot Set')
    plt.show()

def graph3d_contour_str(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    """
    Plots any number of 3D functions given a string function of x equating to y as a contour. The first 6 keyword arguments change the axis of the graph.
    
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
        cmap (str, optional): The colormap to use for the contour plot. Defaults to 'binary'.

    Returns:
        None
    """
    args = list(args)
    for i in range(0, len(args)):
        args[i] = parse_graphing(args[i])
        
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

def graph3d_contour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    warnings.warn(
        "This function is deprecated and will be removed in a future version. It has been replaced by graph3d_contour_str and graph3d_contour_func.",
        DeprecationWarning,
        stacklevel=2
    )
    return graph3d_contour_str(*args, lrangex=lrangex, lrangey=lrangey, urangex=urangex, urangey=urangey, lrangez=lrangez, urangez=urangez, graph_points=graph_points, lablex=lablex, labley=labley, lablez=lablez, graph_title=graph_title, cmap=cmap)

#["2*x", "2*y"]
def graph3d_line(*args, lrangex=-10, lrangey=-10, lrangez = -10, urangex=10, urangey=10, urangez = 10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
    warnings.warn(
        "This function is deprecated and will be removed in a future version. It has been replaced with graph3d_parametric",
        DeprecationWarning,
        stacklevel=2
    )
    """
    Plots any number of 3D line functions given a list of 2 elements - a function of x and a function of y, both equating to z. The first 6 keyword arguments change the axis of the graph.
    
    Args:
        *args (list): Any number of lists containing two elements - a function of x and a function of y, both equating to z.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        lrangez (float, optional): The lower bound for the z-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        urangez (float, optional): The upper bound for the z-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        color (str, optional): The color of the line plot. Defaults to 'gray'.

    Returns:
        None
    """
    args = list(args)[0]
    for i in range(0, len(args)):
        args[i] = parse_graphing(args[i])
    print(args)

    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        lis = args[i]
        fz = lis[0]
        fy = lis[1]
        zline = fz
        yline = fy
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

def graph3d_scatter(x_data, y_data, z_data, xlabel='x', ylabel='y', zlabel='z', graph_title=None):
    """
    Plots a 3D scatter plot with the given x, y, and z data points.
    
    Args:
        x_data (array-like): The x-coordinates of the data points.
        y_data (array-like): The y-coordinates of the data points.
        z_data (array-like): The z-coordinates of the data points.
        xlabel (str, optional): The label for the x-axis. Defaults to 'x'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'y'.
        zlabel (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.

    Returns:
        None
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(x_data, y_data, z_data)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(graph_title)

    return plt.show()

def graph3d_bar(x_data, y_data, z_data, xlabel='x', ylabel='y', zlabel='z', graph_title=None):
    """
    Plots a 3D bar plot with the given x, y, and z data points.
    
    Args:
        x_data (array-like): The x-coordinates of the bars.
        y_data (array-like): The y-coordinates of the bars.
        z_data (array-like): The heights of the bars.
        xlabel (str, optional): The label for the x-axis. Defaults to 'x'.
        ylabel (str, optional): The label for the y-axis. Defaults to 'y'.
        zlabel (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.

    Returns:
        None
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.bar3d(x_data, y_data, np.zeros_like(z_data), 0.5, 0.5, z_data)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(graph_title)

    return plt.show()

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
    
"""
END OF GRAPHING
"""
