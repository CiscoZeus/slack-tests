from subprocess import Popen, PIPE, STDOUT
import random
import sys
p = Popen(["nping", "-c1" ,"-p", sys.argv[2],sys.argv[1]], stdout=PIPE)
fail = False
for line in p.stdout:
	if "refused" in line:
		fail = True

if (fail):
	print "Fail"
	sys.exit(2)
	
