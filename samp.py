import math

arr = [10, 13, 17, 9, 34, 21]
first = math.inf
second = math.inf

for i in range(0, len(arr)):
   if arr[i] < first:
     first = arr[i]

for i in range(0, len(arr)):
   if arr[i] != first and arr[i] < second:
     second = arr[i]

print(second)


list1 = [10, 20, 4, 45, 99]
 
mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
        mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))