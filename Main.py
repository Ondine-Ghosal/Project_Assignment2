def search(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow

        if numbers[mid] == target:
            return mid  # Target found, return index
        elif numbers[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    return -1  # Target not found

# Example usage
numbers = [-1, 0, 2, 4, 6, 8]
if search(numbers, 4):
    print(3)
elif search(numbers, 3):
    print(-1)  # Output: -1

