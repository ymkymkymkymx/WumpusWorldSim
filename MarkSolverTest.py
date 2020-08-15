from MarkSolver import *
from nodeclass import *


if True:
    map1= [[0,0,0,0],[0,0,0,0],[0,0,0,3],[0,0,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map1),4,4)): print("true")
    else: print("false")

    map2= [[0,1,0,0],[1,1,1,1],[0,0,0,3],[0,0,1,0]]
    print("Should be false:")
    if(marksolver(maptrans(map2),4,4)): print("true")
    else: print("false")

    map3= [[0,0,2,0],[0,0,0,3],[1,0,0,0],[0,0,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map3),4,4)): print("true")
    else: print("false")

    map4=[[0,0,1,0],[0,0,0,3],[1,0,0,0],[0,0,0,0]]
    print("Should be false:")
    if(marksolver(maptrans(map4),4,4)): print("true")
    else: print("false")

    map5=[[0,0,0,1],[0,0,2,3],[1,1,0,0],[0,0,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map5),4,4)): print("true")
    else: print("false")

    map6 =[[0,0,0,0],[0,0,0,0],[1,1,0,1],[3,0,2,0]]
    print("Should be true:")
    if(marksolver(maptrans(map6),4,4)): print("true")
    else: print("false")

    map7=[[0,0,0,0],[0,0,0,2],[1,0,0,3],[0,0,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map7),4,4)): print("true")
    else: print("false")

    map8=[[0,0,2,3],[0,0,0,0],[0,0,0,1],[1,1,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map8),4,4)): print("true")
    else: print("false")

    map9 =[[0,0,0,1],[0,0,1,0],[0,1,0,0],[3,0,2,0]]
    print("Should be true:")
    if(marksolver(maptrans(map9),4,4)): print("true")
    else: print("false")

    map10 =[[0,0,1,0],[0,0,0,1],[2,0,3,0],[1,1,0,0]]
    print("Should be true:")
    if(marksolver(maptrans(map10),4,4)): print("true")
    else: print("false")

    map11=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[2,0,3,0]]
    print("Should be true:")
    if(marksolver(maptrans(map11),4,4)): print("true")
    else: print("false")

    map12=[[0,0,1,0],[0,0,0,3],[0,2,0,0],[0,0,0,1]]
    print("Should be true:")
    if(marksolver(maptrans(map12),4,4)): print("true")
    else: print("false")