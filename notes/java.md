
# Java学习

<!-- TOC -->

- [Java学习](#java学习)
    - [stream](#stream)

<!-- /TOC -->
---


## stream

- 将要处理的元素集合看作一种流，流在管道中传输，并可以在管道的节点上进行一步一步、逐级的处理（filter，sort等中间操作），并由最终操作得到前面处理的结果。

```
    List<String> list = Arrays.asList("a", "ab", "bcd", "", "", "abb", "dd");
    System.out.println(list.size());

    Stream<String> stream = list.stream();

    long count = stream.filter(cur -> {
        if(cur.contains("a"))
            return true;
        return false;
    }).count();
    System.out.println(count);
```

- filter()函数对从stream中获得的元素进行过滤，过滤的规则就是传递给filter的参数。这个参数是一个函数，所以这是一个lambda表达式。
    - 这个函数的参数为 cur。
    - 这个函数的方法体为大括号中的内容。如果用大括号来写，要写上返回语句。
    - filter的参数要求应该是一个布尔类型值，对返回结果为true的情况作为过滤后留下。
    - 这里期望过滤出包含字符串"a"的元素。
    - 最终操作是计数。注意，这里被计数的主体已经是经过filter处理后的了。

```
//  输出结果
7
3
```

- 同一个流只能使用一次。如果想多次使用，可以多次调用stream()方法。
- sorted() 排序
- distinct() 去重
- forEach() 最终操作，对处理后的每个元素使用方法
    - 如 System.out::println
    - 这个语法为，前面是调用的方法的类，用::来引出方法名
    - 
- count() 计数
- filter() 过滤，相当于SQL中的where语句
- collect() 最终操作，聚合
    - 如 collect(Collectors.toList()) 将变成流的集合处理后再变成集合
    - collect(Collectors.joining(",")) 返回类型是String，将流中的元素连接成字符串，通过joining的参数作为连字符
- mapToInt(x->x).summaryStatistics() 得到一个对整数型列表进行数学统计的类IntSummaryStatistics的实例。这个类提供常用统计方法：
    - getMax, getMin, getSum等等
- map() 映射，对每个元素映射到对应的结果，相当于给每个元素进行一次函数运算（类似于filter对每个元素进行一次过滤运算）。
    - 如map(i -> i*i)将每个元素变成它对应的平方数

