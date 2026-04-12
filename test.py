import math
from utils import *
import ast, json

def get_point(value):
    point = []
    for x in range(1,29):
      for y in range(1,29):
        point.append(float(value[str(x)+"x"+str(y)]))
    return point

def knn(k,value,table):
    label = value["label"]
    point = get_point(value)

    for e in table:
        e["distance"] = math.dist(point,e["point"])
    table.sort(key= lambda x : x["distance"])
    knn = [table[i]["label"] for i in range(k)]

    predicition = next(iter(occurences(knn).keys()))

    return label == predicition, label , predicition

print("Loading training...")
with open("mnist_train.json") as f:
    train = ast.literal_eval(f.read())
print("Loading testing...")
with open("mnist_test.json") as f:
    test = ast.literal_eval(f.read())

for i in range(100):
   print(knn(5,test[i],train))
