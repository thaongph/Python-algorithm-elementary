# nrows, ncols = map(int, input().split())
# mat = []
# for i in range(nrows):
#     lst_num = list(map(int, input().split()))
#     mat.append(lst_num)

# for i in range(nrows):
#     sum = 0
#     for j in range(ncols):
#         sum += mat[i][j]
#     print(f"{i}: {sum}")


def merge(L, n1, R, n2, a):
    i = j = x = 0
    while i < n1 and j < n2:
        if L[i] < R[j]:
            a[x] = L[i]
            i +=1
        else:
            a[x] = R[j]
            j +=1
        x += 1
    while i < n1:
        a[x] = L[i]
        i += 1
        x +=1
    while j < n2:
        a[x] = R[j]
        j +=1
        x +=1

def mergeSort(a,n):
    if n > 1:
        n1 = n//2
        n2 = n-n1
        L = a[:n1]
        R = a[n1:]
        mergeSort(L, n1)
        mergeSort(R, n2)
        merge(L, n1, R, n2, a)

m, n, k = map(int, input().split())
lst_m = list(map(int, input().split()))
lst_n = list(map(int, input().split()))
lst = []
for i in range(m+n):
    lst.append(1)
mergeSort(lst_m, m)
mergeSort(lst_n, n)
merge(lst_m, m, lst_n, n, lst)
print(lst[k])