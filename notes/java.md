
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
- [3. java annotation](#3-java-annotation)
    - [3.1. 介绍](#31-介绍)
    - [3.2. 举例](#32-举例)
    - [3.3. 自定义annotation](#33-自定义annotation)
    - [3.4. 元Annotation](#34-元annotation)
    - [3.5. 对象注入到方法或成员变量中](#35-对象注入到方法或成员变量中)
    - [3.6. 总结](#36-总结)
- [4. 反射](#4-反射)
    - [4.1. Class 访问类](#41-class-访问类)
    - [4.2. Field 访问字段](#42-field-访问字段)
    - [4.3. Method 访问方法](#43-method-访问方法)
    - [4.4. Constructor 访问构造方法](#44-constructor-访问构造方法)
    - [4.5. 获得继承关系和实现接口](#45-获得继承关系和实现接口)
    - [4.6. 动态代理](#46-动态代理)
- [5. 序列化](#5-序列化)
    - [5.1. toJson](#51-tojson)

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

# 3. java annotation

## 3.1. 介绍
给类、方法、参数、变量、包等加上一种特殊的注释，这种标注可以告诉编译器一些信息，而不像普通的注释那样会直接在编译的时候被忽略。

例如，编写servlet的时候，需要在web.xml中配置每个servlet对应的信息（类似安卓中，manifest文件中配置每个活动、服务的信息），而通过注解，可以直接在每个需要配置的地方直接加上，非常直观和简洁。**注解可以给类、方法上注入信息**。

## 3.2. 举例
- @Override 告诉编译器去检查一下该方法是否正确重载
- @SuppressWarnings 告诉编译器忽略注解中声明的警告

## 3.3. 自定义annotation
dailyexercise中的demo

在注解上定义的成员变量可以是String， 数组， Class， 枚举类，注解

给注解加注解是为了应对嵌套配置的情况。

## 3.4. 元Annotation
用于修饰其他的注解的定义。

- Retention
指定注解的存在时间，SOURCE, CLASS, RUNTIME（枚举类，只能选择这三项）
- Target
指定被修饰的注解只能用于修饰哪些程序单元。
- Inherited
注解跟随类一起被继承

## 3.5. 对象注入到方法或成员变量中
demo

## 3.6. 总结
- 步骤：得到想要注入的对象属性，通过属性得到注解的信息，通过属性的写方法将注解的信息注入到对象上，最后将对象赋给类。
- 作用：让编译器检查代码，将数据注入到方法、成员变量、类上。

# 4. 反射
**Reflection**
反射是Java给我们提供的，为了解决在运行期，对某个实例一无所知的情况下，如何调用它的方法的一种方式。
例如，我们知道Person p，那么可以调用它的getPersonName()，但如果只有一个Object p，在不知道Person类的情况下（也就是不能强制类型转换使用(Person)p),怎样调用getPersonName()。

## 4.1. Class 访问类
各种类class的本质是Class类。每加载一种class， JVM就为其创建一个Class类型的实例。例如，当加载String类时，创建：
```
Class cls = new Class(String);
```
JVM为每个加载的class创建它对应的Class实例，并在实例中保存了这个class的所有信息（类名，包名，extends和implements，方法，字段）。所以只要得到某个Class实例，我们也就得到了和这个实例对应的class的所有信息。

反射：通过Class实例获得class信息的方法。

- 通过某个class的静态变量
```
Class cls = String.class
```
想想安卓的intent中的(MainActivity.this, SecondActivity.class)。
- 有一个实例变量的时候
```
String s = "hello world";       
Class cls = s.getClass();
```
所以，当我们遇到前面所说的，只知道一个Object o实例的情况下，就可以使用o.getClass()来获得这个实例的类型。
- 知道类的完整类名
```
Class cls = Class.forName("java.lang.String");
```
想想Java大作业中的那个困扰了我一下的Class.forName方法。

以上三种方法给我们的启示是，我们可以通过一个已存在的实例来确定它的类别，也可以根据字符串来确定它的类别（这很强大）。

- 对比instanceof
通常情况下使用instanceof来判断数据类型。这个关键字不但匹配指定的类型，还匹配该类型的子类。
- 动态加载
JVM执行Java程序时候，并不是一次性将所有的class都加载到内存中，而是第一次需要用到class的时候才加载。利用这个特点，我们可以在运行期根据条件加载不同的实现类。

## 4.2. Field 访问字段
通过Field来访问类中的字段，然后可以利用getName, getType, getModifiers来得到字段的相关信息。

通过setAccessible来获得对private字段的访问权限。

通过set来修改字段的值。

## 4.3. Method 访问方法
通过Method来访问类中的字段，getMethod(name, Class..)

利用getName, getReturnType, getParameterTypes, getModifiers等来获得方法的相关信息。

## 4.4. Constructor 访问构造方法
使用newInstance只能调用类的public无参构造方法。
使用下面的代码可以任意调用：
```
Constructor cons1 = Integer.class.getConstructor(int.class);
Integer n1 = (Integer)cons1.newInstance(123);

```

## 4.5. 获得继承关系和实现接口
通过getSuperclass和getInterfaces

## 4.6. 动态代理





# 5. 序列化

## 5.1. toJson
需要解决的两类问题：json字段和JavaBean中的属性名不一致（驼峰命名法 < -- > 蛇形命名法）；部分属性不需要序列化。
- @SerializedName
相当于起别名，默认的value填写json字段的名称。也就是在序列化或反序列化时字段的期望名称。

- @Expose
用来表示是否显示某个属性。有两个值serialize和deserialize。默认是true，即显示。

使用expose注解，在生成Gson对象的时候需要用：
```
Gson excludeGson = new GsonBuilder().excludeFieldWithoutExposeAnnotation().create;
```



# 6 多线程

## 线程的创建

- 单个线程的创建

```
    Thread thread = new Thread(new Runnable(){
        @Override
        public void run() {
            for(int i=0;i<100;++i){
                System.out.print("a");
            }
        }
    });
```

- 期望一次性创建多个线程
  - newCachedThreadPool(): 一个线程池，当需要的时候就创建新的线程。可以使用前面已经创建过的可用的线程。
  - newFixedThreadPool(int numberOfThreads): 一个线程池，包含固定数目的线程。
  - shutdown(): 让线程池不再接收新的task，但现有的未完成的task仍然会继续完成。
  - isTerminated(): 判断线程池中的task是否全都执行完成。通过while语句中对此方法的判断（忙时等待）来确保全都完成。

```
        ExecutorService executorService = Executors.newCachedThreadPool();
        for(int i=0;i<100;++i){
            executorService.execute(new AddAPennyTask());
        }
        executorService.shutdown();
        //  等待所有的线程终止
        while(!executorService.isTerminated()){
        }
```


## 方法

- 静态：sleep(), yield()
- 成员：run(), start(), join(), interrupt(), setPriority()

## 线程优先级

## 同步方法

- synchronized 关键字，可以修饰类，方法，代码块。修饰代码块可以减小需要同步的代码的粒度，这样就能让并发的部分尽可能大。
  - 代码执行完后或发生异常后都会释放。
- Lock接口。Lock需要手动释放锁，sync关键字不需要。
  -  在try中加锁，在finally中释放锁。因为发生异常的时候不会自动释放锁，所以需要用finally来进行保护。
  -  ReentrantLock() 可重入锁，Lock的唯一实现类。

```
    //锁需要声明为全局变量
    Lock lock = new ReentrantLock();
    //...
    //在需要加锁的代码块外面
    try{
        lock.lock();
    } 
    //...
    finally{
        lock.unlock();
    }
```

- Lock和synchronized的选择：
  - 资源竞争激烈时，Lock性能好很多；
  - lock可能会发生死锁。

