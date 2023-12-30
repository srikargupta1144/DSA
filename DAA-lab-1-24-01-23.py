
def insertionSort(array):
    for step in range(1,len(array)):
        key = array[step]
        j =step -1
        
        while j>= 0 and key < array[j]:
            array[j + 1] = array[j]
            j =j -1 
            
        array[j + 1] = key 
        
data = [9,5,1,4,3]
insertionSort(data)
print('Sorted array in Ascending order : ')
print(data)

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1
list1 = [5,3,8,6,7,2]
print('The unsorted list is :',list1)
# Calling the bubble sort function
print("The sorted list is : ",bubble_sort(list1))

def selcetionSort(array, size):
    for step in range(size):
        min_idx =step
        
        for i in range(step + 1,size):
            
            if array[i] < array[min_idx]:
                min_idx = i
                
        (array[step], array[min_idx]) = (array[min_idx],array[step])
data = [-2,45,0,11,-9]
size = len(data)
selcetionSort(data, size)
print('Sorted Array in Ascending Order : ')
print(data)

