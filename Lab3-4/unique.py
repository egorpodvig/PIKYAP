class Unique:
    def __init__(self, items, **kwargs):
        self.items = items if isinstance(items, (list, tuple)) else list(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.iterator)
                check_item = item.lower() if self.ignore_case and isinstance(item, str) else item
                if check_item not in self.seen:
                    self.seen.add(check_item)
                    return item
            except StopIteration:
                raise StopIteration

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_numbers = Unique(data)
print(list(unique_numbers))

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_strings = Unique(data)
print(list(unique_strings))

unique_strings_case = Unique(data, ignore_case=True)
print(list(unique_strings_case))

