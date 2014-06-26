from pprint import pprint
data = [[i for i in range(10)] for j in range(10)]
pprint(data)

print("sum of data:", sum(sum(x) for x in data))
