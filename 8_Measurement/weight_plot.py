from matplotlib import style
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This script takes 3 arguments:
#
#     1. The filename where the data are saved for then plotting
#         - SynchCounter.txt
#         - loadweight.txt
#         - blockweight.txt
#         - lockweight.txt
#         - sleepweight.txt
#         - SynchCounter_sb.txt
#         - runtimeweight_sb.txt
#         - blockweight_sb.txt
#         - completionweight_sb.txt
#         - schedweight_sb.txt
#   2. Interval when to refresh the plot
#   3. Plot title

class Scope(object):
    def __init__(self, ax):
        self.ax     = ax
        self.x      = []
        self.y      = []
        self.lines  = 0

        self.ax.set_xlabel('Weight', fontsize=16)
        self.ax.set_ylabel('Synchronization counter', fontsize=16)

    def animate(self, i):

        try:
            file = open(DEBUG_FILE, 'r')
        except IOError:
            print "File ", DEBUG_FILE, "doesn't exist!!!"
            exit()

        data = file.readlines()
        file.close()

        if len(data) < self.lines:
            lines       = data
            self.lines  = 0
            self.x      = []
            self.y      = []
        else:
            lines = data[self.lines:]

        self.lines += len(lines)

        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                self.x.append(float(x))
                self.y.append(float(y))

        self.ax.clear()
        self.ax.plot(self.x, self.y)
        self.ax.set_title(DEBUG_PLT_TITLE, fontsize=16)
        self.ax.set_xlabel('Weight', fontsize=16)
        self.ax.set_ylabel('Synchronization counter', fontsize=16)

if __name__ == "__main__":

    global DEBUG_FILE
    global DEBUG_INTERVAL
    global DEBUG_PLT_TITLE

    DEBUG_FILE      = str(sys.argv[1])
    DEBUG_PLT_TITLE = str(sys.argv[2])
    DEBUG_INTERVAL  = int(sys.argv[3])#ms

    style.use('fivethirtyeight')

    fig = plt.figure(DEBUG_FILE)
    ax  = fig.add_subplot(1, 1, 1)

    scope = Scope(ax)
    ani = animation.FuncAnimation(fig, scope.animate, interval=DEBUG_INTERVAL)

    plt.show()
