import random

print "# Time (seconds) Sequence (number) Size (bytes)"
sequence = 0
for t in range(0,10):
    if t < 4:
        r = 25*t + int(25*random.random())
    else:
        r = 100 + int(10*random.random())        
    for i in range(0,r):
        print (t+i*1.0/r),sequence,1500
        sequence += 1500
