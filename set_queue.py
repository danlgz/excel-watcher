from queue import Queue

class SetQueue(Queue):
    all_elements = set()

    def put(self, item, block=True, timeout=None):
        if item not in self.all_elements:
            super(SetQueue, self).put(item, block=block, timeout=timeout)
            self.all_elements.add(item)

    def exists(self, item):
        return item in self.all_elements
