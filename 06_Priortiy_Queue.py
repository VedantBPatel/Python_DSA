import heapq

def max_product_of_three(arr):
    unique_elements=set(arr)
    if len(unique_elements)<3:
        return "Not enough distinct elements"
    min_heap=[]
    for num in unique_elements:
        heapq.heappush(min_heap,num)
        
        if len(min_heap)>3:
            heapq.heappop(min_heap)
    
    product=1
    for num in min_heap:
        product*=num
    return product

arr=[10,5,3,7,2,2,2,9,8,3,7]
result=max_product_of_three(arr)
print(f"Product of three largest elements: {result}")