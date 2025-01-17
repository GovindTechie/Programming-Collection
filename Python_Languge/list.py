# List Operations
def list_operations():
    my_list = [5, 2, 9, 1]
    print("Original List:", my_list)
    
    # Sorting
    my_list.sort()
    print("Sorted List:", my_list)
    
    # Appending
    my_list.append(10)
    print("List after appending 10:", my_list)
    
    # Merging
    another_list = [8, 7]
    merged_list = my_list + another_list
    print("Merged List:", merged_list)
    
    # Searching
    element_index = my_list.index(2) if 2 in my_list else -1
    print("Index of element '2':", element_index)

list_operations()