
def LCS(str1, str2, curr1, curr2, dict1):
    """
    Returns the length of lcs between str1 and str2.

    :param str1: input string1
    :param str2: input string2
    :param curr1: current index we are on str1
    :param curr2: current index we are on str2
    :dict1: dictionary to mantain DP

    V.I => while calling, curr1 and curr2 will be set equal to last index of str1 and str2 respectively. 
    """
    # DP
    key = f'({curr1},{curr2})'
    if dict1.get(key):
        return dict1.get(key)

    # Base Condition
    if curr1 < 0 or curr2 < 0:  # it means koi ek string khatam ho gai, then LCS('empty string', anystring) = 0
        return 0

    ans = 0
    if str1[curr1] == str2[curr2]:
        ans = 1 + LCS(str1, str2, curr1-1, curr2-1, dict1)  
    else:
        unmatch_1 = 0 + LCS(str1, str2, curr1-1, curr2, dict1)
        unmatch_2 = 0 + LCS(str1, str2, curr1, curr2-1, dict1)
        ans = max(unmatch_1, unmatch_2)

    dict1.update({f'{curr1},{curr2}': ans})
    return ans


def length_of_longest_palindromic_subsequence_in_a_string(str1):
    """
    Returns the length of the longest palindromic sequence in a string.
    
    :param str1: The string

    ans = LCS(str1, str1[::-1])
    """
    pass


# TO-DO
def edit_distance(str1, str2, curr1, curr2, dict1):
    """
    """
    # DP
    key = f'({curr1}, {curr2})'
    if dict1.get(key):
        return dict1.get(key)
    
    # Base Condition 
    if curr1 < 0:
        return curr2 + 1
    if curr2 < 0:
        return curr1 + 1
    
    ans = 0
    if str1[curr1] == str2[curr2]:
        ans =  edit_distance(str1, str2, curr1-1, curr2-1, dict1)
    else:
        # insert
        insert_ans = 1 + edit_distance(str1, str2, curr1, curr2-1, dict1)
        # replace
        replace_ans = 1 + edit_distance(str1, str2, curr1-1, curr2-1, dict1)
        #delete
        delete_ans = 1 + edit_distance(str1, str2, curr1-1, curr2, dict1)
        ans = min(insert_ans, replace_ans, delete_ans)
    
    dict1.update({f'({curr1}, {curr2})': ans})
    return ans

