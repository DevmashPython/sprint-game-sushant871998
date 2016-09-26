import msvcrt
import time
m=0
n=10
o=0
p=5
q=0
r=10
print"press return key to get started"
raw_input()
s_time=time.time()
print "press d"
while(1):
	key=msvcrt.getch()
	if key=='d':
		m=m+1
		print"-->",
		if m==n:
			print"press s key to move down"
			break
	else:
		print"sry u lost d the game"
		exit(1)
while(1):
 	key1=msvcrt.getch()
 	if key1=='s':
 		o=o+1
 		print"                                        |"
 		print"                                        v"
 		if o==p:
 			print "               press d key to mov right" ,
 			break
 	else:
 		print"sry u lost the game"
 		exit(1)


while(1):
 	key2=msvcrt.getch()
 	if key2=='d':
 		q=q+1
 		print"-->" ,
 		if q==r:
 			break
 	else:
 		print"sry u lost d game "
 		exit(1)
time_elapsed=time.time()-s_time
print "congo u have finished d game"
print "ur time was"+str(time_elapsed)
 	
