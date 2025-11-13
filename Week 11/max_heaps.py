#Code from: https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/ 
#Additional explanation can be found here: https://www.youtube.com/watch?v=E2v9hBgG6gE 

#CREATING MAX HEAP
import heapq  
nums = [10, 20, 15, 30, 40]  
# Convert into a max-heap by inverting values  
max_heap = [-n for n in nums]  
heapq.heapify(max_heap)  
# Access largest element (invert sign again)  
print("Largest element:", -max_heap[0])

#ADDING NEW ELEMENTS (7, 50, and 2)
heapq.heappush(max_heap, -7) #Notice how the values added must be negated
heapq.heappush(max_heap, -50)
heapq.heappush(max_heap, -2)

# ACCESS OR REMOVE THE LARGEST ELEMENT
largest = -heapq.heappop(max_heap)
print("Removed largest element:", largest)
print("Heap after removal:", [-x for x in max_heap])

#And so on...