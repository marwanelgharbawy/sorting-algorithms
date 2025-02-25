def bubble_sort(array):
    for i in range(len(array)):
        # sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                # sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
        # if not sorted:
        #     break
    
    return array

def selection_sort(array):
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)): # Loop to identify smallest number
            if array[j] < array[min]:
                min = j 
        array[i], array[min] = array[min], array[i] # For each pass, smallest element will be at the start
    return array
    

# TODO: Generate random array
array = [6, 4, 33, 54, 20, 10, 1, 50, 5, 70, 3, 2]

print(array)

array_bubble = bubble_sort(array)
print(array_bubble)

array_select = selection_sort(array)
print(array_select)
