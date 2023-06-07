n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
left = 0
right = n-1
answer = abs(arr[left] + arr[right])
res = [arr[left], arr[right]]

while left < right:
    start = arr[left]
    end = arr[right]
    sum = start + end
  
    if abs(sum) < answer:
        answer = abs(sum)
        res = [start, end]
        if answer == 0:
          break

    if sum < 0:
        left += 1
    else:
        right -= 1
print(res[0], res[1])