#for-else
names = ["pushpa","srivalli","keshava","pavani","mangalam seenu"]
for i in range(len(names)):
    if names[i] == "pavani":
        print(i)
        break
else:
    print("Not found")

#enumerate
for idx,name in enumerate(names):
    if name == "pavani":
        print(idx)
        break
else:
    print("Not found")

#flag variable approach
found = False
for idx,name in enumerate(names):
    if name == "pavan":
        print(idx)
        found = True
        break
if not found:
    print("Not found")

#using .index()
target = "pavan"
if target in names:
    print(names.index(target))
else:
    print("Not found")
