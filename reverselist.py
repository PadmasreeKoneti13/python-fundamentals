list1 = [6,6,4,8,4,1,2,3,9,75,5]
first = 0
last = len(list1)-1
while first<last:
    list1[first], list1[last] = list1[last], list1[first]
    first += 1
    last -= 1
print(list1)

#maximum optimal manual approach
list1 = [6,6,4,8,4,1,2,3,9,75,5]
for i in range(len(list1)//2):
    list1[i],list1[len(list1)-i-1] = list1[len(list1)-i-1],list1[i]
print(list1)

#with in-built function
list2 = [6,6,4,8,4,1,2,3,9,75,5]
list2.reverse()#or new_list =list(reversed(list2)) and print(new_list)
print(list2)
#or slicing
list2 = [6,6,4,8,4,1,2,3,9,75,5]
print(list2[::-1])

