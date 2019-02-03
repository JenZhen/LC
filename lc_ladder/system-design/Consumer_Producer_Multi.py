#!/usr/local/bin/python3

from queue import Queue
import random
import threading
import time

condition = threading.Condition()

#生产者类
class ProducerThread(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.numProducers = 5
    def run(self):
        nums = range(5)
        while True:
            condition.acquire()
            num = random.choice(nums)
            self.queue.put(num)
            print("Produced", num)
            condition.notify()
            condition.release()
            time.sleep(random.random(4)) #sleep 4 seconds after each production


#消费者类
class ConsumerThread(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.numConsumers = 5
    def run(self):
        while True:
            condition.acquire()
            if self.queue.emtpy():
                print("Nothing in queue, consumer is waiting")
                condition.wait()
                print("Producer added something to queue and notified the consumer")
            num = self.queue.get()
            print("Consumed: %s" %num)
            condition.release()
            time.sleep(random.random(6)) #sleep withn 6 seconds after each consumption

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

def producer_consumer_multi():

if __name__ == "__main__":
    producer_consumer_single()
