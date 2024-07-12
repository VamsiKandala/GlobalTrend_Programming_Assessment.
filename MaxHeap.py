class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_value = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            max_value = self.heap.pop()
        else:
            max_value = None
        return max_value

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

heap = MaxHeap()
while True:
    action = input("Choose action (insert, delete, get_max, exit): ").strip().lower()
    if action == 'insert':
        value = int(input("Enter value to insert: "))
        heap.insert(value)
        print(f"Heap after insertion: {heap.heap}")
    elif action == 'delete':
        print(f"Deleted value: {heap.delete()}")
        print(f"Heap after deletion: {heap.heap}")
    elif action == 'get_max':
        print(f"Max value: {heap.get_max()}")
    elif action == 'exit':
        break
    else:
        print("Invalid action. Please try again.")
