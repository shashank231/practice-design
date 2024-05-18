# Divide and conquer
# Max sum of a subarray (https://www.techiedelight.com/maximum-sum-subarray-using-divide-conquer/#)
arr = [2, -4, 1, 9, -6, 7, -3]

def fun1_1(arr):
    # this approach uses Kadene's Algorithm
    meh = 0  # max ending here
    msf = float('-inf')  # max so far

    for i in range(len(arr)):
        meh = meh + arr[i]
        if arr[i] > meh:
            meh = arr[i]
        if meh > msf:
            msf = meh

    return msf


def fun1_2(arr, left, right):
    # All base cases
    if not arr:
        return 0
    if left is None and right is None:
        left, right = 0, len(arr) - 1
    # If the list contains 0 or 1 element
    if right == left:
        return arr[left]

    mid = (left + right)//2
    # Find maximum sublist sum for the left sublist, INCLUDING the middle element
    leftMax = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > leftMax:
            leftMax = total
    # Find maximum sublist sum for the right sublist, EXCLUDING the middle element
    rightMax = float('-inf')
    total = 0 
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > rightMax:
            rightMax = total
    # Recursively find the maximum sublist sum for the left and right sublist, and take maximum
    maxLeftRight = max(fun1_2(arr, left, mid), fun1_2(arr, mid + 1, right))
    return max(maxLeftRight, leftMax + rightMax)


# Find smallest missing element in a sorted list in logarithmic time
"""
 smallest missing number would be the element’s index, which is not equal to its element
 We can easily solve this problem in O(log(n)) time by modifying the binary search algorithm.
 The idea is to compare the mid-index with the middle element.
 If both are the same, then the mismatch is in the right subarray; otherwise, it lies in the left subarray
"""
def fun2_1(nums, left=None, right=None):
    # base condition
    if left > right:
        return left
 
    mid = left + (right - left) // 2
    # if the mid-index matches with its value, then the mismatch lies on the right half
    if nums[mid] == mid:
        return fun2_1(nums, mid + 1, right)
    # mismatch lies on the left half
    else:
        return fun2_1(nums, left, mid - 1)


