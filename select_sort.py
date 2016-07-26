import time
def select_sort(lists):
	count = len(lists)
	for i in range(0,count):
		min = i
		for j in range(i+1,count):
			if lists[min] > lists[j]:
				min = j
			lists[min],lists[i] = lists[i],lists[min]
	return lists
start = time.clock()
lists = [8,6,-1,0,2,4,-5,0]
l = select_sort(lists)
print l
end = time.clock()
print "the time of select_sort cost %f s"%(end - start)
