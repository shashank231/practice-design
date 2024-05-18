from typing import List

# Normal Binary Search
def binary_search(arr: List[int], target: int) -> int:    
    low  = 0
    high = len(arr) - 1

    while(low <= high):
        mid = low + (high-low)//2        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1   


def findPeakElement(arr: List[int]) -> int:
        """
        This array is constantly incrasing then constantly decreasing.
        """
        if len(arr) == 1:
            return 0

        low        = 0
        high       = len(arr)-1 
        last_index = len(arr)-1

        while (low <= high):            
            mid = low + (high-low)//2

            if mid > 0 and mid < last_index:                            # first index or last index ke mid me
                if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:     # checking for peak
                    return mid
                elif arr[mid-1] > arr[mid]:
                    high = mid-1
                else:
                    low = mid+1

            elif mid==0:  # first index 
                if arr[0] > arr[1]:
                    return 0
                else:
                    return 1

            elif mid==last_index:  # last index
                if arr[mid] > arr[mid-1]:
                    return (last_index)
                else:
                    return (last_index-1)
        
        return -1


# Square Root Using Binary Search
def square_root_using_binary_search(num: int) -> int:
    """
    logic simple, hai 
    - mid ka sqare check kar
    - barabar to return
    - chota hai to, left=mid+1
    - bada hai to, right=mid-1
    """
    left  = 0
    right = num

    while (left <= right):
        mid    = left + (right-left)//2
        mid_sq = mid*mid

        if mid_sq==num:
            return mid
        elif mid_sq > num:
            right = mid-1
        else:
            left = mid+1

    return right


# Book Allocation Problem
def minimize_max_pages(arr: List[int], students_count: int):

    def is_possible(arr, mid, students_count):
        max_pages       = mid
        pages_read      = 0
        students_needed = 0

        for i in arr:
            if i>max_pages: # not possible that this is the max pages read by a student
                return False
            if pages_read+arr[i] > max_pages:
                students_needed += 1  # now we need  a new student
                pages_read = arr[i]   # these pages, now his count of pages read 
            else:
                pages_read += arr[i]  # ongoing student can read this also 

        return students_needed <= students_count

    len_arr = len(arr)
    if len_arr < students_count:  # now each student can't get 1 book
        return -1
    
    low    = max(arr)  # minimum ek student ke pass jitni book(pages) ja sakte hain 
    high   = sum(arr)  # max ek student ke pass jitni book(pages) ja sakte hain 
    result = -1

    while(low <= high):
        mid = low + (high-low)//2
        if is_possible(arr, mid, students_count):
            """
            "mid" result hai ya nahi, vo "is_possible" set karta hai, 
            "is_possible" arr ke instances par he answer based hot hai,
            tabhi result is a sum of consecutive array instances, 
            as "is_possible" is designed like THIS!!!
            """
            result = mid
            high   = mid-1
        else:
            low = mid+1

    return result


# Aggressive Cows
def aggressive_cows(arr: List[int], numOfCows: int):
    # arr is sorted
    def is_possible(arr, mid, numOfCows):
        placedCows        = 0
        maxMinDistance    = mid
        lastStallPosition = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - arr[lastStallPosition] >= maxMinDistance:
                placedCows += 1
                lastStallPosition = arr[i]
                if placedCows == numOfCows:
                    return True
        return False

    numOfStalls = len(arr)
    if numOfCows > numOfStalls:
        return -1

    low    = 1
    high   = arr[-1] - arr[0]
    result = -1

    while (low <= high):
        mid = low + (high-low)//2
        if is_possible(arr, mid, numOfCows):
            result = mid
            low    = mid+1
        else:
            high = mid-1

    return result

