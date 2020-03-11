from timeit import default_timer as timer
import numpy as np
import bisect

def findIndex(arr, value, index):
    '''
    left = arr[index - 1] <= value
    right = arr[index] >= value
    print(f"{value} belongs at position {index} in {arr}")
    print(left, right)
    #edgecase: index's outside range of list
    if(index >= len(arr)):
        index = len(arr) - 2
    #basecase: we've got the right index
    if(left and right):
        return index
    #if left condition is not met we check the left side
    elif(not left):
        return findIndex(arr, value, index//2)
    #if the right condition is not met we check the right
    elif(not right):
        return findIndex(arr, value, index//2 + index)
    '''
    #ran into recursion limit issues with my above method(which shouldnt be happening so while i work on that..)
    #bisect does what my code will eventually do
    return bisect.bisect(arr, value)

def addToChunk(chunk, value):

    #base cases: 
    #when value is greater than the largest value in the chunk
    #when value is less than the smallest value in the chunk
    if value >= chunk[-1]:
        chunk.append(value)
    elif(value < chunk[0]):
        chunk.insert(0, value)
    else:
        #initally check the middle of the list
        chunk.insert(findIndex(chunk, value, len(chunk)//2), value)


def chunkSort(arr):
    #base case
    if(len(arr) <= 1 ):
        return arr
    chunk = arr[:2]
    arr = arr[2:]
    #if they're not in order swap them
    if(chunk[0] > chunk[1]):
        chunk[0], chunk[1] = chunk[1], chunk[0]

    for value in arr:
        addToChunk(chunk, value)
    return chunk

def main():
    

    #very basic test
    size = 100000
    #converting them back into lists so I dont have to rewrite a bunch of the code
    #using an np.array() would be alot more efficient than python list
    #test = list(np.random.random(size))
    test = list(np.random.randint(0, 2**31, size))
    test_two = test.copy()
    #timing pythons .sort method { timsort}
    sort_start = timer()
    test_two.sort()
    sort_end = timer()
    
    #timing chunksort
    chunk_start = timer() 
    test = chunkSort(test)
    chunk_end = timer()
    diff = (chunk_end - chunk_start) / (sort_end - sort_start)

    

    print("Chunksort took:", chunk_end - chunk_start)
    print("the list.sort method took:", sort_end - sort_start)
    print(f"Chunksort was {diff} times slower for a list of size {size}")

if __name__ == "__main__":
    main()
