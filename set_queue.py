from queue import Queue

class SetQueue(Queue):
    all_elements = set()

    def put(self, item, block=True, timeout=None):
        if item not in self.all_elements:
            super(SetQueue, self).put(item, block=block, timeout=timeout)
            self.all_elements.add(item)

    def get(self, block=True, timeout=None):
        item = super(SetQueue, self).get(block=block, timeout=timeout)
        self.all_elements.remove(item)
        return item

    def exists(self, item):
        return item in self.all_elements
