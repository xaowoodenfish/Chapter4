import time
def insert_sort(lists):
  count = len(lists):
  for i in range(1,count):
    key = lists[i]
    j = i-1
    while j>=0:
      if lists[j+1]>key:
        lists[j+1] = lists[j]
        lists[j] =  key
      j -=1
  return lists
start = time.clock()
lists = [9,4,0,1,2,0,-5]
lists = insert_sort(lists)
print lists
end  = time.clock()
print "The time cost is %f s"%(end -start)
