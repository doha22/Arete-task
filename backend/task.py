def sorting(arr):
    min = 0
    sorted_arr = []
    for i in range(len(arr)):
      if arr[i] > min :
        #   min = arr[i]
        #   sorted_arr.push(arr[i])
          sorted_arr=arr[i]
          print(sorted_arr)
      else :
         min = arr[i]

    
        
    return sorted_arr

print(sorting([1,5,3,0,4,12,6,9,0]))

##########################################################################
def getTime(t):
    return t[:2] + ':' + t[2:]

print(getTime("1230"))

