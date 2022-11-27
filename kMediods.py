import numpy as np


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


def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def get_costs(data, medoids):
    tmp_clusters = {i:[] for i in range(len(medoids))}
    cst = 0
        
    for d in data:
        dis = [manhattan(d, data[md]) for md in medoids]
        c = dis.index(min(dis))
        tmp_clusters[c].append(d)
        cst+=min(dis)

    tmp_clusters = {k:np.array(v) for k,v in tmp_clusters.items()}
    return tmp_clusters, cst


def k_medoid(data, k, medoids):
    clusters, cost = get_costs(data, medoids)
    print("Medoids :",medoids)
    n=len(data)
    while True:
        swap = False
        for i in range(n):
            if i not in medoids:
                for j in range(k):
                    tmp_meds = medoids[:]
                    tmp_meds[j] = i
                    clusters_, cost_ = get_costs(data, tmp_meds)

                    if cost_<cost:
                        medoids = tmp_meds
                        cost = cost_
                        swap = True
                        clusters = clusters_
                        print("Medoids :",medoids)
                        
        if not swap:
            print("Medoids :",medoids)
            return clusters
    

k=3
data = ReadData('K-Means.csv')
medoids=[0,1,2]
print("Data :",data)
print()
clusters=k_medoid(data, k, medoids)
print()
for i in range (k):
    print("Medoid {} : {}".format(i, data[medoids[i]]))
    print("Cluster ",i,":",*clusters[i])
    print()
