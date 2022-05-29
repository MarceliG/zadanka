from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "bbbccccccddddeeee"

my_counter = Counter(a)
print("most common: " + str(my_counter.most_common(2)))
print("elements: " + str(list(my_counter.elements())))
print("---------------------------")
Point = namedtuple('Point', "x,y")
pt = Point(1,8)
print("nametuple: {} ".format(pt))
print("---------------------------")
order_dict = OrderedDict() # {} the same
order_dict["a"] = 1
order_dict["b"] = 2
order_dict["c"] = 3
order_dict["d"] = 4
print(order_dict)
print("---------------------------")
default_dict = defaultdict(int)
default_dict["a"] = 1
default_dict["b"] = 2
print("default_dict a:{}, b:{}, c:{}".format(default_dict["a"], default_dict["b"], default_dict["c"]))
print("---------------------------")
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.appendleft(8)
my_deque.append(5)
my_deque.appendleft(10)
print("deque {}".format(my_deque))
my_deque.rotate(1)
print("deque rotated {}".format(my_deque))