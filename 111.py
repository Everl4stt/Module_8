list1 = list(range(64))
list4 = list(range(64))
middle = int(len(list1)/2) + 1
list2 = [list1[i] for i in range(len(list1)//2)]
print(list1)
print(list2)
list3 = list1 + list2
print(list3)

def XOR(list1, list2):
    return [(False if list1[i] == list2[i] else True) for i in range(len(list1))]

print(XOR(list1, list4))
for i in range(len(list1)):
    print(next(list1[i] ^ list4[i] for i in range(len(list1))))


w