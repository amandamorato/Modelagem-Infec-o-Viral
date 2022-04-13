# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import pandas as pd

def readFile(filename):
    file = open(filename, 'r')
    if (file):        
        return pd.read_csv(filename)
    else: 
        print('Error: it was not possible to open the file!')
        exit

def getArrayFromFile(filename):
    file = open(filename, 'r')
    if (file):        
        return np.loadtxt(file, delimiter='\n')
    else: 
        print('Error: it was not possible to open the file!')
        exit

def createFigure(title):
    fig = plt.figure(figsize=(10,7))    
    plt.tick_params(labelsize=18)
    plt.title(title, fontsize=19)
    plt.xlabel('Tempo',fontsize=18)
    plt.ylabel('Concentração',fontsize=18)
    ax = fig.gca()
    return [fig,ax]
    
def initializeGraphParameters():
    global scalarMap, color_index, colorVal
    cm = plt.get_cmap('jet')
    cNorm  = colors.Normalize(vmin=0, vmax=100)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    color_index = 0
    colorVal = scalarMap.to_rgba(color_index)

def saveFig(fig, filename):
    fig.savefig(dir_ + filename + '.svg', format='svg', bbox_inches='tight')

dir_ = ''
initializeGraphParameters()

odeValues = readFile(dir_+'oderesults.csv')
print(odeValues)
t = odeValues['Time']
E = odeValues['E']
I = odeValues['I']
V = odeValues['V']
T = odeValues['T']

fig,ax = createFigure('T')
ax.plot(t, T, label="Células de defesa", color=colorVal)
color_index += 8
colorVal = scalarMap.to_rgba(color_index)
ax.legend(loc='upper right', fontsize=15)
ax.grid()
saveFig(fig,dir_+'T')
fig.clear()
ax.clear()

fig,ax = createFigure('E')
ax.plot(t, E, label="Células epiteliais saudáveis", color=colorVal)
color_index += 8
colorVal = scalarMap.to_rgba(color_index)
ax.legend(loc='upper right', fontsize=15)
ax.grid()
saveFig(fig,dir_+'E')
fig.clear()
ax.clear()

fig,ax = createFigure('I')
ax.plot(t, I, label="Células epiteliais infectadas", color=colorVal)
color_index += 8
colorVal = scalarMap.to_rgba(color_index)
ax.legend(loc='upper right', fontsize=15)
ax.grid()
saveFig(fig,dir_+'I')
fig.clear()
ax.clear()

fig,ax = createFigure('V')
ax.plot(t,V,label="Virus", color=colorVal)
color_index += 8
colorVal = scalarMap.to_rgba(color_index)
ax.legend(loc='upper right', fontsize=15)
ax.grid()
saveFig(fig,dir_+'V')
fig.clear()
ax.clear()