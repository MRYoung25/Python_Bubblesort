data = [1, 3, 4, 6, 8, 7, 2, 5, 10, 11, 9, 13, 12]
def BubbleSort(L):
    length = len(L)
    if length == 0 or length == 1:
        return L

    for i in range(length):
        for j in range(length-1):
            if L[j] < L[j+1]:
                (L[j+1], L[j]) = (L[j], L[j+1])
    return L
pass

print BubbleSort(data)
