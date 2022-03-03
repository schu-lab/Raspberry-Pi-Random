# Iterative Binary Search Function
# Returns index of x in a given array 'nums' if present, else -1

# Function to perform binary search
def binary_search(nums, target):

    # Initialize 'low' and 'high'
    low = 0
    high = len(nums) - 1

    # loop will run until low becomes greater than high
    while low <= high:
        mid = (low + high) // 2

        # Check if target is present at mid
        if nums[mid] == target:
            return mid
        
        # If target is greater, ignore lower half
        elif nums[mid] > target:
            high = mid - 1
        
        # If target is smaller, ignore upper half
        else:
            low = mid + 1
    
    # If we reach here, then the element was not present
    return -1

# Test Array
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

# Function Call
result = binary_search(nums, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
