def remove_duplicates(original_list):
    seen = set()
    result = []

    for item in original_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original_list = (input("Enter Elements separated by space:").split())

new_list = remove_duplicates(original_list)

print("Original List:",original_list)
print("List after removing duplicates:",new_list)
