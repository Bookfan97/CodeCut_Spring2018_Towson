import snap
import importlib
import graphviz as gv
from graphviz import Digraph

count=0
graphList=["DataFiles/px4.gv","DataFiles/gnuchess.gv","DataFiles/px4_subsample_100lines.txt","DataFiles/px4_subsample_762lines.txt"]
UGraph= snap.PUNGraph.New()
w, h = 100, 100;
communities=[[0 for x in range(w)] for y in range(h)]
cmtyindex=0
nodeindex=0
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
        if UGraph.IsNode(b) == False:
            UGraph.AddNode(b)
        if UGraph.IsEdge(a,b)==False:
            UGraph.AddEdge(a, b)
        count=count+1
CmtyV = snap.TCnComV()
modularity = snap.CommunityCNM(UGraph, CmtyV)
for Cmty in CmtyV:
    print ("Community: ")
    print(cmtyindex)
    for NI in Cmty:
        communities[cmtyindex][nodeindex]=NI
        print(nodeindex)
        nodeindex=nodeindex+1
        print (hex(NI))
    cmtyindex=cmtyindex+1

print ("The modularity of the network is %f" % modularity)
print(communities)

# Sort the functions in the cluster by address, lowest first
#
# Module_start = <first node address>
#
# Temp_module_end = <first node address>
#
# Do
#
# Next_function1 = <next function in the sorted cluster list>
#
# Next_function2 = <next function in the sorted list of all functions>
#
# If (Next_function1 == Next_function2)
#
#                                 Temp_module_end =  Next_function1
#
#                 While (next_function1 == Next_function2)
#
#                 Output map entry: module_start – temp_module_end
#
#                 #at this point you will have a non-overlapping map file, but it will be out of order
#
# Sort map file, and output