

mylist = []
mylist.append('list0')
mylist.append('list1')

print(mylist)
print(mylist[1])

mytuple = (1,2,[3,4])
print(mytuple[2])
mytuple[2][1] = 5
print(mytuple[2])

mydic = {}
mydic['key1'] = 'value1'
mydic['key2'] = 'value2'
mydic[3] = 'value3'
print(mydic)
print(mydic['key1'])
print(mydic[3])
print(5 in mydic)

myset = set()
myset.add(1)
myset.add(2)
list1 = [1,2,3,4,5]
set1 = (2,3,4,5,6)

print(myset.union(list1))
print(myset.difference(list1))
# myset.difference(list1)
print(myset.union(set1))
print(myset)
