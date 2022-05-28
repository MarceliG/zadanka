lis = [1,2,3]
print(lis, id(lis))
lis2 = lis
print(lis2, id(lis2))
lis2.append(4)
print(lis, id(lis))
print(lis2, id(lis2))
lis3 = lis.copy()
print(lis3, id(lis3))
