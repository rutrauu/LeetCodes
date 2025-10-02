def selection_sort(arr):
    """
    Sorts a list using the Selection Sort algorithm.

    It works by repeatedly finding the minimum element from the unsorted part
    and putting it at the beginning.

    Args:
        arr: A list of numbers.

    Returns:
        A new list containing the sorted elements.
    """
    # Create a copy to avoid modifying the original list
    new_arr = arr[:]
    n = len(new_arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if new_arr[j] < new_arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]

    return new_arr

sample_list = [64, 25, 12, 22, 11, 90, 34, 7, 1]
print(f"Original list: {sample_list}\n")

sorted_list = selection_sort(sample_list)
print(f"Selection Sort: {sorted_list}")