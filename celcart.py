import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepares given file then converts coordinates to cartesian and plots them.
def celestial_conv(filename):
    neo_cel_table = pd.read_csv(filename)
    ra = neo_cel_table.loc[:, 'AstRA(deg)']
    dec = neo_cel_table.loc[:, 'AstDec(deg)']
    dist = neo_cel_table.loc[:, 'AstRange(km)']
    x = (dist) * np.cos(dec) * np.cos(ra)
    y = (dist) * np.cos(dec) * np.sin(ra)
    z = (dist) * np.sin(dec)
    def neo_cart_plot(x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        fig.set_size_inches(11,11)
        fig.tight_layout()
        ax.scatter(x,y,z)
        ax.set_xlim(-700000000, 700000000)
        ax.set_ylim(-700000000, 700000000)
        ax.set_zlim(-700000000, 700000000)
        ax.set_xlabel('X-Coordinates')
        ax.set_ylabel('Y-Coordinates')
        ax.set_zlabel('Z-Coordinates')
        return 
    return neo_cart_plot(x,y,z)

# Prepares a CSV with X-Coordinates, Y-Coordinates, and Z-Coordinates columms to be placed into cartesain_to_celestial functions
def cartesian_conv(filename):
    neo_cart_table = pd.read_csv(filename)
    x = neo_cart_table.loc[:,'X-Coordinates']
    y = neo_cart_table.loc[:, 'Y-Coordinates']
    z = neo_cart_table.loc[:, 'Z-Coordinates']
    ra = np.arccos(x / (np.sqrt(x**2 + y**2)))
    dec = np.arcsin(z / (np.sqrt(x**2 + y**2 + z**2)))
    dist = np.sqrt(x**2 + y**2 + z**2)
    return (ra,dec,dist)

# Takes celestial coordinates and converts them into a list of cartesians coordinates
def celestial_to_cartesian(ra, dec, dist):
    x = (dist) * np.cos(dec) * np.cos(ra)
    y = (dist) * np.cos(dec) * np.sin(ra)
    z = (dist) * np.sin(dec)
    return (x, y, z)

# Takes cartesain coordinates and converts them into a list of celestial coordinates
def cartesian_to_celestial(x, y, z):
    ra = np.arccos(x / (np.sqrt(x**2 + y**2)))
    dec = np.arcsin(z / (np.sqrt(x**2 + y**2 + z**2)))
    dist = np.sqrt(x**2 + y**2 + z**2)
    return (ra, dec, dist)

# Takes a set of prepared castesian coordinates and plots them on a 3D plot
def neo_cart_plot(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    fig.set_size_inches(11,11)
    fig.tight_layout()

    ax.scatter(x,y,z)
    
    ax.set_xlim(-100000000000, 100000000000)
    ax.set_ylim(-100000000000, 100000000000)
    ax.set_zlim(-100000000000, 100000000000)

    ax.set_xlabel('X-Coordinates')
    ax.set_ylabel('Y-Coordinates')
    ax.set_zlabel('Z-Coordinates')
    return 
