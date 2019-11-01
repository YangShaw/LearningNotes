
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

键值对的集合，就是我们常说的Map，相较于Java中的Map类要指定键和值的数据类型（如Map<Integer, String>）
