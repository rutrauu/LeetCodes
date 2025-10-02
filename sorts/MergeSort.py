def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.

    It is a divide-and-conquer algorithm. It divides the unsorted list into
    n sublists, each containing one element (a list of one element is
    considered sorted). Then it repeatedly merges sublists to produce new
    sorted sublists until there is only one sublist remaining.

    Args:
        arr: A list of numbers.

    Returns:
        A new list containing the sorted elements.
    """
    new_arr = arr[:]
    
    if len(new_arr) > 1:
        mid = len(new_arr) // 2  # Finding the mid of the array
        left_half = new_arr[:mid]   # Dividing the array elements
        right_half = new_arr[mid:]  # into 2 halves

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                new_arr[k] = left_half[i]
                i += 1
            else:
                new_arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            new_arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            new_arr[k] = right_half[j]
            j += 1
            k += 1
            
    return new_arr

sample_list = [64, 25, 12, 22, 11, 90, 34, 7, 1]
print(f"Original list: {sample_list}\n")

sorted_list = merge_sort(sample_list)
print(f"Selection Sort: {sorted_list}")