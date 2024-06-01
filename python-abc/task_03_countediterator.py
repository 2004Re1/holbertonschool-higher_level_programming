class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter

# Testing the implementation
iterable = [1, 2, 3, 4, 5]
counted_iter = CountedIterator(iterable)

for item in counted_iter:
    print(item)

print(f"Items iterated over: {counted_iter.get_count()}")

