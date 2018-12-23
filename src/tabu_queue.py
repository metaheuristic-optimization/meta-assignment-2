"""
Simple implementation of a tabu queue using a list
"""


class Tabu:
    queue = []
    max_length = 5

    def __init__(self, max_length):
        # Determine max length
        self.max_length = max_length

    def reset(self):
        """
        Resets the queue to be empty
        """
        self.queue = []

    def add_to_queue(self, item):
        """
        Append an item to the queue
        :param item: An item to add to the queue
        """
        self.queue.append(item)

        # Make sure we have filled the queue up before removing items from the queue
        if len(self.queue) == self.max_length:
            self.queue.pop(0)

    def is_item_in_queue(self, item):
        """
        Checks if an item is in the tabu list
        :param item: True if the item is in the queue, otherwise False
        """
        return item in self.queue
