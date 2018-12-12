import trees
myDat,labels=trees.createDataSet()
myDat
trees.splitDataSet(myDat,0,1)
trees.splitDataSet(myDat,0,0)
trees.createTree(myDat,labels)
