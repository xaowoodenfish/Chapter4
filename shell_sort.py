import time
def shell_sort(lists):
	count = len(lists)
	step = 2
	group = count/step
	while group>0:
		for i in range(0,group):
			j = i +group
			while j<count:
				k = j - group
				key = lists[j]
				while k>=0:
					if lists[k]>key:
						lists[k+group] = lists[k]
						lists[k] = key
					k -=group
				j +=group
		group /= step
	return lists
start = time.clock()
lists = [8,-1,2,6,0,4,-5,0]
l = shell_sort(lists)
print l
end = time.clock()
print "the time of shell_sort cost is %f s"%(end-start)
