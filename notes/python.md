
# Python学习笔记

--- 

**Contents**


---

## **各种表**

- list列表

有序集合，类似数组。通过索引号来访问，支持append,pop,insert等方法。list中的元素数据类型可以不同，也可以包含list元素来实现高维数组。
通过中括号[]来初始化。
```
mylist = []
mylist.append('list0')
mylist.append('list1')

print(mylist[1])
```

- tuple元组

有序集合，类似list，初始化后不能修改。所以不能用append,pop等方法。仍可以通过索引号来访问。注意元组不是数对pair，并不一定是只有2个数字（我之前也不知道为什么会有这种印象）。如果tuple中的一个元素是list，那么list中的内容是可以变的。
把tuple理解成final的list就好。
通过括号()以及里面的元素进行初始化。
```
mytuple = (1,2,[3,4])
print(mytuple[2])
mytuple[2][1] = 5
print(mytuple[2])

# print result:
[3, 4]
[3, 5]
```

- dict字典

键值对的集合，就是我们常说的Map，相较于Java中的Map类要指定键和值的数据类型（如Map<Integer, String>），dict更灵活，对数据类型没有限制。每个key只能对应一个value。
通过大括号{}进行初始化。
key和value之间通过冒号:连接，不同的键值对之间通过逗号,分隔。
pop,get,按key索引都支持。
```
mydic = {}
mydic['key1'] = 'value1'
mydic['key2'] = 'value2'
mydic[3] = 'value3'
print(mydic)
print(mydic['key1'])
print(mydic[3])
print(5 in mydic)

# print result:
{'key1': 'value1', 'key2': 'value2', 3: 'value3'}
value1
value3
False
```

- set集合

一组元素不能重复的集合。相当于去重的list。支持add,pop,remove方法。可以通过difference,union,intersection和其他集合求差，并，交。

```
myset = set()
myset.add(1)
myset.add(2)
list1 = [1,2,3,4,5]
set1 = (2,3,4,5,6)

print(myset.union(list1))
print(myset.union(set1))
print(myset)

# print result:
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
{1, 2}

```


