list_of_all = [1,2,3,4,1,5,1,3,2,4,2,1,"hi","good","well","hi",1]
new_list = []
for ele in list_of_all:
    if ele not in new_list:
        new_list.append(ele)
print(new_list)
# print(set(list_of_all)) #but unordered

