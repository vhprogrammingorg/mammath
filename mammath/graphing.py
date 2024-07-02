import matplotlib.pyplot as plt
import numpy as np
from .helper import f, parse_graphing
from .constants import *
from .operations import *


"""
GRAPHING
"""
def graph2d_func(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    """
    Plots any number of 2D functions given a function of x equating to y. The first 4 keyword arguments change the axis of the graph.
    
    Args:
        *args (function): Any number of functions of x equating to y.
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
    
    x = np.linspace(lrangex, urangex, graph_points)
    fig, ax = plt.subplots()
    
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    
    for func in args:
        y = func(x)
        ax.plot(x, y, label=func.__name__)
    
    if graph_title:
        plt.title(graph_title)
    if xtitle:
        plt.xlabel(xtitle, fontsize=20)
    if ytitle:
        plt.ylabel(ytitle, fontsize=20)
        
    plt.autoscale(enable=scaling)
    plt.grid(gridset)
    
    if lrangex is not None and urangex is not None:
        plt.xlim([lrangex, urangex])
    if lrangey is not None and urangey is not None:
        plt.ylim([lrangey, urangey])
    
    plt.legend()
    plt.show()

def graph3d_func(*args, plot_type='contour', lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    """
    Plots any number of 3D functions given a function of x and y as a contour, wireframe, surface, or other plot. The first 6 keyword arguments change the axis of the graph.
    
    Args:
        *args (function): Any number of functions of x and y equating to z.
        plot_type (str, optional): Type of plot - 'contour', 'wireframe', 'surface', etc. Defaults to 'contour'.
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
        cmap (str, optional): The colormap to use for the plot. Defaults to 'binary'.

    Returns:
        None
    """
    
    x = np.linspace(lrangex, urangex, int(np.sqrt(graph_points)))
    y = np.linspace(lrangey, urangey, int(np.sqrt(graph_points)))
    X, Y = np.meshgrid(x, y)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    for func in args:
        Z = func(X, Y)
        if plot_type == 'contour':
            ax.contour3D(X, Y, Z, 50, cmap=cmap)
        elif plot_type == 'wireframe':
            ax.plot_wireframe(X, Y, Z)
        elif plot_type == 'surface':
            ax.plot_surface(X, Y, Z, cmap=cmap)
        elif plot_type == 'trisurf':
            ax.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten(), cmap=cmap)
        elif plot_type == 'scatter':
            ax.scatter(X, Y, Z, c=Z, cmap=cmap)
        else:
            raise ValueError("plot_type must be 'contour', 'wireframe', 'surface', 'trisurf', or 'scatter'")
    
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    if graph_title:
        ax.set_title(graph_title)
    
    if lrangez is not None and urangez is not None:
        ax.set_zlim(lrangez, urangez)
    if lrangex is not None and urangex is not None:
        ax.set_xlim(lrangex, urangex)
    if lrangey is not None and urangey is not None:
        ax.set_ylim(lrangey, urangey)
    
    plt.show()


def graph2d_parametric(*args, t_range=(0, 2*np.pi), graph_points=1000, lablex='x', labley='y', graph_title=None):
    """
    Plots multiple 2D parametric functions.
    
    Args:
        *args (tuple): Tuples of (x_func, y_func) where each is a function of t.
        t_range (tuple, optional): The range of the parameter t. Defaults to (0, 2*pi).
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        graph_title (str, optional): The title of the graph. Defaults to None.

    Returns:
        None
    """
    
    t = np.linspace(t_range[0], t_range[1], graph_points)
    
    for x_func, y_func in args:
        x = x_func(t)
        y = y_func(t)
        plt.plot(x, y, label=f'{x_func.__name__}, {y_func.__name__}')
    
    plt.xlabel(lablex)
    plt.ylabel(labley)
    if graph_title:
        plt.title(graph_title)
    plt.legend()
    plt.grid(True)
    plt.show()

def graph3d_parametric(*args, t_range=(0, 2*np.pi), graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='viridis'):
    """
    Plots multiple 3D parametric functions.
    
    Args:
        *args (tuple): Tuples of (x_func, y_func, z_func) where each is a function of t.
        t_range (tuple, optional): The range of the parameter t. Defaults to (0, 2*pi).
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        cmap (str, optional): The colormap to use for the plot. Defaults to 'viridis'.

    Returns:
        None
    """
    
    t = np.linspace(t_range[0], t_range[1], graph_points)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    for x_func, y_func, z_func in args:
        X = x_func(t)
        Y = y_func(t)
        Z = z_func(t)
        ax.plot3D(X, Y, Z, label=f'{x_func.__name__}, {y_func.__name__}, {z_func.__name__}')
    
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    if graph_title:
        ax.set_title(graph_title)
    ax.legend()
    
    plt.show()

def plot2d_vals_func(x_values, y_values, func):
    '''
    Plots values and a function on one graph
    
    Parameters:
    x_values (array-like): The x coordinates of the data points.
    y_values (array-like): The y coordinates of the data points.
    poly_func (np.poly1d): The function.
    '''
    plt.scatter(x_values, y_values, color='red', label='Data points')
    
    x_fit = np.linspace(min(x_values), max(x_values), 500)
    y_fit = func(x_fit)
    
    plt.plot(x_fit, y_fit, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparative Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

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

def riemann_zeta(start, end, num_points=1000):
    '''
    Plots the Riemann zeta function in the complex plane over a range of values.
    
    Parameters:
    start (float): The start of the range for the imaginary part of s.
    end (float): The end of the range for the imaginary part of s.
    num_points (int): The number of points to plot.
    '''
    t_values = np.linspace(start, end, num_points)

    zeta_real = [re(z) for z in zeta_values]
    zeta_imag = [im(z) for z in zeta_values]

    plt.figure(figsize=(10, 10))

    plt.plot(zeta_real, zeta_imag, label=r'$\zeta(0.5 + it)$', color='blue')

    plt.title('Riemann Zeta Function in the Complex Plane')
    plt.xlabel('Real part')
    plt.ylabel('Imaginary part')
    plt.grid(True)
    plt.legend()

    plt.show()

def graph3d_contour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
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

#["2*x", "2*y"]
def graph3d_line(*args, lrangex=-10, lrangey=-10, lrangez = -10, urangex=10, urangey=10, urangez = 10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
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

def graph3d_projection(f, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, lablex='x', labley='y', lablez='z', graph_title=None, cmap='viridis'):
    """
    Creates 2D slice functions from a 3D function f(x, y).
    
    Args:
        f (function): The function f(x, y) to plot.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 100.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        cmap (str, optional): The colormap to use for the plot. Defaults to 'viridis'.

    Returns:
        tuple: Functions to plot the slices at specified x, y, and z coordinates.
    """
    
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    def plot_xy_slice(z_value):
        plt.figure()
        cp = plt.contourf(X, Y, Z, cmap=cmap)
        plt.colorbar(cp)
        plt.xlabel(lablex)
        plt.ylabel(labley)
        plt.title(f"{graph_title} - XY Plane at z={z_value}")
        plt.axhline(y=z_value, color='r', linestyle='--')
        plt.show()

    def plot_xz_slice(y_value):
        plt.figure()
        plt.plot(x, f(x, y_value), label=f'y={y_value:.2f}')
        plt.xlabel(lablex)
        plt.ylabel(lablez)
        plt.title(f"{graph_title} - XZ Plane at y={y_value}")
        plt.grid(True)
        plt.show()

    def plot_yz_slice(x_value):
        plt.figure()
        plt.plot(y, f(x_value, y), label=f'x={x_value:.2f}')
        plt.xlabel(labley)
        plt.ylabel(lablez)
        plt.title(f"{graph_title} - YZ Plane at x={x_value}")
        plt.grid(True)
        plt.show()

    return plot_xy_slice, plot_xz_slice, plot_yz_slice

import numpy as np
import matplotlib.pyplot as plt

def graph3d_parametric_projection(x_func, y_func, z_func, t_range=(0, 2*np.pi), graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='viridis'):
    """
    Creates 2D slice functions from a 3D parametric function.
    
    Args:
        x_func (function): The parametric function for x.
        y_func (function): The parametric function for y.
        z_func (function): The parametric function for z.
        t_range (tuple, optional): The range of the parameter t. Defaults to (0, 2*pi).
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 1000.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        lablez (str, optional): The label for the z-axis. Defaults to 'z'.
        graph_title (str, optional): The title of the graph. Defaults to None.
        cmap (str, optional): The colormap to use for the plot. Defaults to 'viridis'.

    Returns:
        tuple: Functions to plot the slices at specified x, y, and z coordinates.
    """
    
    t = np.linspace(t_range[0], t_range[1], graph_points)
    X = x_func(t)
    Y = y_func(t)
    Z = z_func(t)
    
    def plot_xy_slice(z_value):
        plt.figure()
        plt.plot(X, Y, label='XY')
        plt.axhline(y=z_value, color='r', linestyle='--')
        plt.xlabel(lablex)
        plt.ylabel(labley)
        plt.title(f"{graph_title} - XY Plane at z={z_value}")
        plt.grid(True)
        plt.show()

    def plot_xz_slice(y_value):
        plt.figure()
        plt.plot(X, Z, label='XZ')
        plt.axhline(y=y_value, color='r', linestyle='--')
        plt.xlabel(lablex)
        plt.ylabel(lablez)
        plt.title(f"{graph_title} - XZ Plane at y={y_value}")
        plt.grid(True)
        plt.show()

    def plot_yz_slice(x_value):
        plt.figure()
        plt.plot(Y, Z, label='YZ')
        plt.axhline(y=x_value, color='r', linestyle='--')
        plt.xlabel(labley)
        plt.ylabel(lablez)
        plt.title(f"{graph_title} - YZ Plane at x={x_value}")
        plt.grid(True)
        plt.show()

    return plot_xy_slice, plot_xz_slice, plot_yz_slice

def vector_field(u, v, lrangex=-10, urangex=10, lrangey=-10, urangey=10, grid_points=20, lablex='x', labley='y', graph_title=None):
    """
    Plots a 2D vector field given the vector components u(x, y) and v(x, y).
    
    Args:
        u (function): The function representing the x-component of the vector at each point (x, y).
        v (function): The function representing the y-component of the vector at each point (x, y).
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        grid_points (int, optional): The number of points in the grid for plotting the vector field. Defaults to 20.
        lablex (str, optional): The label for the x-axis. Defaults to 'x'.
        labley (str, optional): The label for the y-axis. Defaults to 'y'.
        graph_title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    
    x = np.linspace(lrangex, urangex, grid_points)
    y = np.linspace(lrangey, urangey, grid_points)
    X, Y = np.meshgrid(x, y)
    U = u(X, Y)
    V = v(X, Y)
    
    plt.figure()
    plt.quiver(X, Y, U, V)
    plt.xlabel(lablex)
    plt.ylabel(labley)
    plt.title(graph_title)
    plt.grid(True)
    plt.show()


def complex_function(f, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=400, graph_title=None):
    """
    Plots a complex function f(z) where z = x + iy.
    
    Args:
        f (function): The complex function to plot.
        lrangex (float, optional): The lower bound for the x-axis. Defaults to -10.
        urangex (float, optional): The upper bound for the x-axis. Defaults to 10.
        lrangey (float, optional): The lower bound for the y-axis. Defaults to -10.
        urangey (float, optional): The upper bound for the y-axis. Defaults to 10.
        graph_points (int, optional): The number of points to sample for the graph. Defaults to 400.
        graph_title (str, optional): The title of the graph. Defaults to None.
    
    Returns:
        None
    """
    
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    F = f(Z)
    magnitude = np.abs(F)
    phase = np.angle(F)
    plt.figure(figsize=(8, 6))
    plt.imshow(phase, extent=(lrangex, urangex, lrangey, urangey), origin='lower', cmap='hsv')
    plt.colorbar(label='Phase (radians)')
    plt.contour(X, Y, magnitude, colors='black', alpha=0.5)
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.title(graph_title)
    plt.show()


"""
END OF GRAPHING
"""
