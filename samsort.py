from timeit import default_timer as timer
import numpy as np
import bisect

def findIndex(arr, value):
    '''
    low = 0
    high = len(arr) - 1
    while(low < high):
        index = (high + low)//2
        left = arr[index - 1] <= value
        right = arr[index] >= value
        #basecase: we've got the right index
        if(left and right):
            return index
        #if left condition is not met we check the left side
        elif(not left):
            high = index
        #if the right condition is not met we check the right
        else:
            low = index
    '''
    #bisect is still slightly faster than my function so im using it
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
        chunk.insert(findIndex(chunk, value), value)


def chunkSort(arr):

    if len(arr) <= 100:
        left = []
        right = []
        pivot = arr[len(arr)//2]
        for value in arr:
            if value <= pivot:
                left.append(value)
            else:
                right.append(value)
        chunkSort(left)
        chunkSort(right)
        return left + right
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
    test = list(np.random.random(size))
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
    #to make sure its sorted
    print(["Did not sort succesfully", "Successfully sorted"][test == test_two])
if __name__ == "__main__":
    main()
