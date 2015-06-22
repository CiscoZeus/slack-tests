from subprocess import Popen, PIPE, STDOUT
import random
import sys
percent = 100.0
p = Popen(["top","-b","-n","1"], stdout=PIPE)
count = -1
for line in p.stdout:
	line = line.split()
	print line
	if line[0] == "%Cpu(s):":
		percent = percent - float(line[7])
		break
print percent
if percent > 85:
	print "CPU Utilsation at critical levels. % = " + str(percent)
	sys.exit(2)
