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
        print(">> Target:", target, "Mid:", nums[mid])

        # Check if target is present at mid
        if nums[mid] == target:
            print(">> Target found at index:", mid)
            print(">>     High: ", high, "Mid: ", mid, "Low: ", low)
            return mid
        
        # If target is greater, ignore lower half
        elif nums[mid] > target:
            print(">> Target (", target, ")", "is less than mid: (", nums[mid], ")")
            high = mid - 1
            print(">>     High: ", high, "Mid: ", mid, "Low: ", low)
        
        # If target is lower, ignore upper half
        else:
            print(">> Target (", target, ")", "is greater than mid: (", nums[mid], ")")
            low = mid + 1
            print(">>     High: ", high, "Mid: ", mid, "Low: ", low)
    
    # If we reach here, then the element was not present
    return -1

# Test Array
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1

# Function Call
result = binary_search(nums, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
