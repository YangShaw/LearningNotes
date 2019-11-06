
# Java学习

<!-- TOC -->

- [Java学习](#java学习)
    - [stream](#stream)
    - [Intermediate operation](#intermediate-operation)
    - [terminal operation](#terminal-operation)
    - [生成流](#生成流)

<!-- /TOC -->
---


## stream

- 将要处理的元素集合看作一种流，流在管道中传输，并可以在管道的节点上进行一步一步、逐级的处理（filter，sort等中间操作），并由最终操作得到前面处理的结果。
- 中间操作时lazy的，只有最终操作才打开这个流，真正开始流的遍历，生成一个结果，并且将流消耗掉。
- 对流的使用是一个**filter-map-reduce**的过程。

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

## Intermediate operation

- filter()函数对从stream中获得的元素进行过滤，过滤的规则就是传递给filter的参数。这个参数是一个函数，所以这是一个lambda表达式。
    - 这个函数的参数为 cur。
    - 这个函数的方法体为大括号中的内容。如果用大括号来写，要写上返回语句。
    - filter的参数要求应该是一个布尔类型值，对返回结果为true的情况作为过滤后留下。
    - 这里期望过滤出包含字符串"a"的元素。
    - 最终操作是计数。注意，这里被计数的主体已经是经过filter处理后的了。
- filter有各种使用的思路，要灵活，就把它当成where语句。如找出偶数，找长度，找属性，等等。
```
//  输出结果
7
3
```

- 同一个流只能使用一次。如果想多次使用，可以多次调用stream()方法。
- sorted() 排序。它的好处在于，可以进行相关必要的操作后（map，filter，limit等）再进行排序，减少被排序的元素的数量。
- distinct() 去重

- filter() 过滤，相当于SQL中的where语句
- collect() 最终操作，聚合
    - collect(Collectors.joining(",")) 返回类型是String，将流中的元素连接成字符串，通过joining的参数作为连字符
    - collect(Collectors.joining()).toString() 不增加连字符，直接合并成字符串
    - 转换成各种数据结构：
        - collect(Collectors.toList()) 将变成流的集合处理后再变成集合
        - collect(Collectors.toCollection(Stack::new)) 变成各种集合类，调用new方法。这里只是用Stack举例。前面的toList也可以归并在这里面，可能是list比较常用，所以单独列了一个方法名。
- map() 映射，对每个元素映射到对应的结果，相当于给每个元素进行一次函数运算（类似于filter对每个元素进行一次过滤运算）。
    - 如map(i -> i*i)将每个元素变成它对应的平方数
- flatMap() 一对多的映射
    ```
    Stream<List<Integer>> inputStream = Stream.of(
    Arrays.asList(1),
    Arrays.asList(2, 3),
    Arrays.asList(4, 5, 6)
    );
    Stream<Integer> outputStream = inputStream.
    flatMap((childList) -> childList.stream());
    ```

- mapToInt(x->x).summaryStatistics() 得到一个对整数型列表进行数学统计的类IntSummaryStatistics的实例。这个类提供常用统计方法：
    - getMax, getMin, getSum等等

- limit() 获取指定数量的流
- skip() 扔掉前n个元素
- parallelStream() 用并行的方式处理流
- IntStream DoubleStream LongStream 基本数值的流，可以直接用它构造流
    ```
    IntStream.range(0,10).forEach(System.out::print);
    IntStream.rangeClosed(0,10).forEach(System.out::print);
    ```

- Optional 表示可能为空，避免空指针错误。
    ```
    List<String> strs = Arrays.asList("abc", null, "bcd");
    Optional.ofNullable(strs.get(1)).ifPresent(System.out::println);
    int length = Optional.ofNullable(strs.get(1)).map(String::length).orElse(-1);
    ```

## terminal operation

- forEach() 最终操作，对处理后的每个元素使用方法
    - 如 System.out::println
    - 这个语法为，前面是调用的方法的类，用::来引出方法名
    - 如果希望对每个元素不仅仅是打印，可以这样操作 forEach(cur->System.out.print(cur+"\t")),诸如此类。
    - 总之，forEach方法接收的是一个lambda表达式，所以这个表达式可以直接是函数名（第一种情况），也可以是在括号中直接写一个函数进来（第二种情况）。 
- count() 计数
- reduce() 

## 生成流
- iterate是一个类似于reduce的函数，给定一个seed，给定一个func，能够生成seed,f(seed),f(f(seed))的数列。
    ```
    List<Integer> generated = Stream.iterate(2, n->n*2)
                    .limit(10)
                    .collect(Collectors.toList());
    ```

- generate 生成自定义类的实例的流。要求被生成的类实现Supplier接口，这个接口要求重写一个get方法。
    - get 用于给出既定的规则，用来自动创建实例。
    ```
    public class PersonSupplier implements Supplier {

        private int index = 0;
        private Random random= new Random();

        @Override
        public MyPerson get() {
            return new MyPerson(index, "StreamGenerate"+index++, random.nextInt(100));
        }

    }
    ```
    - 生成并归类,可以用groupingBy来按照值分组，用partitioningBy只能按照true和false进行两个划分。
    ```
    Map<Integer, List<MyPerson>> personGroups = (Map<Integer, List<MyPerson>>) Stream
                .generate(new PersonSupplier())
                .limit(100)
                .collect(Collectors.groupingBy(MyPerson::getAge));
    
    Iterator it = personGroups.entrySet().iterator();
    while(it.hasNext()){
        Map.Entry<Integer, List<MyPerson>> persons = (Map.Entry<Integer, List<MyPerson>>) it.next();
        System.out.println("Age "+persons.getKey()+"="+persons.getValue().size());
    }

    Map<Boolean, List<MyPerson>> children = (Map<Boolean, List<MyPerson>>) Stream
                .generate(new PersonSupplier())
                .limit(100)
                .collect(Collectors.partitioningBy((MyPerson p)->{
                    if(p.getAge()<18)
                        return true;
                    return false;
                }));

    ```