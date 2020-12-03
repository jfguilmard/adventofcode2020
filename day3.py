def runslope( h,v):
	pos = 0
	count = 0
	for i in range(v,len(Lines),v):
		line=Lines[i]
		pos=(pos+h) % (len(line)-1)
		if line[pos]=="#" :
			count+=1
	print("Tree " + str(h) + "," + str(v) + " " + str(count))
	return count

file1 = open('c:\\users\\j.guilmard\\downloads\\input3.1.txt', 'r') 
Lines = file1.readlines() 

print("Trees: " + str(runslope(1,1)*runslope(3,1)*runslope(5,1)*runslope(7,1)*runslope(1,2)))
