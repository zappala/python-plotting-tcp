# Generate some random data to simulate packets being delivered to a host
# over a TCP connection

# The output data has three columns: time (seconds), sequence number, and
# size of the packet delivered (bytes)

import random

print "# Time (seconds) Sequence (number) Size (bytes)"
sequence = 0
# simulate data for 10 seconds
for t in range(0,10):
    if t < 4:
        # for the first 3 seconds, generate 25*t packets, plus up to 25
        # additional packets
        r = 25*t + int(25*random.random())
    else:
        # for all other periods, generate 100 packets, plus up to 10
        # additional packets
        r = 100 + int(10*random.random())        
    for i in range(0,r):
        # generate the packets and their sequence number
        print (t+i*1.0/r),sequence,1000
        sequence += 1000
