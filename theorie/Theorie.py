#!/usr/bin/env python
# coding: utf-8

# In[65]:


graph4 = [[0,0,1,0],
          [0,0,1,1],
          [1,1,0,1],
          [0,1,1,0]]


graph5 = [[0,1,0,0,0],
          [1,0,0,0,1],
          [0,0,0,1,1],
          [0,0,1,0,1],
          [0,1,1,1,0]]



graph3 = [[0,1,1,1,1],
          [1,0,1,0,0],
          [1,1,0,0,0],
          [1,0,0,0,1],
          [1,0,0,1,0]]

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
         [4, 0, 8, 0, 0, 0, 0, 11, 0], 
         [0, 8, 0, 7, 0, 4, 0, 0, 2], 
         [0, 0, 7, 0, 9, 14, 0, 0, 0], 
         [0, 0, 0, 9, 0, 10, 0, 0, 0], 
         [0, 0, 4, 0, 10, 0, 2, 0, 0], 
         [0, 0, 0, 14, 0, 2, 0, 1, 6], 
         [8, 11, 0, 0, 0, 0, 1, 0, 7], 
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]; 

graph2 = [[0, 3, 1, 0, 5, 0], 
          [3, 0, 0, 1, 0, 6], 
          [1, 0, 0, 0, 2, 0], 
          [0, 1, 0, 0, 0, 1], 
          [5, 0, 2, 0, 0, 4], 
          [0, 6, 0, 1, 4, 0]]; 


def weights_edges(graph): #somme des poids des bords
    w_sum = 0
    l = len(graph)
    for i in range(l):
        for j in range(i,l):
            w_sum += graph[i][j]
    return w_sum
            

    
def shortest_path(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    #Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if(i==source):
            shortest[source] = 0 #graph[source][source]
        else:
            if(graph[source][i]==0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if(shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i
                
    if(source==dest):
        return [0, selected]
    selected.append(ind) 
    while(ind!=dest):
        for i in range(l):
            if i not in selected:
                if(graph[ind][i]!=0):
                    #Check si la distance dois etre maj
                    if((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000

        for j in range(l):
            if j not in selected:
                if(shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)
    
    return [shortest[dest], selected]
                            

def get_odd(graph):
    degrees = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
                if(graph[i][j]!=0):
                    degrees[i]+=1
                
    #print(degrees)
    odds = [i for i in range(len(degrees)) if degrees[i]%2!=0]
    #print('odds are:',odds)
    return odds

#Fonction de generation des paires
def gen_pairs(odds):
    pairs = []
    for i in range(len(odds)-1):
        pairs.append([])
        for j in range(i+1,len(odds)):
            pairs[i].append([odds[i],odds[j]])
        
    return pairs


#Fonction "finale"
def chemin_2_parcours(graph):
    odds = get_odd(graph)
    if(len(odds)==0):
        return weights_edges(graph)
    pairs = gen_pairs(odds)
    l = (len(pairs)+1)//2
    
    pairings_sum = []
    
    def get_pairs(pairs, done = [], final = []):
        
        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])
            
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    get_pairs(pairs[1:],val, f)
                    
        else:
            get_pairs(pairs[1:], done, final)
            
    get_pairs(pairs)
    min_sums = []
    all_path = []
    for i in pairings_sum:
        s = 0
        for j in range(len(i)):
            tmp = shortest_path(graph, i[j][0], i[j][1])
            #s += tmp[0]
            all_path.append(tmp[1])
            
    l_graph = len(graph)
    longest_inc_path = 0
    for i in all_path:
        if (len(i) == l_graph):
            good = True
            for j in range(l_graph):
                if j not in i:
                    good = False
            if (good):
                return i
        else:
            if (len(i) == longest_inc_path):
                longest_inc_path = i
    full_path = all_path[longest_inc_path]
    for m in range(l_graph):
        if m not in full_path:
            tmp2 = shortest_path(graph, full_path[len(full_path) - 1], m)[1]
            for n in range (len(tmp2)):
                if (n != 0):
                    full_path.append(tmp2[n])
    
    return full_path


# In[66]:


chemin_2_parcours(graph)

