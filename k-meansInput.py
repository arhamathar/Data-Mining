import math

def ReadData(fileName): 
  
    f = open(fileName, 'r')
    lines = f.read().splitlines()
    f.close() 
  
    items = []
  
    for val in lines: 
        line = val.split(',') 
        itemFeatures = []
  
        for num in line: 
            v = float(num)
            itemFeatures.append(v)
  
        items.append(itemFeatures) 
    return items

data = ReadData('K-Means.csv')

x = [i[0] for i in data]
y = [i[1] for i in data]


print(data)


def euclideanDistance(center, point):
    d = 0.0
    for i in range(0,len(point)):
        d += (center[i]-point[i])**2
    return math.sqrt(d)


def assignClusters(centers, dataset):
    clusters = []
    for i in range(len(dataset)):
        distances = []
        for center in centers:
            distances.append(euclideanDistance(center, dataset[i]))
        temp = [z for z, val in enumerate(distances) if val==min(distances)]

        clusters.append(temp[0])
    return clusters


def mean_center(k, dataset, clusters):
    nCenters = []
    for i in range(k):
        x = 0.0
        y = 0.0
        count = 0
        for j in range(len(clusters)):
            if(i == clusters[j]):
                x += dataset[j][0]
                y += dataset[j][1]
                count += 1
        x = x/count
        y = y/count
        nCenters.append([x,y])
    return nCenters

print("Enter the value of k")
k = int(input())
centers = []
for i in range(k):
    print("Enter Center "+str(i))
    temp = [int(x) for x in input().split()]
    centers.append(temp)

print("Initial centers are: ")
print(centers)
print("Initial clusters  are: ")
clusters = assignClusters(centers, data)
print(clusters)
for i in range(k):
    print("Cluster "+str(i))
    for j in range(len(clusters)):
        if(i == clusters[j]):
            print(data[j],end=' ')
    print()
print()
for itr in range(4):
    print("Iteration "+str(itr))
    centers = mean_center(k,data,clusters)
    print("Updated centers: ")
    print(centers)
    clusters = assignClusters(centers, data)
    print("Updated clusters: ")
    for i in range(k):
        print("cluster "+str(i))
        for j in range(len(clusters)):
            if(i == clusters[j]):
                print(data[j],end=' ')
        print()