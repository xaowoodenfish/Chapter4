import time 
def bubble_sort(lists):
  count = len(lists)
  for i in range(1,count):
    for j in range(i+1,count):
      if lists[i]>lists[j]:
        lists[j],lists[i] = lists[i],lists[j]
  return lists
start = time.clock()
lists = [9,4,6,-5,0,-1,0,2]
lists = bubble_sort(lists)
print lists
end = time.clock()
print "the time of bubble sort is %f s"%(end-start)
