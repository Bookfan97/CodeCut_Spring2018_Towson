import snap
import importlib
import graphviz as gv

# UGraph.isNode(x)
count=0
UGraph= snap.TUNGraph.New()
# UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
with open("DataFiles/px4.gv", "r") as f:
    for line in f:
        if line== "}":
            break
        NodeIDL, NodeIDR= line.split("->")
        NodeIDR=NodeIDR.split("[") [0]
        print("NodeIDL (pre-strip): "+NodeIDL)
        print("NodeIDL (pre-strip): "+NodeIDR)
        NodeIDR.strip()
        a= NodeIDR.split("x",1)[1]
        b= NodeIDL.strip("s_0x")
        print("NodeIDR: "+ a)
        print("NodeIDL: "+b)
        UGraph.IsNode(int(a, 16))
        UGraph.IsNode(int(b, 16))
        count=count+1

CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    for NI in Cmty:
        print (NI)
print ("The modularity of the network is %f" % modularity)
print("The count is: " ,count)
