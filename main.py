def producer(n):
    i = 1
    while i<= n:
        yield i
        i += 1

def consumer(n):
    data = producer(n)
    for item in data:
        print(item)


consumer(5)
