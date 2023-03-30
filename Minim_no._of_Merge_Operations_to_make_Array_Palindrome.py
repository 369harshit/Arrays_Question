def find(arr):
    ans = 0

    i, j = len(arr) - 1, 0
    while j <= i:
        if arr[j] == arr[i]:
            j += 1
            i -= 1

        elif arr[j] > arr[i]:
            i -= 1
            arr[i] += arr[i + 1]
            ans += 1

        else:
            j += 1
            arr[j] += arr[j - 1]
            ans += 1
    return ans


array = [2, 10, 12, 26, 3, 22, 2]
print("Total number of merging operation required is", find(array))