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


