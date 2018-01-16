def quick_sort(alist,start,end):
	if start == end :
		return
	# 快速排序
 	mid = alist[start]
 	low = start
 	high = end # n是列表的长度
 	while low < high:

	 	while low < high and alist[high] >= mid:
	 		high -= 1
	 	alist[low] = alist[high]
	 	

	 	while low < high and alist[low] < mid:
	 		low += 1
	 	alist[high] = alist[low]
	 # 从循环退出时，low=high
	 alist[low] = mid
	 quick_sort(alist,start,low-1) 
	 quick_sort(alist,low+1,end)
