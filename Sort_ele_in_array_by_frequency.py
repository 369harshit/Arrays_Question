arr=[5,1,1,2,2,3,1,2,3,4,5,5,5,5,5,5,5,5,1,4]
arr_unique=list(set(arr))
arr_unique.sort(key=arr.count)
print(arr_unique)
