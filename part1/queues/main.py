from Queue import Queue

queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.dequeue()
queue.dequeue()

queue.enqueue(40)
queue.enqueue(50)

queue.dequeue()

queue.enqueue(60)
queue.enqueue(70)

print(queue)
queue.reverse()
print(queue)
