#!/usr/local/bin/python3

from queue import Queue
import random
import threading
import time

"""
python多线程的限制
python多线程有个讨厌的限制，全局解释器锁（global interpreter lock），这个锁的意思是任一时间只能有一个线程使用解释器，
跟单cpu跑多个程序一个意思，大家都是轮着用的，这叫“并发”，不是“并行”。手册上的解释是为了保证对象模型的正确性！
这个锁造成的困扰是如果有一个计算密集型的线程占着cpu，其他的线程都得等着, 多线程生生被搞成串行；
当然这个模块也不是毫无用处，手册上又说了：当用于IO密集型任务时，IO期间线程会释放解释器，这样别的线程就有机会使用解释器了！
所以是否使用这个模块需要考虑面对的任务类型。
"""

#生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
        self.timeOfProduction = 5

    def run(self):
        for i in range(self.timeOfProduction):
            print("%s is producing %d to the queue!" % (self.getName(), i))
            self.data.put(i)
            # sleep设置让生产快于消费
            time.sleep(random.randrange(10)/5)
        print("%s finished!" % self.getName())

#消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
        self.timeOfCosumption = 5
    def run(self):
        for i in range(self.timeOfCosumption):
            val = self.data.get()
            print("%s is consuming. %d in the queue is consumed!" % (self.getName(),val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())

def producer_consumer_single():
    queue = Queue()
    producer = Producer("Producer",queue)
    consumer = Consumer("Consumer",queue)

    producer.start()
    consumer.start()
    # 如果没有 join 主线程就不会被阻隔，直接输出‘All threads finished’
    # 然后子线程继续进行，陆续输出结果
    producer.join()
    consumer.join()
    print("All threads finished!")

if __name__ == "__main__":
    producer_consumer_single()
