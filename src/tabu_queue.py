class Tabu:
    queue = []
    max_length = 5

    def __init__(self, max_length):
        self.max_length = max_length

    def reset(self):
        self.queue = []

    def add_to_queue(self, item):
        self.queue.append(item)

        if len(self.queue) == self.max_length:
            self.queue.pop(0)

    def is_item_in_queue(self, item):
        return item in self.queue
