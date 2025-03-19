'''
Created on 2021-07-01

@author: Artur Nowicki, Warsaw  University of Technology
'''

from scripting import *

# get a CityEngine instance
ce = CE()

def convertModelsToShapes():
    
    models = ce.selection()
    print(models)
    
    #repeating operation for all detected models from selection
    for m in models :
        print(m)
        expSettings = ScriptExportModelSettings()
        expSettings.setScript("export_script.py")
        ce.export(m,expSettings)
        
        R = ce.getAttribute(m, 'repRow')
        C = ce.getAttribute(m, 'repCol')
        S = ce.getAttribute(m, 'repSide')
        A = ce.getAttribute(m, 'repArea')
        I = ce.getAttribute(m, 'repID')
        
        n = 0
        
        #bool report value check
        print(m)   
        print('Row:',bool(R))
        print('Column',bool(C))
        print('Side',bool(S))
        
        #setting new variables only if there are values in R, C and S
        if bool(R) == True and bool(C) == True and bool(S) == True :
            Row = R
            Column = C
            Side = S
            Area = A 
            IDparcel = I 
                         
            print('Model:', m)
            print(Row)
            print(Column)
            print(Side)
               
        else :
            print("THERE ARE NO VALUES IN REPORTS") 

    for m in models :
        print("test m", m)
        shapes = ce.convertModelsToShapes(m)
        print('Shapes:', shapes)
        newShapes = ce.separateFaces(shapes)
        print('New shapes:', newShapes)
        ce.setRuleFile(newShapes, 'roman-houses.cga')
        ce.setStartRule(newShapes, 'LotDivided')
        objects = ce.getObjectsFrom(newShapes, ce.isShape)
        print("***")
        print('Objects:', objects)
        
        objectDict = {}
        keyList = []
                              
        n=0
        for o in objects:
            ce.setAttributeSource(o, "/ce/rule/repRow", "USER")
            ce.setAttributeSource(o, "/ce/rule/repCol", "USER")
            ce.setAttributeSource(o, "/ce/rule/repSide", "USER")
            ce.setAttributeSource(o, "/ce/rule/repArea", "USER")
            ce.setAttributeSource(o, "/ce/rule/repID", "USER")
                         
            ce.setAttribute(o, "/ce/rule/repRow", Row)
            ce.setAttribute(o, "/ce/rule/repCol", Column)
            ce.setAttribute(o, "/ce/rule/repSide", Side)
            ce.setAttribute(o, "/ce/rule/repArea", Area)
            ce.setAttribute(o, "/ce/rule/repID", IDparcel)
            
            
            print('#',ce.getName(o))
            objectDict[ce.getName(o)] = o
            keyList.append(ce.getName(o))
                        
            n += 1
        print(n)
                
        keyList = sorted(keyList)
        
        n = 0
        for i in keyList:
            ce.setAttributeSource(objectDict[i], "/ce/rule/rowLot", "USER")
            ce.setAttribute(objectDict[i],"/ce/rule/rowLot", Row[n])
            ce.setAttributeSource(objectDict[i], "/ce/rule/columnIndexLot", "USER")
            ce.setAttribute(objectDict[i],"/ce/rule/columnIndexLot", Column[n])
            ce.setAttributeSource(objectDict[i], "/ce/rule/setSideTypeInner", "USER")
            ce.setAttribute(objectDict[i],"/ce/rule/setSideTypeInner", Side[n])
            n += 1 
             
            
    print("="*30)
            
def subblockSelection():
    shapes = ce.getObjectsFrom(ce.scene, ce.isShape)

if __name__ == '__main__':
    convertModelsToShapes()

pass