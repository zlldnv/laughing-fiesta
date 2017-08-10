import time

a= 11.669
b = 46.713
f = open('dataset.txt', 'w')
while True:
    time.sleep(1)
    a += 0.001
    b += 0.001
    f.write(str("%.0f" % time.time())+','+str(a)+','+str(b)+'\n')
    print "%.0f" % time.time(),a,b
