from timeit import default_timer as timer
import numpy as np

def findIndex(target, arr):
    '''
    Implementation of a binary search
    '''
    #pos = middle index
    pos = len(arr)//2
    if not arr:
        return 0
    #base case
    if len(arr) == 1:
        if arr[0] < target:
            return 1
        else:
            return 0
    if arr[pos] == target:
        return pos
    #if the middle element is greater than our target 
    elif(arr[pos] > target):
        return findIndex(target, arr[:pos])
    #otherwise
    else:
        return findIndex(target, arr[pos:]) + pos
    

class Chunk(object):
    
    def __init__(self, arr):
        #data stores the max and min of each chunk
        self._data = [arr[0], arr[-1]]
        self._numbers = arr
        
    def insert(self, num):
        '''
        Function for adding a new number to the chunk
        basicly if a number is less than data[0] then this number is our new minimum and we toss it in 
        if a number is greater than data[1] then that number is our new maximum, same idea
        '''
        if num >= self._data[1]:
            self._numbers.append(num)
            self.updateData()
        elif(num <= self._data[0]):
            self._numbers.insert(0, num)
            self.updateData()
        #otherwise we need to find where it belongs in this list, so using binary search we find that specific index
        else:
            index = findIndex(num, self._numbers)
            self._numbers.insert(index, num)

    def getNumbers(self):
        return self._numbers
    def updateData(self):
        self._data[0] = self._numbers[0]
        self._data[1] = self._numbers[-1]

def initalValues(arr):

    first_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= first_value:
            return [0, i]
    return [1, 0]
    
def chunkSort(arr):

    #handling base cases 
    if len(arr) <= 1:
        return arr
    elif(len(arr) == 2):
        if arr[1] > arr[0]:
            return arr[::-1]
        return arr
    #otherwise look for a pair of numbers that are in order then use them to create the inital chunk
    chunk = Chunk(arr[:2])
    inital_chunk = initalValues(arr)
    
    for index in inital_chunk:
        arr.pop(index)

    #we sort it by inserting each number into the chunk object
    for value in arr:
        chunk.insert(value)

    return chunk.getNumbers()
                      
def main():
    

    #very basic test
    size = 50000
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
if __name__ == "__main__":
    main()
