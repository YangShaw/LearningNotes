
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
    - ReentrantLock() 可重入锁，Lock的唯一实现类。
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

