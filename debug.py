def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
 
    for record_id in record_ids[:]:
     if record_id % 2 != 0:
      record_ids.remove(record_id)
    return data
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [ 4, 6, 10]

# Adding a slicer in line 4 creates a copy of the code therefore preventing the skipping of numbers as the code is running







# def clean_database(record_ids):
#     # Create a new list with only even numbers
#     return [record_id for record_id in record_ids if record_id % 2 == 0]

# # Test Case
# data = [1, 3, 4, 6, 7, 9, 10]
# cleaned = clean_database(data)
# print(f"Final List: {cleaned}")
# # OUTPUT: [4, 6, 10]


# def clean_database(record_ids):
#     for record_id in reversed(record_ids):
#         if record_id % 2 != 0:
#             record_ids.remove(record_id)
#     return record_ids
