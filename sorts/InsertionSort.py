def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.

    It builds the final sorted array one item at a time. It iterates through
    the input elements and inserts each element into its correct position in
    the sorted part of the array.

    Args:
        arr: A list of numbers.

    Returns:
        A new list containing the sorted elements.
    """
    # Create a copy to avoid modifying the original list
    new_arr = arr[:]
    n = len(new_arr)

    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = new_arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < new_arr[j]:
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = key

    return new_arr

sample_list = [64, 25, 12, 22, 11, 90, 34, 7, 1]
print(f"Original list: {sample_list}\n")

sorted_list = insertion_sort(sample_list)
print(f"Selection Sort: {sorted_list}")