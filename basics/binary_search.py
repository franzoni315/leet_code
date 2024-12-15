def binary_search(arr: list, target: int) -> bool:
    """
    Binary search is an efficient algorithm for finding an item from a sorted list of items.

    It works by repeatedly dividing in half the portion of the list that could contain 
    the item until you've narrowed down the possible locations to just one.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 6], 3))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))
    print(binary_search([1, 2, 3, 4, 5, 6], 3.5))
    print(binary_search([1, 2, 3, 4, 5, 6], 7))
    print(binary_search([1, 2, 3, 4, 5, 6], -1))
