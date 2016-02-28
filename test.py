import numpy as np
import matplotlib.pyplot as plt
from easygui import *
location = enterbox("Enter number of locations")

for i in range(1,int(location)+1):
    longitude = enterbox("Enter the longitude of location ", i)
    latitude= enterbox("Enter the latitude of location " ,i)
 
    plt.scatter(longitude,latitude)
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append((x))
            yar.append((y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
