import snap

count=0
graphList=["DataFiles/px4.gv","DataFiles/gnuchess.gv","DataFiles/px4_subsample_100lines.txt","DataFiles/px4_subsample_762lines.txt", "DataFiles/test_length.txt"]
UGraph= snap.PUNGraph.New()
w= 100;
communities=[[0 for x in range(w)] for y in range(w)]
clusters=[]
comm=[]
map=[]
allnodes=[]
cmtyindex=0
nodeindex=0
c=[]
community=[0 for x in range(50)]
v=0
for index in range(0, len(graphList)):
    print("%(n)s:%(s)s" % {'n': index, 's': graphList[index]})
filename=input("Which graph file would you like to test?")
print(str(graphList[filename]))
with open(graphList[filename], "r") as f:
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
        comm.append(NI)
    comm.sort()
    clusters.append(comm)
    comm=[]
    v = v + 1;
print ("The modularity of the network is %f" % modularity)
allnodes.sort()
for x in xrange(1,len(clusters)):
    index=0
    cluster=clusters[x]
    moduleStart = clusters[x][index]
    indexplusone=index=1
    if indexplusone>len(cluster)-1:
        break
    tempModuleEnd = clusters[x][indexplusone]
    nextFunction1 = clusters[x][index]
    allindex=allnodes.index(moduleStart)
    nextFunction2 = allnodes[allindex]
    while (nextFunction1 == nextFunction2):
        index=index+1
        if index>len(cluster)-1:
            break
        allindex=allindex+1
        if allindex>len(allnodes)-1:
            break
        nextFunction1 = cluster[index]
        nextFunction2 = allnodes[allindex]
        if(nextFunction1 == nextFunction2):
          tempModuleEnd = nextFunction1
    finalindex=abs(moduleStart-tempModuleEnd)
    map.append(hex(finalindex))
map.sort()
print(map)
file=graphList[filename].split(".txt")
filestring=str(file[0])
mapname=filestring+".map"
