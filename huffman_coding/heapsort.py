

class Heapsort():
    def min_heapify(self, arr: list[int], i: int, lenght: int):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left <= lenght and arr[largest] < arr[left]:
            largest = left

        if right <= lenght and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.min_heapify(arr, largest, lenght)


    def build_min_hep(self, arr: list[int]):
        lenght = len(arr)
        for i in range(((lenght - 1) // 2), -1, -1):
            self.min_heapify(arr, i, lenght - 1)


    def heapsort(self, arr: list[int]):
        self.build_min_hep(arr)
        lenght = len(arr)
        for i in range(lenght - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            lenght = lenght - 1
            self.min_heapify(arr, 0, lenght - 1)