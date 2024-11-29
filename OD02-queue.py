class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def process_queue():
    queue = Queue()
    clients = ["Alice", "Bob", "Charlie"]

    for client in clients:
        queue.enqueue(client)

    print("Обслуживание клиентов:")
    while not queue.is_empty():
        print(f"Обслуживается клиент: {queue.dequeue()}")

# Пример использования:
process_queue()
# Вывод:
# Обслуживание клиентов:
# Обслуживается клиент: Alice
# Обслуживается клиент: Bob
# Обслуживается клиент: Charlie
