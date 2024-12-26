import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

num_count = int(input())
begin = int(input())
end = int(input())

for num in gen_random(num_count, begin, end):
    print(num)

