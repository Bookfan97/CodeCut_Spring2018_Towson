import snap
import importlib
import graphviz as gv

# UGraph.isNode(x)
count=0
UGraph= snap.PUNGraph.New()
# UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
with open("DataFiles/test.txt", "r") as f:
    for line in f:
        if line== "}":
            break
        NodeIDL, NodeIDR= line.split("->")
        NodeIDR=NodeIDR.split("[") [0]
        print("NodeIDL (pre-strip): "+NodeIDL)
        print("NodeIDL (pre-strip): "+NodeIDR)
        NodeIDR.strip()
        string1= NodeIDR.split("x",1)[1]
        string2= NodeIDL.strip("s_0x")
        a= int(string1, 16)
        b= int(string2, 16)
        if UGraph.IsNode(a) == False:
            UGraph.AddNode(a)
        if UGraph.IsNode(b) == False:
            UGraph.AddNode(b)
        if UGraph.IsEdge(a,b)==False:
            UGraph.AddEdge(a, b)
            print("Edge w/if added")
        count=count+1
        print("count during for loop: ", count)
print("Test to see if reached")
CmtyV = snap.TCnComV()
# modularity = snap.CommunityGirvanNewman(UGraph, CmtyV)
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    for NI in Cmty:
        print (NI)
print ("The modularity of the network is %f" % modularity)
print("The count is: " ,count)
