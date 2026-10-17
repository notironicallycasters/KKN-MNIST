import math
from utils import *


def get_point(value:dict) -> tuple: #From a table, get the 784 dimensions tuple of one point
    point = []
    for x in range(1,29):
      for y in range(1,29):
        point.append(float(value[str(x)+"x"+str(y)]))
    return point

def fetch_points(table:list) -> list: #From a table, remove all the xy parameters and replace them with one tuple
    print("Fetching points tuple...")
    for e in table:
        point = []
        for x in range(1,29):
            for y in range(1,29):
              point.append(float(e[str(x)+"x"+str(y)]))
              e.pop(str(x)+"x"+str(y), None)
              e["point"] = point
    print("Done!")
    return table

def knn(k:int,value:dict,table:list) -> tuple: #K-Nearest Neighbors, returns tuple with success,label,prediction and confidence
    label = value["label"]
    point = value["point"]

    for e in table:
        e["distance"] = math.dist(point,e["point"])
    table.sort(key= lambda x : x["distance"])
    knn = [table[i]["label"] for i in range(k)]

    occ = occurences(knn)
    predicition = next(iter(occ.keys()))
    confidence = occ[predicition]/k

    return label == predicition, label , predicition,confidence 

train = fetch_points(importTable("Mnist/mnist_train.csv"))
#test = fetch_points(importTable("Mnist/mnist_test.csv"))

print("Testing personal database")
for i in range(10):
    print(knn(5,get_image_as_point("MyDB/"+str(i)+".png"),train))

print("\nTesting MNIST testing data")
for i in range(len(test)):
   print(knn(5,test[i],train))
