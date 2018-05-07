import snap
import importlib
import graphviz as gv
from graphviz import Digraph

count=0
graphList=["DataFiles/px4.gv","DataFiles/gnuchess.gv","DataFiles/px4_subsample_100lines.txt","DataFiles/px4_subsample_762lines.txt"]
UGraph= snap.PUNGraph.New()
w= 100;
communities=[[0 for x in range(w)] for y in range(w)]
clusters=[]
comm=[]
map=[]
# temp=[0 for x in range(w)]
allnodes=[]
cmtyindex=0
nodeindex=0
c=[]
community=[0 for x in range(50)]
t=0
v=0
z=0
string=""
for index in range(0, len(graphList)):
    print("%(n)s:%(s)s" % {'n': index, 's': graphList[index]})
x=input("Which graph file would you like to test?")
print(str(graphList[x]))
with open(graphList[x], "r") as f:
    for line in f:
        if line.strip() == "}":
            break
        NodeIDL, NodeIDR= line.split("->")
        NodeIDR=NodeIDR.split("[")[0]
        NodeIDR.strip()
        string1= NodeIDR.split("x",1)[1]
        string2= NodeIDL.strip("s_0x")
        a= int(string1, 16)
        b= int(string2, 16)
        if UGraph.IsNode(a) == False:
            UGraph.AddNode(a)
            allnodes.append(a)
        if UGraph.IsNode(b) == False:
            UGraph.AddNode(b)
            allnodes.append(b)
        if UGraph.IsEdge(a,b)==False:
            UGraph.AddEdge(a, b)
        count=count+1
CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    string = ""
    print ("Community: ")
    for NI in Cmty:
        print (hex(NI))
        # print(NI)
        comm.append(NI)
    comm.sort()
    print("Community " + str(v) + ":" + str(comm))
    clusters.append(comm)
    comm=[]
    v = v + 1;
print ("The modularity of the network is %f" % modularity)
print(allnodes)
print(clusters)
allnodes.sort()
# Sort map file, and output
for x in xrange(1,len(clusters)):
    index=0
    cluster=clusters[x]
    print (cluster)
    moduleStart = clusters[x][index]
    print("module start: "+str(moduleStart))
    tempModuleEnd = clusters[x][index+1]
    print("tempModuleEnd: "+str(tempModuleEnd))
    nextFunction1 = clusters[x][index]
    print("nextFunction1: "+str(nextFunction1))
    allindex=allnodes.index(moduleStart)
    print("all index"+str(allindex))
    nextFunction2 = allnodes[allindex]
    print("nextFunction2: "+str(nextFunction2))
    while (nextFunction1 == nextFunction2):
        index=index+1
        print ("index: "+str(index))
        if index>len(cluster)-1:
            break
        allindex=allindex+1
        print("allindex: "+str(allindex))
        if allindex>len(allnodes)-1:
            break
        nextFunction1 = cluster[index]
        print("nextFunction1: " + str(nextFunction1))
        nextFunction2 = allnodes[allindex]
        print("nextFunction2: " + str(nextFunction2))
        if(nextFunction1 == nextFunction2):
          tempModuleEnd = nextFunction1
          print("tempModuleEnd: "+str(tempModuleEnd))
    finalindex=abs(moduleStart-tempModuleEnd)
    print(finalindex)
    map.append(finalindex)
print(map)
map.sort()
print(map)
