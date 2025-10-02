def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    It is a divide-and-conquer algorithm. It picks an element as a pivot and
    partitions the given array around the picked pivot.

    Args:
        arr: A list of numbers.

    Returns:
        A new list containing the sorted elements.
    """
    new_arr = arr[:]
    
    # This is a wrapper function to start the recursion
    def _quick_sort_recursive(items, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now at right place
            pi = _partition(items, low, high)

            # Separately sort elements before partition and after partition
            _quick_sort_recursive(items, low, pi - 1)
            _quick_sort_recursive(items, pi + 1, high)

    def _partition(items, low, high):
        # pivot (Element to be placed at right position)
        pivot = items[high]
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if items[j] <= pivot:
                i = i + 1
                items[i], items[j] = items[j], items[i]

        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1
        
    _quick_sort_recursive(new_arr, 0, len(new_arr) - 1)
    return new_arr

sample_list = [64, 25, 12, 22, 11, 90, 34, 7, 1]
print(f"Original list: {sample_list}\n")

sorted_list = quick_sort(sample_list)
print(f"Quick Sort: {sorted_list}")