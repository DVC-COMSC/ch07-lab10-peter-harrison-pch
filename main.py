# ******************************
# Make your Code
# ******************************
# use nested for loops

def switchem(lst1, index1, index2):
    var2 = lst1.pop(index2)
    var1 = lst1.pop(index1)
    lst1.insert(index1, var2)
    lst1.insert(index2, var1)

lst = input().split()
lst = list(map(int, lst))

const = len(lst)
for i in range(const):
    mini = min(lst[i:])
    minindex = lst.index(mini)
    if minindex != i:
            switchem(lst, i, minindex)
    print(lst)
        
