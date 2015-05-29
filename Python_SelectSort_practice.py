data = [4, 2, 6, 5, 1, 3]
def BubbleSort(L):
    length = len(L)
    if length == 0 or length == 1:
        return L

    for i in range(-1, -length-1, -1):
        j = i - 1
        for j in range(j, -length-1, -1):
            if L[j] < L[i]:
                (L[i], L[j]) = (L[j], L[i])
    return L
pass

print BubbleSort(data)
