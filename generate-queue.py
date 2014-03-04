import random

print "# Time (seconds) Size (packets)"
size = 20
q = 0
for t in range(0,10):
    r = 100 + int(10*random.random())
    for i in range(0,r):
        # randomize adding or removing a packet
        direction = random.random()
        if direction < 0.5:
            q += 1
        else:
            q -= 1
        if q < 0:
            q = 0
        if q > 20:
            q = 20
            print (t+i*1.0/r),'x'
        else:
            print (t+i*1.0/r),q
