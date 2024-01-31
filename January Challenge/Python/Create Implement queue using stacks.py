from queue import Queue
class MyQueue:

    def __init__(self):
        self.Q = Queue()

    def push(self, x: int) -> None:
        self.Q.put(x)

    def pop(self) -> int:
        return self.Q.get()

    def peek(self) -> int:
        return self.Q.queue[0]

    def empty(self) -> bool:
        return self.Q.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
