
def fun1(s1, s2, i1, i2):
    """
    LCS
    """
    # BASE CONDITION
    if (i1<0 or i2<0):
        return 0

    if s1[i1] == s2[i2]:
        ans1 = 1 + fun1(s1, s2, i1-1, i2-1)
    else:
        ans1 = max(
            fun1(s1, s2, i1-1, i2),
            fun1(s1, s2, i1, i2-1),
        )

    return ans1


def fun2(s1, s2, i1, i2):
    """
    Print LCS
    """
    # BASE CONDITION
    if (i1<0 or i2<0):
        return ""

    if s1[i1] == s2[i2]:
        ans1 = fun2(s1, s2, i1-1, i2-1) + s1[i1]
    else:
        ans2 = fun2(s1, s2, i1-1, i2)
        ans3 = fun2(s1, s2, i1, i2-1)
        if len(ans2) >= len(ans3):
            ans1 = ans2
        else:
            ans1 = ans3
    return ans1


def fun3(s1, s2, i1, i2):
    """
    Print Shortest common supersequence 
    """
    # BASE CONDITION
    if (i1<0 or i2<0):
        if i1<0:
            return s2[:i2+1]
        if i2<0:
            return s1[:i1+1]

    if s1[i1] == s2[i2]:
        ans1 = fun3(s1, s2, i1-1, i2-1) + s1[i1]
    else:
        ans2 = fun3(s1, s2, i1-1, i2) + s1[i1]
        ans3 = fun3(s1, s2, i1, i2-1) + s2[i2]
        if len(ans2) < len(ans3):
            ans1 = ans2
        else:
            ans1 = ans3
    return ans1



s1 = 'aggtab'
s2 = 'gxtxayb'
i1 = len(s1)-1
i2 = len(s2)-1

a = fun3(s1, s2, i1, i2)

print(a)