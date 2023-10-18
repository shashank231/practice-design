

def list_of_index_of_closest_min_ele_to_right(arr):
    last_index = len(arr) - 1
    ans = [-1] * len(arr)
    stack = []
    stack.append(last_index)

    for index in range(last_index-1, -1, -1):
        if arr[stack[-1]] < arr[index]:
            ans[index] = stack[-1]
        else:
            while(stack):
                if arr[stack[-1]] < arr[index]:
                    ans[index] = stack[-1]
                    break
                else:
                    stack.pop()
        stack.append(index)
    
    return ans

def list_of_index_of_closest_min_ele_to_left(arr):
    start_index = 0
    ans = [-1] * len(arr)
    stack = []
    stack.append(start_index)

    for index in range(start_index+1, len(arr)):
        if arr[stack[-1]] < arr[index]:
            ans[index] = stack[-1]
        else:
            while(stack):
                if arr[stack[-1]] < arr[index]:
                    ans[index] = stack[-1]
                    break
                else:
                    stack.pop()
        stack.append(index)
    
    return ans

def max_rectangular_area_in_histogram(arr):
    left = list_of_index_of_closest_min_ele_to_left(arr)
    right = list_of_index_of_closest_min_ele_to_right(arr)
    lenArr = len(arr)
    right = [lenArr if (i==-1) else i for i in right]

    maxArea = float("-inf")
    for index in range(lenArr):
        height = arr[index]
        length = (right[index] - left[index]) - 1
        area = length * height
        maxArea = max(maxArea, area)

    return maxArea

def max_Area_rectangle_in_a_matrix(matrix):
    maxArea = float('-inf')
    lenRow = len(matrix[0])
    initialHistogram = [0]*lenRow

    for row in matrix:
        for i in range(lenRow):
            if row[i] == 0:
                initialHistogram[i] = 0
            else:
                initialHistogram[i] = initialHistogram[i] + 1    
        # initialHistogram => now ready for this iteration
        area = max_rectangular_area_in_histogram(initialHistogram)
        maxArea = max(area, maxArea)

    return maxArea
