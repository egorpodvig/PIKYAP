def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:
                yield result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стул', 'color': None}
]

print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))
