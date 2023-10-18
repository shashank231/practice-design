from typing import List

def list_of_closest_max_ele_to_right(arr: List[int]) -> List[int]:
    """
    Returns an array that contains the closest maximum or equal element to the right for each element,
    if there is no such element, append -1.

    :param arr: input list of integers
    :returns: an array that contains the closest maximum element to the right for each element.
    """
    last_index = len(arr)-1
    ans = [-1] * len(arr)
    stack = []
    stack.append(arr[last_index])
    
    for index in range(last_index-1, -1, -1):
        
        if stack[-1] > arr[index]:
            ans[index] = stack[-1]
        else:
            while(len(stack)):
                if (stack[-1] > arr[index]):
                    ans[index] = stack[-1]   
                    break
                else:
                    stack.pop()

        stack.append(arr[index])

    return ans



def buy_stock2(arr, last_index, curr_index, buy, dict1):
    """
    :param arr: list of stock prices, always same
    :param last_index: list of stock prices, always same
    :curr_index: current index
    :buy: boolean state, 
          if True: can buy
             False: can't buy
    :dict1: dict to mantain dp
    """

    # Check in dict1, for DP
    key = f'curr_index:{curr_index}, buy:{buy}'
    if dict1.get(key):
        return dict1.get(key)
    
    # Base Condition
    if curr_index == last_index:
        return 0


    profit = 0

    if (buy):
        buy_karo = -arr[curr_index] + buy_stock2(arr, last_index, curr_index+1, 0, dict1)
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 1, dict1)
        profit = max(buy_karo, skip_karo)
    else:
        sell_karo = arr[curr_index] + buy_stock2(arr, last_index, curr_index+1, 1, dict1)
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 0, dict1)
        profit = max(sell_karo, skip_karo)
    
    # set dict1 for DP
    new_key = f'curr_index:{curr_index}, buy:{buy}'
    dict1.update({new_key: profit})
    
    return profit

def buy_stock5(arr, last_index, curr_index, buy, fee, dict1):
    """
    :param arr: list of stock prices, always same
    :param last_index: list of stock prices, always same
    :curr_index: current index
    :buy: boolean state, 
          if True: can buy
             False: can't buy
    :fee: fees for every transaction
    :dict1: dict to mantain dp

    V.I => See there is a very samll change
           as transaction sell pe khatam hoti hai,
           to bus humne vaha ek fees minus kar di..
           ye hum buy pe b kar sakte (kahi b kare par bus ek baar karni hai..)
    """

    # Check in dict1, for DP
    key = f'curr_index:{curr_index}, buy:{buy}'
    if dict1.get(key):
        return dict1.get(key)
    
    # Base Condition
    if curr_index == last_index:
        return 0


    profit = 0

    if (buy):
        buy_karo = -arr[curr_index] + buy_stock2(arr, last_index, curr_index+1, 0, fee, dict1)
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 1, fee, dict1)
        profit = max(buy_karo, skip_karo)
    else:
        sell_karo = arr[curr_index] + (-fee) + buy_stock2(arr, last_index, curr_index+1, 1, fee, dict1)    # transaction per fees subtract kar di
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 0, fee, dict1)
        profit = max(sell_karo, skip_karo)
    
    # set dict1 for DP
    new_key = f'curr_index:{curr_index}, buy:{buy}'
    dict1.update({new_key: profit})
    
    return profit

def buy_stock3_4(arr, last_index, curr_index, buy, limit, dict1):
    """
    :param arr: list of stock prices, always same
    :param last_index: list of stock prices, always same
    :curr_index: current index
    :buy: boolean state, 
          if True: can buy
             False: can't buy
    :limit: number of transactions aloud
    :dict1: dict to mantain dp

    The most Imp point to notice in this code is that, buy_stock_2 and this one is almost same,
    isme ek limit add ho gai hai no. of transactions par, 
    
    V.I => transaction tabhi puri hoti hai stock ki jab vo buy ke bad sell ho jaye
           isliye bus selling ke case me limit changed to limit-1 
    """

    # Check in dict1, for DP
    key = f'curr_index:{curr_index}, buy:{buy}, limit:{limit}'
    if dict1.get(key):
        return dict1.get(key)

    # Base Condition
    if curr_index == last_index:
        return 0

    # Base Condition for limit
    if limit == 0:
        return 0

    profit = 0

    if (buy):
        buy_karo = -arr[curr_index] + buy_stock2(arr, last_index, curr_index+1, 0, limit, dict1)
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 1, limit, dict1)
        profit = max(buy_karo, skip_karo)
    else:
        sell_karo = arr[curr_index] + buy_stock2(arr, last_index, curr_index+1, 1, limit-1, dict1)   # transaction complete, now reduce limit by 1 
        skip_karo = 0 + buy_stock2(arr, last_index, curr_index+1, 0, limit, dict1)
        profit = max(sell_karo, skip_karo)
    
    # set dict1 for DP
    new_key = f'curr_index:{curr_index}, buy:{buy}'
    dict1.update({new_key: profit})
    
    return profit



def max_area_square_in_matrix(mat, lx, ly, cx, cy, dict1, var_ref):
    """
    
    :param mat: matrix,
    :param lx: length of the mat,
    :param ly: length of the mat[0],
    :param cx: current index of x,
    :param cy: current index of y,
    :param dict1: dictionary for DP,
    :var_ref: [0] to pass integer as reference

    """
    # DP
    key = f'({cx}, {cy})'
    if dict1.get(key):
        return dict1.get(key)
    
    # Base Case
    if (cx > (lx-1)) or (cy > (ly-1)):
        return 0
    
    # Choice diagram
    right   = max_area_square_in_matrix(mat, lx, ly, cx, cy+1, dict1, var_ref)
    diagnol = max_area_square_in_matrix(mat, lx, ly, cx+1, cy+1, dict1, var_ref)
    down    = max_area_square_in_matrix(mat, lx, ly, cx+1, cy, dict1, var_ref)

    ans = 0
    if mat[cx][cy] == 1:
        ans = 1 + min(right, diagnol, down)
        var_ref[0] = max(var_ref[0], ans)
    else:
        ans = 0
    
    dict1.update({f'({cx}, {cy})': ans})
    return ans

def max_area_square(mat):
    lx = len(mat)
    ly = len(mat[0])
    dict1 = {}
    var_ref = [0]
    max_area_square_in_matrix(mat, lx, ly, 0, 0, dict1, var_ref)

    length = var_ref[0]
    return length*length



def length_of_longest_increasing_subsequence(arr):
    lenArr = len(arr)
    trackArr = [1]*lenArr

    for index in range(1, lenArr):
        maxa = 1
        for j in range(index):
            if arr[index] > arr[j]:
                maxa = max(trackArr[j]+1, maxa)
        trackArr[index] = maxa

    return max(trackArr)