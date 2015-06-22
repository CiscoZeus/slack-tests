from subprocess import Popen, PIPE, STDOUT
import random
import sys
capacity = 0.0
used = 0.0
p = Popen(["free","-k"], stdout=PIPE)
count = -1
for line in p.stdout:
        count = count + 1
        if count == 0:
                continue
        else:
                try:
                        line = line.split()
                        capacity = capacity + int(line[1])
                        used = used + int(line[2])
                        break
                except:
                        print "Test terminated abruptly."
                        sys.exit(2)

percent = used/capacity * 100
if percent > 85:
        print "Free RAM at critical levels. Used % = " + str(percent)
        sys.exit(2)
