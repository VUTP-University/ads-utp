"""
This module demonstrates the basic usage of Python dictionaries, including creation, access,
modification, and deletion of key-value pairs.

"""

def create_dictionary():
    """Create and return a sample dictionary."""
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
    return sample_dict


def iter_dictionary(d):
    """Iterate through the dictionary and print key-value pairs."""
    for key, value in d.items():
        print(f"{key}: {value}")
        
        
def modify_dictionary(d, key, value):
    """Modify the value of a given key in the dictionary."""
    if key in d:
        d[key] = value
        print(f"Updated {key} to {value}")
    else:
        print(f"Key {key} not found in dictionary.")
        

def delete_key(d, key):
    """Delete a key-value pair from the dictionary."""
    if key in d:
        del d[key]
        print(f"Deleted key {key}")
    else:
        print(f"Key {key} not found in dictionary.")
        

def get_dict_keys(d):
    """Return the keys of the dictionary."""
    return list(d.keys())


def get_dict_values(d):
    """Return the values of the dictionary."""
    return list(d.values())


def dict_remove_pair(d):
    """Remove a key-value pair by value."""
    value_to_remove = 'New York'
    keys_to_remove = [key for key, value in d.items() if value == value_to_remove]
    
    for key in keys_to_remove:
        del d[key]
        print(f"Removed key {key} with value {value_to_remove}")
        

def dict_remove_value(d, value):
    """Remove a value from the dictionary."""
    if value in d.values():
        d.pop(value)
    raise ValueError(f"Value {value} not found in dictionary.")


def dict_remove_last_pair(d):
    """Remove the last key-value pair from the dictionary."""
    if d:
        key, value = d.popitem()
        print(f"Removed last pair: {key}: {value}")
    else:
        print("Dictionary is empty.")
        
    
def dic_create_new_pair(d, key, value):
    """Create a new key-value pair in the dictionary."""
    d[key] = value
    print(f"Added new pair: {key}: {value}")
    
    
def dict_clear_all(d):
    """Clear all key-value pairs from the dictionary."""
    d.clear()
    print("Cleared all key-value pairs from the dictionary.")
    
    
# Example usage
if __name__ == "__main__":
    my_dict = create_dictionary()
    print("Initial Dictionary:")
    iter_dictionary(my_dict)
    
    modify_dictionary(my_dict, 'age', 31)
    print("\nAfter Modification:")
    iter_dictionary(my_dict)
    
    delete_key(my_dict, 'city')
    print("\nAfter Deletion:")
    iter_dictionary(my_dict)
    
    print("\nKeys:", get_dict_keys(my_dict))
    print("Values:", get_dict_values(my_dict))
    
    dic_create_new_pair(my_dict, 'country', 'USA')
    print("\nAfter Adding New Pair:")
    iter_dictionary(my_dict)
    
    dict_remove_last_pair(my_dict)
    print("\nAfter Removing Last Pair:")
    iter_dictionary(my_dict)
    
    dict_clear_all(my_dict)
    print("\nAfter Clearing All Pairs:")
    iter_dictionary(my_dict)