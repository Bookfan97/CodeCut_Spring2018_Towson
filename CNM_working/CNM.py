import snap
import importlib
import graphviz as gv
from graphviz import Digraph

# UGraph.isNode(x)
count=0
graphList=["DataFiles/px4.gv","DataFiles/gnuchess.gv","DataFiles/px4_subsample_100lines.txt","DataFiles/px4_subsample_762lines.txt"]
UGraph= snap.PUNGraph.New()

for index in range(0, len(graphList)):
    # print(index + ": " + graphList[index])
    print("%(n)s:%(s)s" % {'n': index, 's': graphList[index]})
x=input("Which graph file would you like to test?")
# UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)

# dot = Digraph(comment=graphList[x])
with open(graphList[x], "r") as f:
    for line in f:
        if line.strip() == "}":
            break
        NodeIDL, NodeIDR= line.split("->")
        NodeIDR=NodeIDR.split("[")[0]
        # print("NodeIDL (pre-strip): "+NodeIDL)
        # print("NodeIDL (pre-strip): "+NodeIDR)
        NodeIDR.strip()
        string1= NodeIDR.split("x",1)[1]
        string2= NodeIDL.strip("s_0x")
        a= int(string1, 16)
        b= int(string2, 16)
        if UGraph.IsNode(a) == False:
            UGraph.AddNode(a)
            # dot.node(string1, str(a))
        if UGraph.IsNode(b) == False:
            UGraph.AddNode(b)
            # dot.node(string2, str(b))
        if UGraph.IsEdge(a,b)==False:
            UGraph.AddEdge(a, b)
            # dot.edge(string1, string2, constraint='false')
            # print("Edge w/if added")
        count=count+1
        # print("count during for loop: ", count)
# print("Test to see if reached")
CmtyV = snap.TCnComV()
# print("Test to see if reached2")
# modularity = snap.CommunityGirvanNewman(UGraph, CmtyV)
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    for NI in Cmty:
        print (hex(NI))
print ("The modularity of the network is %f" % modularity)
# print(dot.source)
# dot.render(graphList[x], view=True)
# print("The count is: ", count)
# dot= Digraph(UGraph)
# dot.render("DataFiles/px4.gv", view=True)