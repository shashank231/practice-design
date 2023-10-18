
def solve(index, diff, arr, dict1):
    key = f'({index}, {diff})'
    if dict1.get(key):
        return dict1.get(key)

    if index < 0:
        return 0

    maxAns = 0
    for j in range(index-1, -1, -1):
        if arr[index] - arr[j] == diff:
            ans = 1 + solve(j, diff, arr, dict1)
            maxAns = max(maxAns, ans)
    
    dict1.update({f'({index}, {diff})': maxAns})
    return maxAns

def len_of_longest_AP(arr, n):
    if (n <= 2):
        return n 
    
    maxLen = 0
    dict1 = {}

    for i in range(n):
        for j in range(i+1, n):
            common_diff = arr[j] - arr[i]
            ans = 2 + solve(i, common_diff, arr, dict1)
            maxLen = max(maxLen, ans)
    
    return maxLen



def subset_sum2(arr, lenArr, index, target, dict1):

    # Base case
    if (index >= lenArr):
        return 0
    if (target < 0):
        return 0
    if (target == 0):
        return True
    
    # DP
    key = f'({index}, {target})'
    if dict1.get(key):
        return dict1.get(key)
    
    bool_inc = subset_sum2(arr, lenArr, index+1, target - arr[index], dict1)
    bool_exc = subset_sum2(arr, lenArr, index+1, target - 0, dict1)
    ans = bool_inc or bool_exc
    dict1.update({key: ans})
    return ans

def partition_half2(arr):
    sumArr = sum(arr)
    if sumArr % 2 == 0:
        halfSumArr = sumArr//2
        bool1 = subset_sum2(arr, len(arr), 0, halfSumArr, {})
        return bool1
    else:
        return False



def max_to_right_fun(arr):
    lenArr = len(arr)
    lastIndex = lenArr - 1
    ansArr = [-1] * lenArr
    maxEle = arr[lastIndex]

    for index in range(lastIndex-1, -1, -1):
        if arr[index] < maxEle:
            ansArr[index] = maxEle
        else:
            maxEle = arr[index]
    
    return ansArr

def max_to_left_fun(arr):
    lenArr = len(arr)
    startIndex = 0
    ansArr = [-1] * lenArr
    maxEle = arr[startIndex]

    for index in range(startIndex+1, lenArr):
        if arr[index] < maxEle:
            ansArr[index] = maxEle
        else:
            maxEle = arr[index]
    
    return ansArr

def rain_water_trapping(arr):
    max_to_right = max_to_right_fun(arr)
    max_to_left = max_to_left_fun(arr)
    print(max_to_left, max_to_right)
    trappedWater = 0

    for i in range(len(arr)):
        if max_to_left[i] == -1 or max_to_right[i] == -1:
            trappedWater += 0
        else:
            height_water_can_go_upto_on_this_index = min(max_to_left[i], max_to_right[i])
            area = 1 * (height_water_can_go_upto_on_this_index-arr[i])
            trappedWater += area
    
    return trappedWater







