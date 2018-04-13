import snap
import importlib
import graphviz as gv
from graphviz import Digraph

# UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
UGraph=gv.Digraph(open("DataFiles/px4.gv", "r") )
CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    for NI in Cmty:
        print (NI)
print ("The modularity of the network is %f" % modularity)