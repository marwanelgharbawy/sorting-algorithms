def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

def selection_sort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)): # Loop to identify smallest number
            if array[j] < array[min]:
                min = j 
        array[i], array[min] = array[min], array[i] # For each pass, smallest element will be at the start
    return array

def insertion_sort(array):
    for i in range(1, len(array)):  # Assuming first element is sorted
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:  # array[i] is the element to be inserted
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array
    
    
# TODO: Generate random array
array = [6, 4, 33, 54, 20, 10, 1, 50, 5, 70, 3, 2]

print(array)

array_bubble = bubble_sort(array)
print(array_bubble)

array_select = selection_sort(array)
print(array_select)

array_insert = insertion_sort(array)
print(array_insert)
