def gen():
    i=0
    while i<10:
        yield i
        i+=1


print(list(gen()))