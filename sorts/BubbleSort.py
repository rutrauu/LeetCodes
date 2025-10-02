def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    It repeatedly steps through the list, compares adjacent elements and
    swaps them if they are in the wrong order. The pass through the list is

    repeated until the list is sorted.

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
        # Last i elements are already in place, so we don't need to check them
        swapped = False
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return new_arr

sample_list = [64, 25, 12, 22, 11, 90, 34, 7, 1]
print(f"Original list: {sample_list}\n")

sorted_list = bubble_sort(sample_list)
print(f"Selection Sort: {sorted_list}")