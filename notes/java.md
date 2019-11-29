
**Java学习**

<!-- TOC -->

- [1. stream](#1-stream)
    - [1.1. Intermediate operation](#11-intermediate-operation)
    - [1.2. terminal operation](#12-terminal-operation)
    - [1.3. 生成流](#13-生成流)
- [2. 输入输出流](#2-输入输出流)
    - [2.1. 关于字节](#21-关于字节)
    - [2.2. 字节操作](#22-字节操作)
    - [2.3. 字符操作](#23-字符操作)
- [java annotation](#java-annotation)
    - [介绍](#介绍)
    - [举例](#举例)

<!-- /TOC -->
---


# 1. stream

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

## 1.1. Intermediate operation

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

## 1.2. terminal operation

- forEach() 最终操作，对处理后的每个元素使用方法
    - 如 System.out::println
    - 这个语法为，前面是调用的方法的类，用::来引出方法名
    - 如果希望对每个元素不仅仅是打印，可以这样操作 forEach(cur->System.out.print(cur+"\t")),诸如此类。
    - 总之，forEach方法接收的是一个lambda表达式，所以这个表达式可以直接是函数名（第一种情况），也可以是在括号中直接写一个函数进来（第二种情况）。 
- count() 计数
- reduce() 

## 1.3. 生成流
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

# 2. 输入输出流

![javaio](imgs/java-io.png)

## 2.1. 关于字节
- String类型的getBytes()方法，将字符串转成字节数组，字节数组的长度就是字节的个数。
    - getBytes()方法可以加编码格式作为参数，如UTF-8,GBK等。
    - new String()方法可以接收一个字节数组作为参数，用来将字节数组转回字符串格式。同样可以加入一个编码格式作为参数。

## 2.2. 字节操作

- FileOutputStream 打开一个文件输出流
    - DataOutputStream 允许按照基本数据类型和字节数组进行读取
        - 构造方法 接收文件流作为参数，通过data流向文件中输出内容。
        - write方法 接收字节数组作为参数，写入这个字节数组的内容。如果用这个方法来写入整数，那么会默认只写入一个字节（而int会占用四个字节，从而造成丢失）。还可以增加偏移量和长度参数，用来写入字节数组的某个特定部分。
        - writeInt方法 写入int型数据。除此之外，这个类还提供写入各种基本数据类型的方法，很方便。
        
    - ByteArrayOutputStream 打开一个字节缓存流，但是不直接和文件流对接
        - write方法 接收字节数组作为参数，同上。但是不提供写入各种数据类型的方法，只能按照字节数组来传入。
        - writeTo方法 接收一个文件输出流作为参数，把这个字节缓存流的内容写入到文件中。
    - FileOutputStream 直接在文件流输入
        - 构造方法 接收文件名称或文件地址作为参数。
        - write方法 类似前面

- FileInputStream 打开一个文件输入流
    - DataInputStream
        - available方法 返回一个整数，检查文件是否读入完成。若返回负数则文件读取结束。
        - read方法 接收字节数组作为参数，读取响应字节的数据存放到数组中。也可以加入偏移量和长度参数。
        - readInt方法 读取一个整数。同理还有读取其他数据类型的方法。

## 2.3. 字符操作

- Writer
    - FileWriter 打开一个文件，直接写入
        - write方法 可以写入int，String等，但不能按字节写入。
        - flush方法 刷新后才写入文件，之前是暂存。
    - PrintWriter 打开一个文件，直接写入
        - 直接用print和println方法写，格式和System.out.print相同。

# java annotation

## 介绍
给类、方法、参数、变量、包等加上一种特殊的注释，这种标注可以告诉编译器一些信息，而不像普通的注释那样会直接在编译的时候被忽略。

## 举例
- @Override 告诉编译器去检查一下该方法是否正确重载
- @SuppressWarnings 告诉编译器忽略注解中声明的警告

    
