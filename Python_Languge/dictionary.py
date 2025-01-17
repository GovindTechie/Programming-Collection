# Dictionary Operations
def dictionary_operations():
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print("Original Dictionary:", my_dict)
    
    # Adding a new key-value pair
    my_dict['profession'] = 'Engineer'
    print("Dictionary after adding a new key-value pair:", my_dict)
    
    # Accessing value by key
    age = my_dict.get('age', None)
    print("Value of 'age' key:", age)
    
    # Updating a value
    my_dict['age'] = 26
    print("Dictionary after updating 'age':", my_dict)
    
    # Removing a key-value pair
    removed_value = my_dict.pop('city', None)
    print("Dictionary after removing 'city':", my_dict)
    print("Removed value:", removed_value)

dictionary_operations()