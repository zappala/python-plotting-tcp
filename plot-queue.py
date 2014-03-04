import optparse
import sys

import matplotlib
from pylab import *

# Class that parses a file of queue events and plots a graph over time
class Plotter:
    def __init__(self,file):
        """ Initialize plotter with a file name. """
        self.file = file
        self.data = []
        self.min_time = None
        self.max_time = None

    def parse(self):
        """ Parse the data file """
        first = None
        f = open(self.file)
        for line in f.readlines():
            if line.startswith("#"):
                continue
            try:
                t,size = line.split()
            except:
                continue
            t = float(t)
            try:
                size = int(size)
            except:
                pass
            self.data.append((t,size))
            if not self.min_time or t < self.min_time:
                self.min_time = t
            if not self.max_time or t > self.max_time:
                self.max_time = t

    def plot(self):
        """ Create a line graph of the queue size over time. """
        clf()
        x = []
        y = []
        dropX = []
        dropY = []
        i = 0
        max_queue = 20
        max = None
        for (t,size) in self.data:
            if size == 'x':
                dropX.append(t)
                dropY.append(max_queue+1)
            else:
                x.append(t)
                y.append(size)

        plot(x,y)
        scatter(dropX,dropY,marker='x',color='black')
        xlabel('Time (seconds)')
        ylabel('Queue Size (packets)')
        xlim([self.min_time,self.max_time])
        ylim([0,max_queue+2])
        savefig('queue.png')

def parse_options():
        # parse options
        parser = optparse.OptionParser(usage = "%prog [options]",
                                       version = "%prog 0.1")

        parser.add_option("-f","--file",type="string",dest="file",
                          default=None,
                          help="file")

        (options,args) = parser.parse_args()
        return (options,args)


if __name__ == '__main__':
    (options,args) = parse_options()
    if options.file == None:
        print "plot.py -f file"
        sys.exit()
    p = Plotter(options.file)
    p.parse()
    p.plot()
