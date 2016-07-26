import time 
def quick_sort(lists,left,right):
  if left>=right:
    return lists
  key = lists[left]\
  low = left
  high = right
  whiel left<right:
    while left<right and lists[right]>=key:
      right -=1
    lists[left] = lists[right]
    while left<right and lists[left]<=right:
      left +=1
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
  return lists
start = time.clock()
lists = [8,2,0,-1,4,5,0]
l = quick_sort(lists,0,len(lists))
print l
end = time.clock()
print "the time of quick_sort cost is %f s"%(end-start)
