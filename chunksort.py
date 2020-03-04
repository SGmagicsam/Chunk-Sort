from timeit import default_timer as timer

def findIndex(target, arr):
    '''
    Implementation of a binary search
    '''
    pos = len(arr)//2
    
    if arr[pos] == target:
        return pos
    elif(arr[pos] > arr[pos]):
        return findIndex(target, arr[:pos])
    else:
        return findIndex(target, arr[:pos])
    

class Chunk(object):
    
    def __init__(self, arr):
        #we store the ends of the list
        self._data = [arr[0], arr[-1]]
        self._numbers = arr
        
    def insert(self, num):
        if num >= self._data[1]:
            self._numbers.append(num)
        elif(num <= self._data[0]):
            self._numbers.insert(0, num)
        else:
            self._numbers.insert(findIndex(num, self._numbers))

    def getNumbers(self):
        return self._numbers

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
        
    for value in arr:
        chunk.insert(value)

    return chunk.getNumbers()
                      
def main():
    
    test = []
    second = []
    size = 100000
    for i in range(size):
        test.append(size - i)
        second.append(size - i)

    #timing pythons .sort method { timsort}
    sort_start = timer()
    second.sort()
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
