import snap
import importlib
import graphviz as gv

# UGraph.isNode(x)
UGraph= snap.TUNGraph.New()
# UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
# UGraph = snap.LoadEdgeList(snap.PNGraph, "DataFiles/px4.gv", 0, 1)
# f=open("DataFiles/px4.gv", "r")
# contents=f.read()
#     for line in contents:
#         print(line)
# print(contents)
UGraph.AddNode(int("80297ac", 16))

CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    for NI in Cmty:
        print (NI)
print ("The modularity of the network is %f" % modularity)


# # with open('data.txt', 'r') as myfile:
# #
# with open("DataFiles/px4.gv", "r") as f:
#     for line in f:
#         <data=myfile.read()
#           node1= data.split("->", 1)
#           node2= data.split("[", 1)
#           data.split("=", 1)
#           node3= data.split("]", 1)
#           graph.add(node1, node 2, node3
#          >
