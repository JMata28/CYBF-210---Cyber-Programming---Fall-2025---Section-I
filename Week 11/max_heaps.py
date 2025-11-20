#Code from: https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/ 
#Additional explanation can be found here: https://www.youtube.com/watch?v=E2v9hBgG6gE 

#CREATING MAX HEAP
import heapq  
nums = [10, 20, 15, 30, 40]  
# Convert into a max-heap by inverting values  
temp_heap = [-n for n in nums]  #temp_heap is the max_heap but with negative values, so it still is not our final max_heap
heapq.heapify(temp_heap)  
print("This is our temporary heap: ", temp_heap)
max_heap = [-n for n in temp_heap]
# Access largest element  
print("Largest element:", max_heap[0])

#ADDING NEW ELEMENTS (7, 50, and 2)
heapq.heappush(temp_heap, -7) #Notice how the values added must be negated because I'm adding them to temp_heap
heapq.heappush(temp_heap, -50)
heapq.heappush(temp_heap, -2)
print("This is our temporary heap: ", temp_heap)
max_heap = [-n for n in temp_heap]

# ACCESS OR REMOVE THE LARGEST ELEMENT
largest = -heapq.heappop(temp_heap)
print("Removed largest element:", largest)
max_heap = [-n for n in temp_heap]
print("Heap after removal:", max_heap)

#And so on...