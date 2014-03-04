# Generate some random data to simulate packets being added to and removed
# from a queue

# The output data has two columns: time (seconds) and queue size (packets)

import random

print "# Time (seconds) Size (packets)"
# maximum queue size
size = 20
# current queue length
queue_length = 0
# simulate data for 10 seconds
for t in range(0,10):
    # during each second, generate 100 + e events, where e is a random
    # number from 0 to 10
    r = 100 + int(10*random.random())
    for i in range(0,r):
        # randomize adding or removing a packet
        direction = random.random()
        if direction < 0.5:
            queue_length += 1
        else:
            queue_length -= 1
        if queue_length < 0:
            queue_length = 0
        if queue_length > 20:
            queue_length = 20
            print (t+i*1.0/r),'x'
        else:
            print (t+i*1.0/r),queue_length
