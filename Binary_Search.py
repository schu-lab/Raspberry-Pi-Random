# Function to perform binary search
def binary_search(nums, x):

    # Initialize 'low' and 'high'
    low = 0
    high = len(nums) - 1

    # loop will run until low becomes greater than high
    while low <= high:
        mid = (low + high) // 2

        # Check if x is present at mid
        if nums[mid] == x:
            return mid
        
        # If x is greater, ignore left half
        elif nums[mid] < x:
            high = mid - 1
        
        # If x is smaller, ignore right half
        else:
            low = mid + 1
    
    # If we reach here, then the element was not present
    return -1

# Test Array
nums = [1, 20, 300, 40, 500, 60, 700, 80, 900, 10]
x = 80

# Function Call
result = binary_search(nums, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
