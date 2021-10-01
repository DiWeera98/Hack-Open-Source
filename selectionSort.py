def selection_sort(array):
    array_length = len(array)
    
    #Traverse through all array elements
    for i in range(0, array_length - 1):
        min_element = i
        #Traverse through the unchecked elements
        for j in range(i + 1, array_length):
            if array[j] < array[min_element]:
                min_element = j
        #Swap elements
        if min_element != i:
            array[min_element], array[i] = (array[i], array[min_element])
    return array

#Driver code
if __name__ == "__main__":
    raw_array = list(map(int, input("Enter space separated elements").split()))
    sorted_array = selection_sort(raw_array)
    print ("Sorted array is:")
    for i in range(len(sorted_array)):
        print ("% d" % sorted_array[i])
