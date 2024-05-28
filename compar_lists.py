"""
compare_lists.py
Almarranz 2024 May 28
Extracts the nearest neighbors between tow list that are closer that the value of 'dis_min'
l1 and l2 should be np arrays of coordinates [x,y] 
Returns: Coord. of l1 matches, Coord. of l2 matches, l1 ind. of matches, l2 ind. of matches, distances 
"""
from sklearn.neighbors import NearestNeighbors
import numpy as np
def compare_lists(l1,l2, dis_min):
    nbrs1 = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(l2)
    dis1, ind1 = nbrs1.kneighbors(l1)

    nbrs2 = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(l1)
    dis2, ind2 = nbrs2.kneighbors(l2)

    dis1 = np.array(dis1)

    # print(ind1)

    # print(ind2)
    matc1  = []
    matc2  = []
    d1 = [] 
    d2 = [] 
    l1_i = []
    l2_i = []
    for i, idx1 in enumerate(ind1):
        # idx1 is the index of the nearest neighbor in list2 for point i in list1
        if ind2[idx1[0]] == i and dis1[i]< dis_min:
            # print(l1[i], l2[idx1[0]])
            matc1.append(l1[i])
            matc2.append(l2[idx1[0]])
            d1.append(dis1[i])
            d2.append(dis2[idx1[0]])
            l1_i.append(i)
            l2_i.append(idx1[0])
            

    # valid = d1 < dis_min       
    d1 = np.array(d1)
    d2 = np.array(d2)
    matc1= np.array(matc1)
    matc2= np.array(matc2)
    l1_i = np.array(l1_i)
    l2_i = np.array(l2_i)

    comp = np.c_[matc1,matc2,l1_i,l2_i,d1]
    
    return comp
