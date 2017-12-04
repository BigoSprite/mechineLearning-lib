import kMeans
from numpy import *
import matplotlib

def plotResult():
    datMat=mat(kMeans.loadDataSet('testSet.txt'))
    myCentroids, clustAssing = kMeans.kMeans(datMat,4)
    #return myCentroids, clustAssing
    
    

