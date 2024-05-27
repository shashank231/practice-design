
# Print all balanced parenthesis combinations
def solve_balanced_parenthesis(n):

    def valid_parenthesis(ip: str) -> bool:
        lst1 = [i for i in ip]
        track = 0
        for i in lst1:
            if i=="(":
                track += 1
            if i==")":
                track -= 1
            if track < 0:
                return False
        return True

    def balanced_parenthesis(a, b, ans):
        if a == 0 and b == 0:
            if valid_parenthesis(ans):
                print(ans)

        if a > 0:
            new_ans = ans + "("
            balanced_parenthesis(a-1, b, new_ans)
        if b > 0:
            new_ans = ans + ")"
            balanced_parenthesis(a, b-1, new_ans)

    balanced_parenthesis(n, n, "")


def josephus_problem(arr, start, cnt):
    """
    arr = [1, 2, 3, 4, 5]
    cnt = 2
    har step me jo marega use arr se hatate jaenge
    fir jo arr me last bachega uss step ka no. hoga jaha banda khada hota to bach jata
    """
    # BASE CONDITION
    if len(arr) == 1:
        return arr[0]
    

    new_posn = (cnt % len(arr)) - 1  # nayi posn ka index agar 0 se start karta cnt plus karna
    new_posn2 = (new_posn + start) % len(arr) # as last step me 0 se start kia tha, so now adding starting steps
    arr1 = arr[:new_posn2] + arr[new_posn2+1:]

    start = new_posn2
    if start > len(arr1)-1:
        start = 0

    return josephus_problem(arr1, start, cnt)

ans = josephus_problem([i for i in range(1, 41)], 0, 7)

print(ans)