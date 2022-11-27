from random import uniform
import math

def ReadData(fileName): 
  
    # Read the file, splitting by lines 
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


def FindColMinMax(items):
    n = len(items[0])
    minima = [float("inf") for i in range(n)]
    maxima = [float("-inf") for i in range(n)]

    for item in items:
        for i in range(len(item)):
            minima[i]=min(minima[i], item[i])
            maxima[i]=max(maxima[i], item[i])
    print('minima ->' ,minima)
    print('maxima ->' ,maxima)
    return minima,maxima


def InitializeMeans(items, k, cMin, cMax):    
    f = len(items[0])
    means = [[0 for i in range(f)] for j in range(k)]
      
    for mean in means:
        for i in range(len(mean)):
            mean[i] = uniform(cMin[i]+1, cMax[i]-1)
    return means


def EuclideanDistance(x, y): 
    S = 0;
    for i in range(len(x)): 
        S += math.pow(x[i]-y[i], 2)
  
    return math.sqrt(S)


def UpdateMean(n,mean,item):
    for i in range(len(mean)):
        m = mean[i]
        m = (m*(n-1)+item[i])/float(n)
        mean[i] = round(m, 3)
      
    return mean


def FindClusters(means, items):
    clusters = [[] for i in range(len(means))]
      
    for item in items:
        index = Classify(means,item)  
        clusters[index].append(item)
    return clusters


def Classify(means,item):  
    minimum = float("inf")
    index = -1
  
    for i in range(len(means)):  
        dis = EuclideanDistance(item, means[i])
        
        if (dis < minimum):
            minimum = dis
            index = i
    return index


def CalculateMeans(k, items, maxIterations=100000):
    cMin, cMax = FindColMinMax(items)
    means = InitializeMeans(items,k,cMin,cMax)
      
    clusterSizes= [0 for i in range(len(means))]
    print(clusterSizes,'clusterSizes')
  
    belongsTo = [0 for i in range(len(items))]
  
    for e in range(maxIterations):
  
        noChange = True
        for i in range(len(items)):
  
            item = items[i];
            index = Classify(means,item)
  
            clusterSizes[index] += 1
            cSize = clusterSizes[index]
            means[index] = UpdateMean(cSize,means[index],item)
            if(index != belongsTo[i]):
                noChange = False
            belongsTo[i] = index
            
        if (noChange):
            break
            
    return means


items = ReadData('K-Means.csv')
k = 3
means = CalculateMeans(k,items)
clusters = FindClusters(means,items)
print (means)
print(clusters)